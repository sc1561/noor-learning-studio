from pathlib import Path
import base64
root=Path(__file__).resolve().parents[1]
logo='data:image/svg+xml;base64,'+base64.b64encode((root/'assets/logo.svg').read_bytes()).decode()
page=(root/'index.html').read_text().replace('<link rel="stylesheet" href="assets/style.css?v=1.5.2">','<style>'+(root/'assets/style.css').read_text()+'</style>').replace('assets/logo.svg',logo)
for name in ['core.js','catalog.js','grade5-labs.js','grade6-labs.js','labs.js','app.js']:
 code=(root/'assets'/name).read_text().replace('assets/logo.svg',logo)
 for doc in ['CONTENT-GUIDE.md','ARCHITECTURE.md','NOOR.md']:
  uri='data:text/plain;charset=utf-8;base64,'+base64.b64encode((root/'docs'/doc).read_bytes()).decode()
  code=code.replace('href="docs/'+doc+'"','href="'+uri+'" download="'+doc+'"')
 zipuri='data:application/zip;base64,'+base64.b64encode((root/'downloads/noor-studio-extension-v1.5.2.zip').read_bytes()).decode()
 code=code.replace('downloads/noor-studio-extension-v1.5.2.zip',zipuri)
 page=page.replace('<script src="assets/'+name+'?v=1.5.2"></script>','<script>'+code+'</script>')
(root.parent/'noor-learning-studio-preview.html').write_text(page)
