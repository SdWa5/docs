# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.22.2] - 2026-10-05

### Changed

- The PhpStorm project config holds the settings of both machines. It carries the `sdwa5-3d` source, test and
  include paths and the PHPUnit configuration, and the excludes of the removed `trackdsp` checkout are gone.

## [0.22.1] - 2026-10-05

### Changed

- The external link check runs weekly on Mondays instead of nightly.

### Fixed

- The external link check excludes `sdwa5-dsp`, whose missing exclude made the run of 2026-10-05 fail. Both
  link jobs now take the sibling repositories from one list.

## [0.22.0] - 2026-10-05

### Added

- `docs/services.md` describes the PayPal sync through the BankSync fork, built but not live yet.
- `README.md` lists `sdwa5-banksync` among the sub-repositories.
- `docs/organization.md` records that Revolut is ruled out and the SEPA, IBAN and card gaps of a
  PayPal-only Verein as proposals.

### Changed

- `.gitignore` covers the nested `sdwa5-banksync` checkout.

## [0.21.0] - 2026-10-05

### Changed

- `trackdsp` is now `sdwa5-dsp`, published as `SdWa5/dsp`. It is linked from `README.md`, gitignored and
  registered as a VCS root under its new name, and the docs workflow checks it out for the link check like the
  other two siblings.
- `docs/going-public.md` covers the fourth repository, with its two redactions, its licence, the lock dialog and its publication.
- The `README.md` entry for `sdwa5-dsp` names the gain riders, measurements and Auto EQ.

## [0.20.0] - 2026-10-01

### Added

- `TODO.md` item 5 plans a mapping engine inspired by Mapshroom and Resolume. Its USPs are a camera video
  feedback loop and a doubled perspective correction, and it is to be controllable from a browser and a phone.

## [0.19.0] - 2026-09-30

### Changed

- [docs/going-public.md](docs/going-public.md) records the flip. All three repositories went public on
  2026-09-30, after a last scan of every blob, every commit message and the 37 Actions log archives.
- It records the identity regression of 2026-09-29 as well. Four `sdwa5-3d` commits carried the business
  address and were rewritten and republished on 2026-09-30, with the `HEAD` tree unchanged, and an
  `includeIf` in the global git config now pins the noreply identity for every clone under `sdwa5/`.
- The `ssh-hardening.md` re-read is done. One sentence stays, and the stale one is fixed in `sdwa5-vps`
  1.50.1.

### Fixed

- Two places said the authorship trailers stay, although they were removed on 2026-09-15 and none is
  left in any of the three histories.

### Removed

- The go-public item from `TODO.md`, because it is done. The later items move up by one.

## [0.18.0] - 2026-09-30

### Added

- `trackdsp` sits next to `sdwa5-vps` and `sdwa5-3d` as a nested repository. It is gitignored,
  registered as a VCS root in `.idea/vcs.xml` and listed in `README.md` without a link, because it
  lives outside the SdWa5 organization and CI cannot clone it for the link check.

## [0.17.0] - 2026-09-16

### Added

- **[docs/going-public.md](docs/going-public.md) now measures the plugin carve-out instead of
  assuming it.** The four plugin directories `sdwa5-vps` carries as source declare MIT in their own
  `composer.json`, so republishing them is permitted. The carve-out's wording stays, because it also
  has to cover whatever gets vendored next.
- A note that the same measurement found five further plugins active on the shop that no repository
  records, and that this belongs in `sdwa5-vps/TODO.md` rather than on a disclosure page.

## [0.16.0] - 2026-09-15

### Added

- **`docs/services.md` records that the VPS now hosts a site for someone else.** The artist website
  Chimo Diazz gets `chimodiazz.sdwa5.org`, and the section says plainly that this is a favour rather
  than an SdWa5 service, that the association's Impressum ends up attached to content it does not
  write, and who owns which half of the work. The technical side lives in
  [`sdwa5-vps/docs/chimodiazz.md`](sdwa5-vps/docs/chimodiazz.md).

## [0.15.0] - 2026-09-15

### Security

- **The fifth history rewrite ran, over all three repositories.** The authorship trailers came out of
  every commit message, `.idea/scopes` out of every commit of this repository, and in `sdwa5-vps` two
  real secrets and six people's names out of theirs. One `git-filter-repo` run each, messages and
  contents together.
- **The trailers came out through a message callback rather than a text replacement**, because a
  replacement only empties the text and leaves the blank line behind. The callback drops whole lines
  and trims what they leave, and it is scoped to Claude and Anthropic so an attribution line naming a
  human would survive. There was none.
- **The content is provably untouched in all three.** Commit counts are 71, 166 and 147 before and
  after, and the trees at `HEAD` are `d95e57c5`, `c586aec3` and `2f562d25` before and after, so only
  commit objects changed. The working trees had been corrected by ordinary commits first, precisely so
  that this invariant could hold while content was still leaving the history.
- **All three were republished rather than force-pushed.** Verified afterwards: every probe term
  returns zero over every blob and every commit message, the two removed paths appear in no commit, a
  pre-rewrite SHA answers `not our ref`, and a control fetch of `main` succeeds. `sdwa5-vps` is 184
  tests green with shellcheck clean and this repository's link check reports no errors.

### Changed

- `docs/going-public.md` records how the pass was run and what proves it, and `TODO.md` carries the
  result of the audit of the two repositories that had not had one.

## [0.14.1] - 2026-09-15

### Changed

- **`.claude/` is gitignored, like it already was in `sdwa5-3d`.** The project settings file exists
  only to switch off the authorship attribution, so committing it would disclose exactly what the
  same day's rewrite removed from every commit message.

## [0.14.0] - 2026-09-15

### Security

- **The authorship trailers are being removed, which reverses a decision taken the same day.** The
  first answer was to keep them. The owner decided otherwise, and the deciding argument is ordering:
  a trailer is permanent in every public clone the moment a repository is published, so it is cheap
  to remove now and impossible to remove later. Measured before removal: of the three repositories'
  376 commits, 225 carried an attribution line and 211 a session link, naming 31 distinct sittings,
  and no attribution line ever named a human.
- **`.idea/scopes` named an unrelated employer and is untracked.** Two PhpStorm scope definitions
  pointed at `htdocs/…` paths that do not exist in this repository, and the file sat in 66 of 67
  commits. That association is exactly what two history rewrites and a repository move were run to
  remove from the commit headers, and it survived in a tracked file where no scanner would ever flag
  it, because a company name is not a credential. The file held nothing else, so it goes rather than
  gets edited, and the history goes with it.
- **`pull_request` is no longer a trigger.** A fork's pull request would spend runner time on
  attacker-supplied Markdown. No step interpolates `github.event.*` into a shell argument, so there
  was no injection sink, but free compute for strangers buys this repository nothing.
- **The Vaultwarden posture in `docs/services.md` is down to one line.** The thinning of 2026-09-12
  removed the per-account figures and left the conclusions standing. A reachable host read next to a
  named owner, a count of weaker accounts and a stated single point of failure is a targeting
  statement whatever the figures say.
- **`docs/google-workspace.md` no longer says which mailbox carries which service credential.** One
  row made a single account the Shopware SMTP holder, the Let's Encrypt contact and the owner of the
  backup folder, in one sentence. No credential was ever in a repository; the sentence was the map.

### Changed

- **The Rechnungsprüfer conflict is stated by role rather than against a person.** The defect belongs
  to the association, and it belongs in the same amendment as the four defects in the statutes. Both
  stay published, because an association that names its own defects and fixes them stands better than
  one where somebody else finds them.
- **The two deferred board names keep their roles and dates, decided rather than defaulted.** The
  point of deferring was that this repository should not be the publisher, not that the names become
  unfindable, and the ZVR number is in the shop's Impressum by law. Recorded so the question does not
  come up a third time.
- **`.idea/` is named in the licence split.** It was 15 of the 30 tracked files and fell under
  neither clause, while `LICENSE-docs` delegates its own scope back to the README.

### Added

- **`docs/going-public.md` carries the 2026-09-15 audit of this repository and of `sdwa5-vps`**, the
  same four passes `sdwa5-3d` had. It opens with a correction to the method, because the earlier runs
  described as "without the allowlist" were not: gitleaks reads a `.gitleaks.toml` found in the scan
  target even without `--config`, and the export carried one. Repeating them properly is what turned
  the `sdwa5-vps` result from clean to not clean.

## [0.13.4] - 2026-09-15

### Changed

- **The authorship trailers stay, decided 2026-09-15, and that was the last open item before the
  flip.** `docs/going-public.md` had the question down as a property of `sdwa5-3d` alone and with
  figures that a later push had overtaken. Re-measured across all three repositories: 122 of 164
  commit messages in `sdwa5-3d`, 69 of 143 in `sdwa5-vps` and 33 of 65 here, with 18, 18 and 13
  distinct session ids. So a decision for one repository would have come back twice.
- **The session URLs were checked rather than assumed.** Fetched without a session cookie one answers
  HTTP 403, so it is an opaque identifier and not a readable transcript. What publication discloses is
  that the work was AI-assisted and how many sittings it took, and none of it is in file contents.
- **Kept, because the attribution was the honest answer to how this work was made**, and a set of
  repositories that has just been through four rewrites to make its own record true is the wrong place
  to understate authorship. The alternative was a fifth rewrite across three repositories and three
  more republish cycles, each carrying the risk the 2026-09-15 pass demonstrated when it rewrote
  another session's in-flight branch along the way.
- `TODO.md` and `docs/going-public.md` now both say that nothing blocks the flip.

## [0.13.3] - 2026-09-15

### Security

- **The fourth history rewrite ran, so the PSL decision is real rather than cosmetic.** 0.13.1 narrowed
  the claim on `docs/going-public.md` to the working tree and left the history as an open decision.
  Both statements stood in 28 of `sdwa5-3d`'s 162 commits, in two of its commit messages and in two
  commits of this repository, so publishing either repository would have published them whatever the
  tree said. `git-filter-repo` ran over file contents and commit messages together, with 13
  replacements.
- **The content is provably untouched in both.** The commit counts are 162 and 61 before and after,
  and the tree at `HEAD` is `d440b3e8` and `37d1beed` before and after, so only commit objects changed.
- **Both were republished rather than force-pushed**, by renaming the repository, creating it empty,
  pushing, confirming the tip and then deleting the old one. A force-push leaves the pre-rewrite
  commits reachable by SHA in GitHub's cache; recreating leaves no cache. Verified in both afterwards:
  seven probe phrases return zero matches over every blob and every message, a pre-rewrite SHA answers
  `not our ref`, and a control fetch of `main` succeeds.
- **`sdwa5-vps` was deliberately not touched**, because another session was working in it at the time.
  It carries none of the affected text, measured the same day over all 141 of its commits.

### Changed

- `TODO.md` records the rewrite under "configure repos as public". The one item still open before the
  flip is the authorship trailers in 119 of `sdwa5-3d`'s commit messages.

## [0.13.2] - 2026-09-15

### Changed

- **`docs/services.md`: the ERP is no longer only the accounting system.** It now also holds the
  organization's operational backlog in the Projects module, written in from a gitignored spec by
  `sdwa5-vps/tools/dolibarr/sync-pm.sh`. The split is stated so it is not re-derived later: the
  repositories' `TODO.md` files stay technical, and purchases, deadlines, event settlements and
  Verein administration live in the ERP.

## [0.13.1] - 2026-09-14

### Fixed

- **This repository's 0.13.0 entry and `docs/going-public.md` both quoted the PSL inference while
  recording its removal**, which is the failure that page already has a lesson about. The quote is
  gone from both.
- **The same page claimed more than had happened.** `sdwa5-3d` 0.117.0 cleaned the two files it named
  and left the assertion standing in that repository's changelog and in `docs/sources.md`, which is
  the file the third-party section was written about. Finished in `sdwa5-3d` 0.117.1, and the claim
  here now says working tree where it used to say removed.
- **The history is now stated as an open decision rather than left implied.** Both PSL statements
  stand in 28 of `sdwa5-3d`'s 160 commits and one of them in a commit message, measured 2026-09-14.
  Nothing is exposed while the repository is private, so the choice is a fourth rewrite before the
  flip or an explicit decision to keep them. `TODO.md` carries it next to the authorship trailers.

## [0.13.0] - 2026-09-14

### Added

- **`docs/going-public.md` gains a section on what changes at the flip itself**, which the page never
  had, because everything on it until now was about content rather than behaviour. Two things were
  checked for `sdwa5-3d` and both are written up. Its workflow has no `pull_request` trigger and reads
  no `secrets`, so a stranger's fork cannot make it execute anything once the repository is public.
  And 119 of its 158 commit messages carry an authorship trailer with a session URL, 16 distinct ones,
  which becomes public with the repository and is the one item on that page nobody has decided.

### Changed

- **The `sepp` decision covered a nickname and not the full name, which is also in the history.**
  `sdwa5-3d/TODO.md` names the owner of the second van in full, in the working tree and in 78 of that
  repository's 158 commits. It surfaced on 2026-09-14 through a sweep for common given names rather
  than through the redaction patterns, which had no reason to carry it. Kept on the same ground as the
  nickname, decided the same day, so no fourth history rewrite is needed.
- **PSL's inventory is no longer inferred from what they bring to one event.** The third-party section
  cleared `sdwa5-3d/docs/sources.md` and named the GMSS owner and the Innschleife crew as content.
  PSL are a rental company who were never asked, and `rosters/psl-next-event.yaml` had turned a
  statement about one load-out into a floor on their stock. Corrected in `sdwa5-3d` 0.117.0, and the
  reasoning is recorded here.
- **The same section now says that the clearance covers one file while the content is in fifteen
  more**, namely `rosters/`, `docs/requests.md`, `docs/scenes.md`, `TODO.md`, `CHANGELOG.md` and about
  twenty spec files. That part is the same shape as `sources.md` and needs no further decision,
  because the two crews cleared their inventory rather than one document.
- **The 2026-09-13 rewrite is verified rather than asserted.** All 22 replacement patterns were run
  over the full history of the pre-rewrite backup and of the current repository, contents and commit
  messages together. The backup answers with 8 patterns matching, one of them 25 times, which is what
  proves the test works, and `sdwa5-3d` answers with zero across all 158 commits.
- **A second lesson joins the one about notes quoting what they redact.** An allowlist can exempt
  tracked files while its own comment says it does not, which is what `sdwa5-3d/.gitleaks.toml` did to
  four committed files under `.ddev/` for as long as it existed. Running the scanner once with the
  allowlist off is the cheap check.

## [0.12.0] - 2026-09-14

### Fixed

- **The nightly `links-external` job had never passed, and its failure mail is most of what looks
  like GitHub Actions running at random.** Measured on run `34830869821`: exit code 2 on three
  errors, all of them links to the sibling *directories* themselves, written as
  ``[sdwa5-vps](sdwa5-vps)`` and ``[sdwa5-3d](sdwa5-3d)``, twice in `README.md` and once in this
  file. Both jobs excluded the siblings as `--exclude sdwa5-vps/`, but lychee matches `--exclude` as
  a regular expression against
  the resolved URI, and a link to a bare directory produces a URI with no trailing slash. So the
  pattern matched `sdwa5-vps/docs/caddy.md` and missed `sdwa5-vps`. The trailing slash is gone from
  both jobs.
- **Why `links` stayed green while `links-external` went red on the same files.** `links` checks the
  siblings out first, and `actions/checkout` leaves the directory behind even when the fetch fails,
  so the bare link resolves there. `links-external` checks out nothing, so it does not. The
  behaviour is recorded next to the loop that builds the exclusions.

### Changed

- The `schedule` trigger now records that its time is a request rather than a promise. Measured on
  the same run: `23 4 * * *` asked for 04:23 UTC and the run started at 09:59 UTC, 5 h 36 m late.
  GitHub queues scheduled events and drops them under load, so a failure mail from this workflow
  says nothing about the hour it names, and a missing night is not evidence of a fault.
- `TODO.md` no longer claims that CI is blocked account-wide on billing. That was measured on
  2026-09-08 and stopped being true: runs execute and complete in all three repositories from
  2026-09-13 onwards. What going public still buys is unmetered minutes and a four-core runner in
  place of a private repository's two, and the first executed `sdwa5-3d` push is the evidence for
  why the core count matters.

## [0.11.1] - 2026-09-14

### Fixed

- `docs/going-public.md` still claimed in the present tense that the shop's Impressum publishes the
  old address. **It stopped being true on 2026-09-14**, when the storefront was updated. Both
  sentences are now in the past tense and the closing note records what a fetch of each page finds,
  which is Egitlweg 6 and no trace of the old address. A document about what is safe to publish is
  the last place an untrue present-tense claim belongs.

## [0.11.0] - 2026-09-14

### Added

- **[`docs/statuten.md`](docs/statuten.md)**, the full statutes as a Markdown reading copy, converted
  from `Vereinsstatuten.docx` and checked page by page against the stamped scan. The authoritative
  version stays the stamped scan; the file says so. `docs/organization.md` links to it.

### Fixed

- **Paragraph citations of the statutes were one paragraph too high, in this repository's plan
  documents and in two letters drafted for the Vereinsbehörde.** Word carries the numbering as
  automatic list numbering, so the text holds none of it, and the first reconstruction put the
  Vorstand at § 11. It is **§ 10**. Corrected: the Vorstand's meeting rules are § 10 Abs. 4 to 6 and
  not § 11, the signature rule is **§ 12 Abs. 2** and not § 11 Abs. 2, and the clause giving the
  Vorstand the last word over the Generalversammlung is **§ 8 Abs. 8** and not Abs. 9. Verified
  twice, against § 7 of the statutes, which states their own structure, and against all seven pages
  of the stamped scan.

### Notes

- **The filed statutes carry the same off-by-one in three of their own cross-references.** § 8
  Abs. 2 lit. d and lit. e cite "§ 11 Abs. 2" and § 13 Abs. 3 cites "§ 11 Abs. 8 bis 10"; all three
  mean the Vorstand at § 10, and § 11 has no such clauses. The template they were adapted from
  evidently had the Vorstand one paragraph further down. Together with the unfilled template line in
  § 1 Abs. 3, the § 8 Abs. 8 clause and a numbering restart in § 15, that is four defects, all listed
  in `docs/statuten.md` and all belonging in the same future amendment.

## [0.10.0] - 2026-09-14

### Changed

- **The Zustellanschrift is Egitlweg 6, 5322 Hof bei Salzburg, Österreich, since 2026-09-14**, by
  resolution of the Vorstand. `docs/organization.md` carries it and a new section
  **Address change, in progress since 2026-09-14** that keeps the two moves apart: the postal
  address has changed and is a free notification under § 14 Abs 3 VerG, while the **Sitz** is still
  Ostermiething because § 1 Abs 2 of the statutes names it and moving it is a Statutenänderung under
  § 14 Abs 1 VerG, needing a two-thirds resolution of the Generalversammlung.
- The **Registration authority** row no longer reads as permanent. Competence follows the Sitz, so
  both notifications go to Bezirkshauptmannschaft Braunau am Inn, and only after the Sitz move is
  registered does it pass to Bezirkshauptmannschaft Salzburg-Umgebung in Seekirchen am Wallersee.
- The source line now says what it actually covers. The register extract of 2026-07-04 is the source
  for every row **except** the Zustellanschrift, because the ZVR still shows the old address until
  the notification is processed.

### Added

- `docs/going-public.md`: an update stating that the disclosure reasoning for the old address carries
  over to the new one unchanged, and that `Mühlenstraße 24` stays in the history rather than earning
  a fourth rewrite. It was the lawfully published address of the Verein throughout that period, and
  every rewrite costs another force-push cycle.

### Notes

- Nothing outside the repositories has been changed yet. The storefront Impressum, Datenschutz and
  AGB pages, the Dolibarr company record, Google Workspace, PayPal and the domain registrant still
  carry the old address, and the notification to the authority has not been filed.

## [0.9.1] - 2026-09-13

### Fixed

- **`docs/going-public.md` said deleting the personal repositories "removed the cache". That conflated
  unreachable with destroyed.** GitHub restores a deleted repository within 90 days, so the record
  outlives the delete and the REST API reports 404 long before the content is gone. Six repositories
  are inside that window: the three personal ones deleted 2026-09-12 and the three `-old` ones the
  2026-09-13 rewrite deleted, each restorable until roughly 2026-12-11 with the pre-rewrite history
  intact.
- The measurement that does hold is narrower, and it is the one the threat model needed: fetching a
  pre-rewrite SHA from each new repository returns `not our ref`, with a control fetch proving the test
  itself works, so a reader holding an old hash cannot pull it. Restoring needs owner or
  organization-admin credentials, so there is no route to it from outside and no publication decision
  waits on it. Tracked as item 7.6 in `sdwa5-vps/TODO.md`.

## [0.9.0] - 2026-09-13

An independent audit of all three repositories on 2026-09-13 found that
[docs/going-public.md](docs/going-public.md) certified several items as closed that were not, and that
the file was itself one of the leaks it certified. Everything below is measured against `origin/main`
rather than reasoned from the previous notes.

### Security

- **A bare surname survived both the tree edit and the 2026-09-12 rewrite**, standing alone inside a
  parenthetical in `docs/organization.md` one line from a date the board table repeats. The redaction
  rules matched full names, so nothing matched it. It was in **40 of this repository's 45 commits** and
  in the working tree.
- **Commit messages were never rewritten.** `git-filter-repo` applies `--replace-text` to file contents
  only; messages need the separate `--replace-message`. The commit that performed the redaction
  therefore carried all three names verbatim in its own body, here and in `sdwa5-3d`.
- **The Vaultwarden redaction was undone by the sentences describing it.** `docs/going-public.md` and
  this file each still quoted a per-account figure while explaining why that figure had been removed,
  in **31 of 45 commits** and in the working tree. `sdwa5-vps`'s `TODO.md` restated the whole pairing
  with more detail than the table had ever held, which the corresponding entry there now removes.
- **A private email address sits in this repository's `TODO.md` history**, in 4 of 45 commits. Every
  rewrite so far was scoped to `sdwa5-vps`, so this one had never been looked for here.
- **The mailbox table mapped two local-parts to a board role.** `docs/google-workspace.md` now says
  "board member" instead, which is what created the join rather than the addresses themselves.
- **All three repositories were rewritten over contents and messages together** on 2026-09-13. Each
  kept its commit count and its `HEAD` tree.

### Changed

- `docs/services.md` loses the paragraph that explained why the per-account Vaultwarden figures were
  removed, because it restated them. One sentence is left, that three accounts are on PBKDF2 and only
  their holders can change that. The cipher and collection counts and the `emergency_access` row count
  go with it; that the organization has a single Owner stays, because a single point of failure is
  worth naming.
- `docs/services.md`, `CHANGELOG.md` and `docs/google-workspace.md` refer to board members and to the
  new member by role rather than by name, matching what
  <https://sdwa5.org/Impressum> publishes, which is the Obmann alone.
- `.gitleaks.toml` **stops allowlisting `^\.idea/`**, reversing the earlier decision. Every tracked
  file there and every `.idea/` path that ever held a blob is clean, so the allowlist bought nothing
  while blinding the scanner to the one directory PhpStorm writes database and SSH credentials into
  without being asked.
- `docs/going-public.md` and `TODO.md` record what the earlier passes actually achieved rather than
  what they claimed, and keep the one lesson that caught this list twice: a note documenting a
  redaction tends to quote the thing it redacted, and neither a tree scan nor `gitleaks` will see it.

## [0.8.3] - 2026-09-12

### Fixed

- **The `links` job was red the first time it ever ran, and the guard was the reason.** It tested
  `[ -d "$dir/.git" ]` to decide whether a sibling repository had been cloned, but `actions/checkout`
  creates the directory and initialises `.git` *before* it fetches, so a failed checkout leaves both
  behind with nothing under them. Both siblings reported "checked out", nothing was excluded, and
  lychee called about sixty working cross-repository links broken. It now tests
  `git -C "$dir" rev-parse --verify HEAD`, because only a fetch that succeeded produces a commit.
- Measured on run 34700494948: the sibling checkouts fail with "Not Found", because this repository's
  `GITHUB_TOKEN` cannot read a sibling repository even inside the same organization. That is the
  designed-for case, and the job's own warning already says the remedy is a `SIBLING_REPOS_TOKEN`
  secret or making the repositories public. The bug was only that the guard never noticed.

### Measured, and worth stating plainly

- **The organization has its own Actions allowance and CI runs again.** Every run in all three
  repositories had failed in 3 to 5 seconds since 2026-09-08 with "recent account payments have
  failed", which was the personal account's exhausted balance. Since the move to `SdWa5`, `secrets`
  passes in 8 to 11 seconds and `static` in 40. So going public is no longer what unblocks CI. It
  still buys unlimited minutes and 4-core runners rather than 2.

## [0.8.2] - 2026-09-12

### Security

- **The board members' names are out of the history, not just out of the tree.** 41 commits rewritten,
  tree hash unchanged at `7f99283f`, commit count 41 before and after. Zero commits now contain either
  Obmann-Stellvertreter's name, the former Obmann-Stellvertreterin's, or the Vaultwarden KDF and item
  values. `Mühlenstraße 24` is kept in 39 of the 41 and `Stefan Ripper` in 39, both on purpose, because
  <https://sdwa5.org/Impressum> publishes them by law.
- `sdwa5-vps` went the same way in 1.31.1: 117 commits, tree hash unchanged at `e49d1314`, zero names,
  the address kept in all 117, and `.gitleaks.toml`'s allowlisted commit `9f800d7` still reachable, so
  the secret scan is unaffected. `SdWa5/3d` needed no rewrite, carrying none of the three names in any
  of its 152 commits.

## [0.8.1] - 2026-09-12

### Fixed

- **The notes documenting the name redaction named the people being redacted.** `CHANGELOG.md`,
  `TODO.md` and `docs/going-public.md` carried all three names across eleven lines, written in the same
  change that took them out of `docs/organization.md`. So the tree was not clean and neither would the
  history have been. They now read as roles. The redactor grew a catch-all pass for exactly this,
  because its shaped rules only knew the table and prose forms the names had in `organization.md`, and
  loose prose in a changelog matches none of them.

## [0.8.0] - 2026-09-12

Every open decision in `docs/going-public.md` is made. Two of them reverse what that file used to
recommend, because the shop's own Impressum publishes more than the analysis assumed.

### Added

- **A licence, in all three repositories.** MIT in `LICENSE` for code and configuration, CC BY-SA 4.0
  in `LICENSE-docs` for prose, documentation and data, with each `README.md` naming which directories
  fall on which side. The root `README.md` said "No license specified — all rights reserved", which
  published unchanged would have meant a reader may reuse nothing, not a diagram, not a script, not a
  spec.
- Two carve-outs are stated rather than left implied. `sdwa5-vps/shopware-html-data/` is
  store-installed Shopware plugin content under its vendors' own terms, and any mesh a `sdwa5-3d` spec
  reaches through `mesh_override` is third-party CAD, deliberately uncommitted, with its provenance in
  that repository's `docs/sources.md`.

### Changed

- **Two board members' names defer to the ZVR register, and the Obmann's does not.** The two
  Obmann-Stellvertreter are replaced by their roles in `docs/organization.md` and
  `docs/google-workspace.md`, because <https://sdwa5.org/Impressum> does **not** name them, so this
  repository would have been the only publisher. `Stefan Ripper` stays, because that Impressum names
  him as Obmann by law and he authored all 304 commits, so removing it from three documents would
  change nothing a reader could not already see.
- **The former board member is gone entirely**, name and dates. She left in 2024 and the current ZVR
  extract does not list her either.
- **The Vaultwarden table loses its KDF and Items columns** and keeps one sentence, that three
  accounts are on PBKDF2 and only their holders can change that. The pairing was the finding rather
  than either figure: beside a reachable `vault.sdwa5.org`, a row naming which active account holds
  how many items on the weaker KDF names the soft target and prices it.

### Fixed

- **The recommendation to remove the residential address was wrong, and the address stays.**
  <https://sdwa5.org/Impressum> publishes `Mühlenstraße 24` today and an Austrian webshop is required
  by law to state a Zustellanschrift, so taking it out of git while the shop publishes it is theatre.
  It is in all 115 commits of `sdwa5-vps` for that reason. What did come out is the `c/o <name>`
  prefix, so the repositories no longer say whose home it is, which the Impressum does not say either.

### Measured, and worth stating plainly

- **The trees are clean and the histories are not, which is the same trap the email address set.**
  The two Obmann-Stellvertreter remain in 32 of this repository's 37 commits and 95 of
  `sdwa5-vps`'s 115, the former Obmann-Stellvertreterin in 32 of this repository's, and the Vaultwarden values in
  23. A rewrite over both is prepared and was refused three times by the environment's
  `[Git Destructive]` guard, so it is outstanding. `SdWa5/3d` needs none. This is the only item left
  that cannot be done after the repositories are public.

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

- `docs/services.md` described both Dolibarr and Vaultwarden as having one account in use with two
  more planned. Neither was true, measured on 2026-09-08. Dolibarr has three enabled accounts, two of
  which were created on 2025-07-08 and have never been logged into, so they are provisioned rather
  than planned. Vaultwarden has four accounts, two of them in active use.

### Added

- `docs/services.md` records two decisions taken on 2026-09-08. Emergency access with a Takeover
  grantee is being set up with a new member, and the two unused Vaultwarden accounts are kept rather
  than deleted, because neither holds anything and deleting an account someone was invited to costs
  more explaining than it saves.
- `docs/services.md` records the Vaultwarden accounts with their organization role, and states plainly
  that the organization has a single Owner, so losing that account loses the organization's data until
  a grantee is confirmed.

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
