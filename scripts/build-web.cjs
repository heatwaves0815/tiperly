const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const out = path.join(root, 'web');
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });
for (const file of ['index.html', 'styles.css', 'dark.css', 'app.js', 'manifest.webmanifest', 'sw.js', 'icon.svg']) {
  fs.copyFileSync(path.join(root, file), path.join(out, file));
}
console.log(`Web-App gebaut: ${out}`);
