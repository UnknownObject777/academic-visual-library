"""Set PNG physical-resolution metadata without changing image-data bytes."""
import argparse,struct,zlib
from pathlib import Path

def stamp_png(raw,dpi):
    if not raw.startswith(b'\x89PNG\r\n\x1a\n'):raise ValueError('Input is not PNG')
    if dpi<=0:raise ValueError('DPI must be positive')
    ppm=round(dpi/.0254);pos=8;out=bytearray(raw[:8]);seen=False
    while pos<len(raw):
        if pos+12>len(raw):raise ValueError('Truncated PNG')
        n=struct.unpack('>I',raw[pos:pos+4])[0];end=pos+12+n
        if end>len(raw):raise ValueError('Truncated PNG chunk')
        tag=raw[pos+4:pos+8]
        if tag!=b'pHYs':out.extend(raw[pos:end])
        if tag==b'IHDR':
            data=struct.pack('>IIB',ppm,ppm,1);payload=b'pHYs'+data
            out.extend(struct.pack('>I',len(data))+payload+struct.pack('>I',zlib.crc32(payload)&0xffffffff));seen=True
        pos=end
    if not seen:raise ValueError('Missing PNG IHDR')
    return bytes(out)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('png',type=Path);p.add_argument('--dpi',type=float,required=True)
    a=p.parse_args();a.png.write_bytes(stamp_png(a.png.read_bytes(),a.dpi))
