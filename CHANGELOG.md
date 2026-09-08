# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.6.0] - 2026-09-08

### Added

- [docs/going-public.md](docs/going-public.md), the half of the go-public content check that a scanner
  cannot do. The credential half is done and gated in CI, and all three repositories are clean in tree
  and history. This is the list of things that are not credentials and would still become
  world-readable, each with its evidence and a recommendation. The file deliberately describes each
  item without reproducing the address, name or value, because it is published too.
- **The finding that matters most is the commit identities.** Measured: all 95 commits in `sdwa5-vps`
  are authored and committed as a private address on a third-party provider, and 162 across `sdwa5`
  and `sdwa5-3d` as a work address on a business domain. No file change touches that, only a history
  rewrite does, and that is practical only while the repositories are private with two clones each and
  no forks. It is the one item on the list whose window is closing.
- The rest are recorded as decisions: a private residential address and a former board member's name
  in `docs/organization.md`, both of which the public ZVR register also carries; the per-account
  Vaultwarden KDF and item counts in `docs/services.md`, which are anonymised but read differently
  next to three named board members and a reachable `vault.sdwa5.org`; roughly 40 attributions and 49
  quotations of another sound system owner's private messages about their own gear in
  `sdwa5-3d/docs/sources.md`; and four Minecraft pseudonyms with their UUIDs.
- Recorded that the published infrastructure detail is deliberate, since `TODO.md` gives "No security
  by obscurity" as the guideline, and that the identifiers which do appear are useless without access.
- Restated the licence question as a decision with its three usual shapes, rather than as an omission.

## [0.5.1] - 2026-09-08

### Fixed

- `actions/checkout` bumped from `v4` to `v5`. GitHub forces `v4` onto Node 24 and warns that it is
  deprecated. **Unverified on GitHub**, because no job can currently run — see below.

### Added

- `TODO.md` records that **CI is blocked account-wide on billing**, measured 2026-09-08. Every run in
  all three repositories fails within 2 to 4 seconds with "The job was not started because recent
  account payments have failed or your spending limit needs to be increased", including runs that
  predate this work. So no pipeline in any of the three repositories is verified on GitHub.
- The consumption behind it is measured and recorded: all three repositories are private, so Actions
  minutes are metered, and `sdwa5-3d` spends them. One push costs about 2 h 15 m for the `phpunit` job
  alone, against 23 minutes locally, and one nightly costs about 548 minutes because the `full` job
  runs 6 h 1 m and is then killed at GitHub's 6-hour ceiling. Three consecutive nightlies were
  cancelled that way between 5 and 7 September.
- This turns going public from a preference into the fix: a public repository gets Actions minutes
  free and unlimited.

## [0.5.0] - 2026-09-08

### Added

- Continuous integration, in [.github/workflows/docs.yml](.github/workflows/docs.yml). This repository
  had no CI at all. Three jobs run: `links` resolves every relative link and every `#anchor` against
  the filesystem on each push, `links-external` fetches external URLs nightly, and `secrets` scans the
  working tree and the full history for credentials.
- [lychee.toml](lychee.toml) configures the link checker. External URLs are checked nightly rather
  than per push, because a rate limit or a briefly unreachable host fails a build for reasons that
  have nothing to do with the commit.
- [.gitleaks.toml](.gitleaks.toml) configures the secret scanner. It extends the upstream rule set
  rather than replacing it, and allowlists the two gitignored sibling repositories, which run the same
  scan in their own CI.
- The link check covers cross-repository links such as `../sdwa5-vps/docs/caddy.md`, which was the
  point of the item it closes. `sdwa5-vps` and `sdwa5-3d` are gitignored sibling directories rather
  than submodules, so CI clones them separately. While they are private that clone needs a
  `SIBLING_REPOS_TOKEN` secret; without it the job stays green and warns that those links were skipped
  rather than checked, instead of reporting them as broken.
- `TODO.md` records the result of the go-public secret scan, the missing `sdwa5-3d` transfer, the
  licence question and the Google Drive duplicates.

### Changed

- The secret scanner is the gitleaks CLI rather than `gitleaks/gitleaks-action`. That action requires
  a licence key for repositories owned by a GitHub Organization, and moving these repositories into an
  `sdwa5` organization is the plan, so the action would stop working at exactly the wrong moment. The
  CLI is MIT and needs no key.

### Fixed

- `CHANGELOG.md` had the entry from commit `eb93397` under `Unreleased` although that commit shipped
  as 0.4.0 and `composer.json` was never bumped past it. Moved into 0.4.0 where it belongs.

## [0.4.0] - 2026-09-08

### Fixed

- `docs/services.md` said both Dolibarr and Vaultwarden had "currently only Stefan; Sepp and Ziri
  planned". Neither was true, measured on 2026-09-08. Dolibarr has three enabled accounts, and the
  Sepp and Ziri ones were created on 2025-07-08 and have never been logged into, so they are
  provisioned rather than planned. Vaultwarden has four accounts, two of which are in active use with
  differing numbers of items.

### Added

- `docs/services.md` records two decisions taken on 2026-09-08. Emergency access with a Takeover
  grantee is being set up with a new member, and the two Vaultwarden accounts holding zero
  items are kept rather than deleted, because neither holds data and deleting an account someone was
  invited to costs more explaining than it saves.
- `docs/services.md` records the Vaultwarden accounts with their KDF, item count, last activity and
  organization role, and states plainly that the SdWa5 organization has a single Owner holding 32
  ciphers in 5 collections while `emergency_access` has zero rows, so losing that account loses the
  organization's data.

## [0.3.0] - 2026-07-30

### Added

- New sub-repository [`sdwa5-3d`](sdwa5-3d) — spec-driven parametric 3D models of the speakers and
  stage equipment, for Blender event previews and PA setup planning. Its own docs, TODO and
  changelog live in that repo
- `README.md`: `sdwa5-3d` listed under sub-repositories
- `TODO.md`: delegation to [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
- `.gitignore`: `/sdwa5-3d` — nested repos stay separate, same as `/sdwa5-vps`
- `.idea/vcs.xml`: `sdwa5-3d` registered as a VCS root; `.idea/developer-tools.xml` added

### Changed

- `composer.json`: description mentions `sdwa5-3d`

### Fixed

- `CHANGELOG.md`: backfilled the missing `0.2.0`–`0.2.8` entries from their commit messages, and
  corrected `0.1.0`, which listed `README.md`, `CHANGELOG.md` and `docs/` although those arrived in
  `0.2.0`

## [0.2.8] - 2026-07-07

### Removed

- `TODO.md`: TODO format consistency item — obsolete, docs TODO sections all resolved; numbered
  lists kept (resolved items get deleted, not checked off)

## [0.2.7] - 2026-07-07

### Changed

- `TODO.md`: infrastructure diagram item resolved (diagram in `sdwa5-vps/docs/infrastructure.md`)

## [0.2.6] - 2026-07-07

### Added

- `docs/services.md`: Google Workspace/Drive, PayPal, social accounts (Facebook, Instagram, YouTube,
  SoundCloud), GitHub, Minecraft, Ollama sections; Dolibarr/Vaultwarden user info
- `README.md`: explicit docs separation (`docs/` = org-level what/why, `sdwa5-vps/docs/` =
  technical how)

### Changed

- `TODO.md`: services.md TODO resolved, "resolve TODOs" item removed

### Removed

- `docs/services.md`: TODO section
- `docs/google-workspace.md`: `swda5.system@` alias (deleted in Workspace) + typo note

## [0.2.5] - 2026-07-04

### Fixed

- `docs/google-workspace.md`: Shared Drive "SdWa5" is central storage (previously stated no Shared
  Drives in use)

## [0.2.4] - 2026-07-04

### Added

- `docs/google-workspace.md`: nonprofit status, admin, users, group + aliases, drive/backup relation

### Changed

- `TODO.md`: google-workspace.md TODO resolved

### Removed

- `docs/google-workspace.md`: TODO section

## [0.2.3] - 2026-07-04

### Added

- `docs/organization.md`: board (Vorstand), Rechnungsprüfer, PayPal payment info, statutes summary,
  documents section
- `docs/organization.md`: public ZVR register fetch URL

### Changed

- `docs/organization.md`: legal identity extended (Sitz, founding date, registration authority,
  Zustellanschrift)
- `docs/google-workspace.md`, `docs/services.md`: links updated to split shopware docs
- `TODO.md`: organization.md TODO resolved

### Removed

- `docs/organization.md`: TODO section

## [0.2.2] - 2026-07-03

### Added

- `.idea/laravel-idea.xml` for Inertia package configuration

### Changed

- `TODO.md`: readability improved by replacing static paths with relative links
- `.idea/misc.xml`: removed redundant `SshConsoleOptionsProvider` component
- `.idea/sdwa5.iml`: added source directory mappings for custom plugins and test folders

## [0.2.1] - 2026-07-01

### Changed

- `TODO.md`: documentation tasks streamlined and refined. Removed outdated project description and
  added action to resolve TODOs in `docs/`

## [0.2.0] - 2026-07-01

### Added

- `README.md` with project overview and documentation references
- `CHANGELOG.md` adhering to Keep a Changelog format
- `docs/` — organization documentation: [organization.md](docs/organization.md) (legal and official
  organization information), [google-workspace.md](docs/google-workspace.md) (Google Workspace usage
  details), [services.md](docs/services.md) (overview of core services: Dolibarr, Vaultwarden,
  Shopware)
- `composer.json`: project description
- `.idea/git_toolbox_prj.xml` for IntelliJ Git settings

### Changed

- `TODO.md`: outdated entries removed and tasks streamlined

## [0.1.0] - 2026-07-01

### Added

- `.gitignore`
- `composer.json` with project metadata
- `TODO.md` with initial project documentation tasks
- Initial `.idea` project configuration: inspection profiles, module definition, dependency scopes
