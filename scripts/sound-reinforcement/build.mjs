// Prints the sound reinforcement handbook to one PDF through headless Chromium.
//
// Usage: node build.mjs [out.pdf]
// The default output is docs/assets/sound-reinforcement/sdwa5-sound-reinforcement.pdf. CHROME names the browser
// binary; without it, playwright-core uses the Chromium that `npx playwright-core install chromium` downloaded.
// The run fails if a diagram or a formula did not render.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { chromium } from 'playwright-core';
import { renderHtml, repoRoot } from './render.mjs';

const out = path.resolve(process.argv[2]
  ?? path.join(repoRoot, 'docs/assets/sound-reinforcement/sdwa5-sound-reinforcement.pdf'));
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sdwa5-sr-'));
const htmlPath = path.join(tmp, 'sound-reinforcement.html');
fs.writeFileSync(htmlPath, renderHtml());

const browser = await chromium.launch(process.env.CHROME ? { executablePath: process.env.CHROME } : {});
try {
  const page = await browser.newPage();
  await page.goto('file://' + htmlPath);
  await page.waitForFunction(() => document.body.dataset.done, null, { timeout: 60000 });
  const r = await page.evaluate(() => ({
    done: document.body.dataset.done,
    diagrams: document.querySelectorAll('pre.mermaid').length,
    rendered: document.querySelectorAll('pre.mermaid svg').length,
    formulas: document.querySelectorAll('.katex').length,
    formulaErrors: document.querySelectorAll('.katex-error').length,
  }));
  if (r.done !== 'ok' || r.rendered !== r.diagrams || r.formulaErrors) {
    console.error(JSON.stringify(r));
    process.exitCode = 1;
  } else {
    fs.mkdirSync(path.dirname(out), { recursive: true });
    await page.pdf({
      path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: '<div style="font:8pt sans-serif;width:100%;text-align:center;color:#666">'
        + '<span class="pageNumber"></span> / <span class="totalPages"></span></div>',
      margin: { top: '18mm', bottom: '18mm', left: '20mm', right: '20mm' },
    });
    console.log(JSON.stringify({ ...r, out }));
  }
} finally {
  await browser.close();
  fs.rmSync(tmp, { recursive: true, force: true });
}
