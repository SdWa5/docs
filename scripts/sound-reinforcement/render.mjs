// Renders the sound reinforcement handbook (index plus every chapter) into one self-contained HTML document.
// build.mjs prints it to PDF, and the tests check it without a browser.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import MarkdownIt from 'markdown-it';
import texmath from 'markdown-it-texmath';
import katex from 'katex';

export const here = path.dirname(fileURLToPath(import.meta.url));
export const repoRoot = path.resolve(here, '../..');

const siblings = {
  'sdwa5-3d': 'https://github.com/SdWa5/3d/blob/main/',
  'sdwa5-dsp': 'https://github.com/SdWa5/dsp/blob/main/',
  'sdwa5-vps': 'https://github.com/SdWa5/vps/blob/main/',
};

/**
 * Lists the source files in reading order as [sectionId, absolutePath]: the index as ch00, the numbered chapters,
 * then the appendices as appx1, appx2 and so on.
 */
export function sourceFiles(repo = repoRoot) {
  const dir = path.join(repo, 'docs/sound-reinforcement');
  const names = fs.readdirSync(dir).sort();
  return [['ch00', path.join(repo, 'docs/sound-reinforcement.md')]]
    .concat(names.filter(f => /^\d\d-.*\.md$/.test(f)).map(f => ['ch' + f.slice(0, 2), path.join(dir, f)]))
    .concat(names.filter(f => /^appendix-.*\.md$/.test(f)).map((f, i) => ['appx' + (i + 1), path.join(dir, f)]));
}

/** GitHub's heading slug: lowercase, punctuation dropped, spaces to hyphens. */
export const slug = s => s.trim().toLowerCase().replace(/<[^>]+>/g, '')
  .replace(/[^\p{L}\p{N}\- _]/gu, '').replace(/ /g, '-');

/**
 * Maps a Markdown link to its target in the single document. Links between chapters become in-document anchors
 * (section id plus heading slug), links to sibling repositories and other docs become GitHub URLs.
 */
export function rewriteHref(href, current, idOf) {
  if (/^[a-z]+:/i.test(href)) return href;
  const [p, a = ''] = href.split('#');
  if (!p) return '#' + current + '-' + a;
  const m = p.match(/^(?:\.\.\/)+(sdwa5-3d|sdwa5-dsp|sdwa5-vps)\/(.*)$/);
  if (m) return siblings[m[1]] + m[2] + (a ? '#' + a : '');
  const base = path.basename(p);
  if (idOf[base]) return '#' + idOf[base] + (a ? '-' + a : '');
  const rel = path.normalize(path.join(current === 'ch00' ? 'docs' : 'docs/sound-reinforcement', p));
  return 'https://github.com/SdWa5/docs/blob/main/' + rel + (a ? '#' + a : '');
}

/** Renders all chapters into one HTML page. `built` is the date printed in the footer note. */
export function renderHtml({ repo = repoRoot, built = new Date().toISOString().slice(0, 10) } = {}) {
  const files = sourceFiles(repo);
  const idOf = Object.fromEntries(files.map(([id, p]) => [path.basename(p), id]));
  let body = '';
  for (const [id, p] of files) {
    const md = new MarkdownIt({ html: false, linkify: false, typographer: false })
      .use(texmath, { engine: katex, delimiters: 'dollars' });
    const fence = md.renderer.rules.fence;
    md.renderer.rules.fence = (t, i, o, e, s) => t[i].info.trim() === 'mermaid'
      ? `<pre class="mermaid">${md.utils.escapeHtml(t[i].content)}</pre>` : fence(t, i, o, e, s);
    md.core.ruler.push('ids', st => {
      st.tokens.forEach((t, i) => {
        if (t.type === 'heading_open') {
          t.attrSet('id', id + '-' + slug(st.tokens[i + 1].children.map(c => c.content).join('')));
        }
        if (t.type === 'inline') {
          (t.children || []).forEach(c => {
            if (c.type === 'link_open') c.attrSet('href', rewriteHref(c.attrGet('href'), id, idOf));
          });
        }
      });
    });
    body += `<section class="chapter" id="${id}">${md.render(fs.readFileSync(p, 'utf8'))}</section>\n`;
  }

  const katexDir = path.join(here, 'node_modules/katex/dist');
  const css = fs.readFileSync(path.join(katexDir, 'katex.min.css'), 'utf8')
    .replace(/url\(fonts\//g, 'url(file://' + katexDir + '/fonts/');
  const mermaid = 'file://' + path.join(here, 'node_modules/mermaid/dist/mermaid.min.js');
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>SdWa5 — Sound reinforcement</title>
<style>${css}
body{font:10.5pt/1.45 "DejaVu Serif",Georgia,serif;color:#111;margin:0}
h1{font:600 20pt/1.2 "DejaVu Sans",sans-serif;margin:0 0 12pt}
h2{font:600 13.5pt/1.25 "DejaVu Sans",sans-serif;margin:18pt 0 6pt;break-after:avoid}
h3,h4{font:600 11pt/1.3 "DejaVu Sans",sans-serif;margin:12pt 0 4pt;break-after:avoid}
.chapter{break-before:page}.chapter:first-child{break-before:auto}
table{border-collapse:collapse;margin:8pt 0;font-size:9pt;break-inside:auto}
th,td{border:0.5pt solid #999;padding:2pt 5pt;vertical-align:top}
th{background:#eee}tr{break-inside:avoid}
blockquote{margin:8pt 0;padding:4pt 10pt;border-left:3pt solid #c90;background:#fff8e6;font-size:9.5pt}
code{font:9pt "DejaVu Sans Mono",monospace;background:#f3f3f3;padding:0 2pt}
pre{background:#f6f6f6;padding:6pt;font-size:8.5pt;white-space:pre-wrap}
pre.mermaid{background:none;text-align:center;break-inside:avoid}
a{color:#0645ad;text-decoration:none}
.katex-display{margin:6pt 0}
.built{font:8pt "DejaVu Sans",sans-serif;color:#666}
</style></head><body>
<p class="built">Built ${built} from github.com/SdWa5/docs. The Markdown pages there are the current version.</p>
${body}
<script src="${mermaid}"></script>
<script>mermaid.initialize({startOnLoad:false,theme:'neutral',flowchart:{htmlLabels:false}});
mermaid.run({querySelector:'pre.mermaid'}).then(()=>{document.body.dataset.done='ok'},
  e=>{document.body.dataset.done='error: '+e});</script>
</body></html>`;
}
