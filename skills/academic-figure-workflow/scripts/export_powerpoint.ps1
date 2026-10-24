param(
  [Parameter(Mandatory=$true)][string]$InputPptx,
  [Parameter(Mandatory=$true)][string]$OutDir,
  [Parameter(Mandatory=$true)][string]$PythonPath,
  [ValidateRange(72,1200)][int]$Dpi=600
)
$ErrorActionPreference='Stop'
$inputPath=(Resolve-Path -LiteralPath $InputPptx).Path
$outputPath=[IO.Path]::GetFullPath($OutDir)
New-Item -ItemType Directory -Path $outputPath -Force | Out-Null
$renderCopy=Join-Path $outputPath ('.render-input-'+[guid]::NewGuid().ToString()+'.pptx')
[IO.File]::Copy($inputPath,$renderCopy,$false)
$app=$null
$deck=$null
$bounds=@()
try {
  $app=New-Object -ComObject PowerPoint.Application
  # A unique copy prevents Open() from reusing/closing an already-open user deck.
  $deck=$app.Presentations.Open($renderCopy,-1,0,0)
  $width=[int][math]::Round($deck.PageSetup.SlideWidth/72*$Dpi)
  $height=[int][math]::Round($deck.PageSetup.SlideHeight/72*$Dpi)
  for($i=1;$i -le $deck.Slides.Count;$i++){
    $slide=$deck.Slides.Item($i)
    try {
      $png=Join-Path $outputPath ('figure-{0:D2}.png' -f $i)
      if(Test-Path -LiteralPath $png){throw "Use a fresh render directory; output exists: $png"}
      $slide.Export($png,'PNG',$width,$height)
      & $PythonPath (Join-Path $PSScriptRoot 'png_dpi.py') $png --dpi $Dpi
      if($LASTEXITCODE -ne 0){throw 'PNG metadata operation failed'}
      foreach($shape in $slide.Shapes){
        try {
          if($shape.HasTextFrame -eq -1 -and $shape.TextFrame.HasText -eq -1){
            $text=$shape.TextFrame.TextRange
            try {
              $bounds += [pscustomobject]@{slide=$i;name=$shape.Name;text=$text.Text;font=$text.Font.Name;fontPt=$text.Font.Size;
                x=$shape.Left;y=$shape.Top;width=$shape.Width;height=$shape.Height;
                boundX=$text.BoundLeft;boundY=$text.BoundTop;boundWidth=$text.BoundWidth;boundHeight=$text.BoundHeight;
                overflow=($text.BoundWidth -gt $shape.Width+.5 -or $text.BoundHeight -gt $shape.Height+.5)}
            } finally {[void][Runtime.InteropServices.Marshal]::ReleaseComObject($text)}
          }
        } finally {[void][Runtime.InteropServices.Marshal]::ReleaseComObject($shape)}
      }
    } finally {[void][Runtime.InteropServices.Marshal]::ReleaseComObject($slide)}
  }
  ConvertTo-Json -InputObject @($bounds) -Depth 5 | Set-Content -LiteralPath (Join-Path $outputPath 'text-bounds.json') -Encoding utf8
  Write-Output "Exported $($deck.Slides.Count) canvases at ${Dpi} dpi: ${width}x${height} pixels. Inspect every PNG."
} finally {
  if($null -ne $deck){$deck.Close();[void][Runtime.InteropServices.Marshal]::ReleaseComObject($deck)}
  if($null -ne $app){[void][Runtime.InteropServices.Marshal]::ReleaseComObject($app)}
  if(Test-Path -LiteralPath $renderCopy){Remove-Item -LiteralPath $renderCopy}
}
