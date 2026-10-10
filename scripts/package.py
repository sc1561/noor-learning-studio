from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import sys
root=Path(__file__).resolve().parents[1]
if sys.argv[1]=='extension':
 with ZipFile(root/'downloads/noor-studio-extension-v1.4.0.zip','w',ZIP_DEFLATED) as z:
  for p in (root/'extension').rglob('*'):
   if p.is_file():z.write(p,p.relative_to(root/'extension'))
else:
 with ZipFile(root.parent/'noor-learning-studio-v1.4.0.zip','w',ZIP_DEFLATED) as z:
  for p in root.rglob('*'):
   if p.is_file() and not any(x in p.parts for x in ['.git','node_modules','__pycache__']):z.write(p,Path('noor-learning-studio')/p.relative_to(root))
