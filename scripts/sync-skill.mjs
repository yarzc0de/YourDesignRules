#!/usr/bin/env node
// Copies rules/, guides/, and archetypes/ into skills/your-design-rules/references/
// so the skill folder is self-contained when an installer copies only that folder.
//
//   node scripts/sync-skill.mjs          write the copies
//   node scripts/sync-skill.mjs --check  exit 1 if the copies are out of date (used in CI)

import { readdirSync, readFileSync, writeFileSync, mkdirSync, rmSync, existsSync, statSync } from "node:fs";
import { join, relative, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const sources = ["rules", "guides", "archetypes"];
const dest = join(root, "skills", "your-design-rules", "references");
const check = process.argv.includes("--check");

function listFiles(dir) {
  if (!existsSync(dir)) return [];
  return readdirSync(dir).flatMap((name) => {
    const full = join(dir, name);
    return statSync(full).isDirectory() ? listFiles(full) : [full];
  });
}

const expected = new Map();
for (const src of sources) {
  for (const file of listFiles(join(root, src))) {
    if (!file.endsWith(".md")) continue;
    expected.set(join(dest, relative(root, file)), readFileSync(file, "utf8"));
  }
}

if (check) {
  const actual = new Set(listFiles(dest));
  const problems = [];
  for (const [path, content] of expected) {
    if (!actual.has(path)) problems.push(`missing: ${relative(root, path)}`);
    else if (readFileSync(path, "utf8") !== content) problems.push(`stale:   ${relative(root, path)}`);
    actual.delete(path);
  }
  for (const extra of actual) problems.push(`extra:   ${relative(root, extra)}`);
  if (problems.length) {
    console.error("Skill references are out of sync. Run: node scripts/sync-skill.mjs");
    for (const p of problems) console.error("  " + p);
    process.exit(1);
  }
  console.log(`Skill references in sync (${expected.size} files).`);
} else {
  rmSync(dest, { recursive: true, force: true });
  for (const [path, content] of expected) {
    mkdirSync(dirname(path), { recursive: true });
    writeFileSync(path, content);
  }
  console.log(`Wrote ${expected.size} files to ${relative(root, dest)}/`);
}
