# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.7.4] - 2026-09-12

### Changed

- **The three repositories live in the [SdWa5](https://github.com/SdWa5) organization**, moved there
  on 2026-09-12 as [docs](https://github.com/SdWa5/docs), [vps](https://github.com/SdWa5/vps) and
  [3d](https://github.com/SdWa5/3d). The organization belongs to the Verein rather than to a personal
  account, with `mail@sdwa5.org` as its contact address, that being the existing Workspace group
  rather than one of the two addresses the plan named, which `docs/google-workspace.md` records as not
  existing yet.
- **Moved by a fresh push and not by GitHub's transfer function**, which is what actually removed the
  cached pre-rewrite commits of both history rewrites. Three empty repositories were created and
  pushed into, then the three personal originals were deleted. Verified: each new `main` matches its
  local `HEAD`, zero commits on `SdWa5/vps` hold the private address, and all three old paths answer
  "Not Found".

### Fixed

- **Three places pointed at repository paths that the deletion turned into 404s**, and one of them was
  a broken build rather than a broken link. `.github/workflows/docs.yml` checked out
  `bestcodename/sdwa5-vps` and `bestcodename/sdwa5-3d` for the cross-repository link check, and now
  checks out `SdWa5/vps` and `SdWa5/3d`. `lychee.toml` excluded `^https://github\.com/bestcodename/`
  from link checking because those repositories were private, and now excludes
  `^https://github\.com/SdWa5/` for the same reason. `docs/services.md` listed two repositories under
  the personal account and now lists all three under the organization, with why they were pushed
  rather than transferred.

## [0.7.3] - 2026-09-12

### Changed

- **The repositories are to be published by a fresh push into the `sdwa5` organization, never by
  GitHub's transfer function**, and `docs/going-public.md` and `TODO.md` now say so. A transfer moves
  the same repository and the same object store, so it would carry every cached pre-rewrite commit
  into the new organization and quietly undo both history rewrites. A force-pushed commit stays
  reachable by its SHA until GitHub garbage-collects, and that has no schedule worth planning around,
  since it is triggered by repository maintenance rather than by a clock. Creating the repository
  empty and pushing clears the residue and performs the move in one action.
- Measured on 2026-09-12, nothing is lost by publishing that way: all three repositories are private
  with **0 forks, 0 tags and 0 releases**, no pull requests and no issues, at 54 KB, 6380 KB and
  980 KB. What goes is the Actions run history, every run of which failed on billing, and one
  stargazer on `sdwa5-vps`.
- Stated plainly in both files: **nothing is exposed while the repositories are private**, because an
  unreachable object is unreachable to anyone without access to the repository. The risk is entirely
  one of ordering.

## [0.7.2] - 2026-09-12

### Fixed

- **0.7.0's "no commit carries a private or a business email address any more" is true of the commit
  identities and false of the file contents, and `docs/going-public.md` now says so.** That rewrite
  replaced the author and committer fields of every commit, which is a different thing from what a
  file says. Measured on 2026-09-12 in `sdwa5-vps`: the current tree is clean, and **74 of the 113
  commits still contain the private address**, in all five files at once — `README.md`,
  `monitoring/lib.sh`, `.env.example`, `docs/monitoring.md` and `docs/infrastructure.md`. The earliest
  carrying commit is the first on the branch and the latest is 1.5.0 on 2026-09-01. `gitleaks` does
  not catch it and never would, because an email address is not a credential.
- **It is fixed the same day, in `sdwa5-vps` 1.30.0.** The address was removed from all 74 commits
  together with its separator rather than substituted, because on every line it stood next to
  `ripper@sdwa5.org` as the second recipient. Verified afterwards: `HEAD`'s tree hash unchanged at
  `c887c215`, 113 commits before and after, zero commits reachable from `origin/main` holding it, and
  no doubled recipient anywhere. `docs/going-public.md` now records the work items as done and names
  the one step that is left, which belongs to GitHub rather than to git: a force-pushed commit stays
  reachable by SHA until the repository is garbage-collected.

### Changed

- **The third-party question in `docs/going-public.md` is decided, and the decision is to publish.**
  The owner of GMSS and the Innschleife crew are both known personally to the association's owner, who
  states that neither objects to their inventory being public. The content was checked at the same
  time rather than taken on trust: all 60 distinct quoted strings in `sdwa5-3d/docs/sources.md` are
  dimension enumerations, cabinet names or phrases out of a published datasheet, with no opinion, no
  third person, no price and no commercial term in any of them.
- **The manufacturer specifications were examined and are not a publishing risk**, which was the
  question that prompted this. Dimensions, weights and performance figures are facts and carry no
  copyright; what a datasheet protects is its prose, its drawings and its photographs, and
  `sdwa5-3d` commits none of those. Verified: zero PDFs, zero images, zero CAD and zero meshes are
  tracked in that repository, and the longest quoted string anywhere in its specs is a single line of
  figures. The genuine licence questions there attach to the *open* designs rather than to the
  commercial ones, because those are the ones whose CAD was written by somebody else, and that CAD
  lives outside git under an ignored `meshes/` on purpose.

## [0.7.1] - 2026-09-11

### Changed

- **Every job states a `timeout-minutes`, and the workflow states a `concurrency` group.** GitHub's default
  timeout is 360 minutes, and that default is what let `sdwa5-3d`'s `full` job burn roughly 1644 minutes across
  three nightly runs in September before anybody saw a log, because a job cancelled at the ceiling reports only
  that it was cancelled. The concurrency group cancels a superseded push. It is deliberately **not** applied on
  `main`, because a merge commit's green run is what a release is judged by.
  On `main` that also stops a push cancelling the nightly external link check mid-flight.

  Nothing here is expensive — this repository's runs are well under a minute — so the change is about the rule being the same
  in all three SdWa5 repositories rather than about the minutes.


## [0.7.0] - 2026-09-08

### Security

- **All three repository histories were rewritten, so no commit carries a private or a business email
  address any more.** Before: 95 commits in `sdwa5-vps` authored and committed as a private address on
  a third-party provider, and 162 across `sdwa5` and `sdwa5-3d` as a work address on a business
  domain. Publishing a repository publishes every one of them, so this was the only item in
  `docs/going-public.md` whose window closed the moment the repositories went public. Every commit
  now carries `Stefan Ripper <7108645+bestcodename@users.noreply.github.com>` as author and committer,
  verified on GitHub as well as locally, and the commits are still attributed to the `bestcodename`
  account so the contribution graph survived.
- **The content is provably untouched.** The tree hash at `HEAD` is identical to its pre-rewrite value
  in all three repositories, `dbbe151333fb`, `e7d94eebd0ad` and `1981e6b43b7b`, so only the commit
  objects changed.
- `sdwa5-vps` carried a **local** `user.email` override set to the private address, which is why that
  repository's commits differed from the other two, and the next commit would have reintroduced
  exactly what the rewrite removed. All three now set the noreply address as a local identity, and the
  machine's global identity is deliberately left alone because the work address is correct for other
  projects.
- `/opt/docker` on the VPS was moved with `fetch` plus `reset --hard` and **never a re-clone**, because
  it holds the untracked runtime state of the whole stack with `minecraft-data` alone at 6.9 GiB.
  Verified afterwards: the 6.9 GiB is still there, the rotated `server.properties` is still there, the
  tree is clean, and all eight health checks are green.

### Added

- `docs/going-public.md` records how it was done, so it is repeatable: `git-filter-repo` as a single
  script needing no installation, a two-line mailmap built from the repositories themselves rather
  than typed out, bare backups of all three first, and a force push per repository with a
  `--force-with-lease` on its exact pre-rewrite commit, so a concurrent push elsewhere would have
  aborted it rather than been overwritten.

## [0.6.1] - 2026-09-08

### Fixed

- **"Four copies of `AmpLimiterCalc.csv`" overstated what was measured**, in 0.5.0 and in `TODO.md`.
  Re-measured: the four files share a name but have **three distinct sizes**, 7700, 7718 and 7432
  bytes with the last appearing twice at the same timestamp. So three are hand-kept versions and only
  one pair is a true duplicate. That is stronger evidence for the drift the repository-as-master
  decision is meant to remove, not weaker, because somebody is versioning by duplicating a filename.
  It also changes the remedy from a delete into a reading job.
- Dropped the claim that both `Drivers.csv` and `drivers.csv` sit in that folder. Both were listed
  earlier in the day and only `drivers.csv` is present now, at 554 bytes, so the pair is not something
  to assert. Deleting or renaming anything there needs a write scope in any case, since the `SdWa5:`
  remote is `scope = drive.readonly`.

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
