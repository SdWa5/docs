// Checks the single-document rendering without a browser: every chapter and appendix is in, every formula renders and every
// in-document link lands on a heading. Run with `node --test` from scripts/sound-reinforcement/.
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { renderHtml, rewriteHref, slug, sourceFiles } from '../render.mjs';

const html = renderHtml({ built: '2000-01-01' });
const files = sourceFiles();

test('every chapter file becomes one section', () => {
  assert.equal(files.length, 22);
  assert.equal((html.match(/<section class="chapter"/g) || []).length, files.length);
});

test('every formula renders without a KaTeX error', () => {
  assert.ok((html.match(/class="katex"/g) || []).length > 100);
  assert.equal((html.match(/katex-error/g) || []).length, 0);
});

test('every mermaid block is handed to mermaid', () => {
  const fences = files.reduce((n, [, p]) => n + (fs.readFileSync(p, 'utf8').match(/^```mermaid$/gm) || []).length, 0);
  assert.ok(fences > 0);
  assert.equal((html.match(/<pre class="mermaid">/g) || []).length, fences);
});

test('every in-document link lands on an id', () => {
  const ids = new Set([...html.matchAll(/ id="([^"]+)"/g)].map(m => m[1]));
  const targets = [...html.matchAll(/ href="#([^"]+)"/g)].map(m => m[1]);
  assert.ok(targets.length > 20);
  assert.deepEqual(targets.filter(t => !ids.has(t)), []);
});

test('links are rewritten for one document', () => {
  const idOf = { 'sound-reinforcement.md': 'ch00', '03-decibels-levels-loudness.md': 'ch03' };
  assert.equal(rewriteHref('03-decibels-levels-loudness.md#dbu', 'ch02', idOf), '#ch03-dbu');
  assert.equal(rewriteHref('#mains', 'ch17', idOf), '#ch17-mains');
  assert.equal(rewriteHref('../../sdwa5-3d/docs/signal-chain.md#mains', 'ch17', idOf),
    'https://github.com/SdWa5/3d/blob/main/docs/signal-chain.md#mains');
  assert.equal(rewriteHref('acoustics.md', 'ch00', idOf), 'https://github.com/SdWa5/docs/blob/main/docs/acoustics.md');
  assert.equal(rewriteHref('https://example.org/a', 'ch01', idOf), 'https://example.org/a');
  assert.equal(slug('Why 32 dB and 26 dB'), 'why-32-db-and-26-db');
});
