// Keeps the appendix complete: every abbreviation the book uses is listed, and every listed abbreviation is used
// and links to a chapter that contains it. Run with `node --test` from scripts/sound-reinforcement/.
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { sourceFiles } from '../render.mjs';

// Words with at least two capitals that are names of products, software, venues, publishers or people, or
// roman numerals, rather than abbreviations.
const NOT_ABBREVIATIONS = new Set(['ArrayCalc', 'CATT', 'CD', 'CRC', 'DCX2496', 'DIY', 'EASE', 'GitHub', 'II', 'III',
  'ISBN', 'IV', 'LaTeX', 'MAPP', 'MARK', 'MIT', 'MM14K', 'McCarthy', 'NL2', 'NL4', 'NL8', 'ODEON', 'PDF', 'REW',
  'SdWa5', 'TIP10000q', 'TRUE1', 'TV']);
// Standard numbers are listed with their titles in each chapter's Sources instead.
const STANDARD = /^(AES|CTA|DIN|EIA|EN|IEC|IEEE|ISO|ITU|RFC|SMPTE)-?\d/;
const TOKEN = /(?<![\p{L}\p{N}_/-])(?=[\p{L}\p{N}]*\p{Lu}[\p{L}\p{N}]*\p{Lu})[\p{Lu}\p{N}][\p{L}\p{N}]*(?:-[\p{Lu}\p{N}]+)*(?![\p{L}\p{N}_])/gu;

const files = sourceFiles();
const appendix = files.find(([id]) => id.startsWith('appx'))[1];
const chapters = files.filter(([id]) => !id.startsWith('appx')).map(([, p]) => p);
const prose = text => text.replace(/\]\([^)]*\)/g, ']').replace(/`[^`]*`/g, '').replace(/\$[^$]*\$/g, '');
const tokens = text => [...prose(text).matchAll(TOKEN)].map(m => m[0]);
const uses = (text, token) => new RegExp(`(?<![\\p{L}\\p{N}_])${token.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}s?(?![\\p{L}\\p{N}_])`, 'u')
  .test(text);

const appendixText = fs.readFileSync(appendix, 'utf8');
const rows = appendixText.split('\n').filter(l => l.startsWith('| ') && !l.startsWith('| Abbreviation'));
const listed = new Set(rows.flatMap(l => tokens(l.split('|')[1])));
const abbreviationRows = rows.map(l => l.split('|').map(c => c.trim()))
  .filter(c => /^\[[A-Z0-9]+\]\(/.test(c[4] || ''));

test('every abbreviation in the chapters is in the appendix', () => {
  const missing = new Set();
  for (const p of chapters) {
    for (const t of tokens(fs.readFileSync(p, 'utf8'))) {
      const base = t.replace(/s$/, '');
      const stem = t.replace(/(-\d+)+$/, '');
      if (NOT_ABBREVIATIONS.has(t) || STANDARD.test(t) || listed.has(t) || listed.has(base) || listed.has(stem)) {
        continue;
      }
      missing.add(`${t} (${path.basename(p)})`);
    }
  }
  assert.deepEqual([...missing], []);
});

test('every listed abbreviation is used and its chapter contains it', () => {
  assert.ok(abbreviationRows.length > 100);
  const dir = path.dirname(appendix);
  const all = chapters.map(p => fs.readFileSync(p, 'utf8')).join('\n');
  const wrong = [];
  for (const c of abbreviationRows) {
    const ts = tokens(c[1]);
    for (const t of ts) if (!uses(all, t)) wrong.push(`${t} is not used`);
    const target = c[4].match(/\]\(([^)#]+)\)/);
    if (!target || !ts.length) continue;
    const text = fs.readFileSync(path.join(dir, target[1]), 'utf8');
    if (!ts.some(t => uses(text, t))) wrong.push(`${c[1]} is not in ${target[1]}`);
  }
  assert.deepEqual(wrong, []);
});
