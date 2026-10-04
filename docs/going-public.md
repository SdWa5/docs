# Going public: what publishing would disclose

The three SdWa5 repositories were private and went public on 2026-09-30, which was tracked in
[`../TODO.md`](../TODO.md) until it was done. That item asked for a scan of the content first. **The
credential half of that is done and automated.** `gitleaks` runs over the working tree and the full
history of all three repositories in CI, and all three are clean as of 2026-09-08.

This document is the other half, the one a scanner cannot do. Nothing below is a leaked credential.
Every item is something real that publishing would make world-readable and search-engine-indexable,
and each is a decision rather than a defect.

**This file is itself public.** So it describes each item and names its location, and it deliberately
does not reproduce the address, the name or the value in question. Read it next to the file it points
at.

## The one that could not be fixed later, and was done on 2026-09-08

**Every commit carries the identity that made it, and publishing a repository publishes all of them.**
What that used to be, measured before the rewrite:

| Repository | Commits | Authored as |
|---|---|---|
| `sdwa5` | 22 | a work address on a business domain |
| `sdwa5-3d` | 140 | the same work address |
| `sdwa5-vps` | 95 | a private address on a third-party mail provider, as author *and* committer |

So the private address was published 95 times no matter what any file said, and the business domain
162 times across the other two, which linked the association's repositories to an unrelated employer.

**All three histories are rewritten.** Every commit in every repository now carries a single identity,
`Stefan Ripper <7108645+bestcodename@users.noreply.github.com>`, as author and as committer, and
neither old address appears anywhere. Verified on GitHub as well as locally, and the commits are still
attributed to the `bestcodename` account, so the contribution graph survived.

**It regressed once, on 2026-09-29, and was rewritten again on 2026-09-30.** Four `sdwa5-3d` commits,
two releases and their merges, were made in a clone whose git identity fell back to the business
address, as author and as committer. The desktop clone was not the source, because its config had
carried the noreply identity since 2026-09-15 and its reflog shows only a fetch of those commits. The
four were rewritten with `git filter-repo --mailmap`, the tree at `HEAD` stayed identical, and the
repository was republished rather than force-pushed, so the pre-rewrite head is no longer fetchable. Two
Actions runs had carried the address in their `head_commit` metadata, and they went with the deleted
repository. An `includeIf "gitdir:~/PhpstormProjects/sdwa5/"` in the global git config now sets the
noreply identity for every clone under that directory, so a fresh clone no longer inherits the default.

**The content is provably untouched.** The tree hash at `HEAD` is identical to its pre-rewrite value in
all three repositories, so only the commit objects changed:

| Repository | Tree at `HEAD`, before and after |
|---|---|
| `sdwa5` | `dbbe151333fb` |
| `sdwa5-vps` | `e7d94eebd0ad` |
| `sdwa5-3d` | `1981e6b43b7b` |

How it was done, in case it is ever needed again. `git-filter-repo` runs as a single script and needs
no installation, driven by a two-line mailmap built from the repositories themselves rather than typed
out. It removes `origin`, so the remotes were re-added and each repository force-pushed with a
`--force-with-lease` on its exact pre-rewrite commit, so a concurrent push elsewhere would have
aborted it rather than been overwritten. Bare backups of all three were taken first.

**The two things that would have undone it, and were therefore also done.** `sdwa5-vps` carried a
*local* `user.email` override set to the private address, which is why that repository's commits
differed from the other two, so the next commit would have reintroduced exactly what the rewrite
removed. All three repositories now set the noreply address as a local identity, and the machine's
global identity is deliberately left alone, because the work address is correct for other projects.

And **`/opt/docker` on the VPS was moved with `fetch` plus `reset --hard`, never a re-clone.** It holds
the untracked runtime state of the whole stack, `minecraft-data` alone being 6.9 GiB, so a fresh clone
would have discarded it. Verified afterwards: 6.9 GiB still there, the rotated `server.properties`
still there, tree clean, and all eight health checks green.

## Personal data of named people

**DECIDED 2026-09-12, and two of the three came out.** The board members' names now defer to the ZVR
register, the Vaultwarden posture is thinned, and the address stays. The reasoning for each is below,
kept because the address decision reverses the recommendation this file used to make.

**The tree was done before the histories were, and the first rewrite did not finish the job.** Removing
a name from the working tree does not remove it from the history, which is the same trap the email
address set. That much was understood, and a rewrite ran on 2026-09-12. An independent audit on
2026-09-13 found three ways it fell short, all of them measured:

- **A bare surname survived, because the rules matched full names.** One deputy's surname stood alone
  inside a parenthetical in [`organization.md`](organization.md), one line from a date the board table
  repeats, and it was in 40 of this repository's 45 commits and in the working tree.
- **Commit messages were never touched.** `git-filter-repo` applies `--replace-text` to file contents
  only; messages need the separate `--replace-message`. So the commit that performed the redaction
  carried all three names in its own body, in this repository and in `sdwa5-3d`.
- **`sdwa5-3d` was declared clean without being checked.** It carried a deputy's full name as a test
  fixture in 153 of its 154 commits, and a changelog line asserting the three names appear nowhere in
  it.

**All three are fixed and the histories were rewritten again on 2026-09-13**, this time over contents
and messages together. See "What is left to do".

**A private residential address**, in [`organization.md`](organization.md). The association's service
address is care-of a named board member at their home. The Austrian
[ZVR register](https://citizen.bmi.gv.at/at.gv.bmi.fnsweb-p/zvn/public/Registerauszug) already
publishes it against the association's ZVR number, so this discloses nothing legally private. It is
still an escalation, because a register you query on purpose is not the same as a page Google
indexes.

**Kept, and the recommendation this file used to make was wrong.** The shop's own Impressum at
<https://sdwa5.org/Impressum> published `Mühlenstraße 24` while it was the current address, and an
Austrian webshop is required by law to state a Zustellanschrift. Taking it out of git while the shop publishes it is theatre, and
it is in all 115 commits of `sdwa5-vps` for exactly that reason. **What did come out is the `c/o
<name>` prefix**, so the repositories no longer say whose home it is, which the Impressum does not say
either. The only real remedy would be a Zustellanschrift that is not a private home, and that is a ZVR
filing rather than a documentation change.

**Update 2026-09-14: the address changed, and the reasoning carries over unchanged.** The
Zustellanschrift is now Egitlweg 6, 5322 Hof bei Salzburg, still care-of a board member's home and
still a second member's home. § 5 ECG obliges the shop to publish this one too, so it goes into the
repositories in plain text for the same reason the old one did, again without a `c/o <name>` prefix.
`Mühlenstraße 24` stays in the history of `sdwa5-vps` and this repository and is **not** worth a
fourth rewrite: it was the lawfully published address of the Verein throughout that period, it is
now a former address, and each rewrite costs another force-push cycle. The storefront was updated on 2026-09-14, so the
sentences above are in the past tense: the Impressum, the Datenschutz page and the German AGB now
carry Egitlweg 6, and a fetch of each finds no trace of the old address.

**Four full names with roles and dates**, in the same file. **Three of the four now defer to the ZVR
register and one is kept**, decided on the same evidence as the address.

The former board member who left in 2024 is gone entirely, name and dates, because she is no longer
involved and the current ZVR extract does not list her either. The two Obmann-Stellvertreter
are replaced by their roles, because the Impressum does **not** name them, so this repository would
have been the only publisher. `Stefan Ripper` stays: the Impressum names him as Obmann by law and he
authored all 304 commits, so taking the name out of three documents while every commit carries it
would be the same theatre as the address.

**A private email address in `sdwa5-vps`.** Removed from all five places in the working tree in
1.24.0 and moved into `.env` on the host, which is gitignored, with the effective alert recipients
unchanged.

**The history still carries it, and the item above is not the fix.** That rewrite replaced the author
and committer fields of every commit, which is a different thing from the contents of a file. Measured
on 2026-09-12: the current tree is clean, and **74 of the 113 commits still contain the address**, in
all five files at once — `README.md`, `monitoring/lib.sh`, `.env.example`, `docs/monitoring.md` and
`docs/infrastructure.md`. The earliest carrying commit is the first one on the branch and the latest is
1.5.0 on 2026-09-01.

**Done on 2026-09-12 in `sdwa5-vps` 1.30.0.** A second rewrite, over file contents rather than over
identities, removed the address together with its separator rather than substituting it, because on
every line it stood next to `ripper@sdwa5.org` as the second recipient. Verified afterwards: `HEAD`'s
tree hash is unchanged at `c887c215`, which it must be since the tree was already clean, the commit
count is 113 before and after, zero commits reachable from `origin/main` contain the address, and no
file anywhere in the history carries a doubled recipient. `.gitleaks.toml`'s allowlisted commit did
not move, checked rather than assumed.

**What remains is GitHub's own copy, and it is the same for all three repositories.** A force-pushed
commit stays reachable by its SHA on GitHub until the repository is garbage-collected, so `da46b79`
and its 74 siblings are still fetchable there by anyone who knows the hash. The two identity rewrites
of 2026-09-08 left the same residue in `sdwa5` and `sdwa5-3d`.

**GitHub's garbage collection has no schedule worth planning around.** It is internal and triggered by
repository maintenance rather than by a clock, and GitHub's own guidance for removing sensitive data
is to contact Support rather than to wait. Support can run one on request, which is free and
open-ended in time.

**Nothing is exposed while the repositories are private**, since an unreachable object is unreachable
to anyone without access to the repository. The whole risk is ordering, so the cache has to be cleared
before the flip to public rather than after it.

**Done on 2026-09-12, by pushing into fresh repositories rather than by transferring.** GitHub's
transfer function moves the same repository and the same object store, so a transfer into the
organization would have carried every cached pre-rewrite commit along with it and quietly undone both
rewrites. Three empty repositories were created in [SdWa5](https://github.com/SdWa5) instead and
pushed into, and the three personal repositories were then deleted. Verified: each new repository's
`main` matches its local `HEAD`, zero commits on `SdWa5/vps` hold the address, and all three old paths
answer "Not Found".

**That made the commits unreachable and it did not destroy them, which this file used to run
together.** Corrected on 2026-09-13. GitHub restores a deleted repository within 90 days, so the
record survives the delete and the REST API reports 404 well before the content is gone. The three
personal repositories can be brought back until roughly 2026-12-11, and the three `-old` repositories
that the 2026-09-13 rewrite deleted until a day later, each with the pre-rewrite history intact. The
measurement that does hold is narrower and is the one that matters: fetching a pre-rewrite SHA from
each new repository returns `not our ref`, with a control fetch proving the test itself works, so a
reader holding an old hash cannot pull it. Restoring needs owner or organization-admin credentials, so
there is no route to it from outside and no publication decision waits on it. Tracked as item 7.6 in
[`sdwa5-vps/TODO.md`](../sdwa5-vps/TODO.md), with the choice being to accept it, to let the window
close and verify after 2026-12-12, or to ask Support to purge the six permanently.

Nothing was lost by doing it that way. All three were private with **0 forks, 0 tags and 0 releases**,
no pull requests and no issues, at 54 KB, 6380 KB and 980 KB. What went is the Actions run history,
every run of which had failed on billing, and one stargazer on `sdwa5-vps`.

## A combination that is more revealing than its parts

[`services.md`](services.md) used to document the Vaultwarden accounts with their KDF, item count and
last activity alongside their organization role. Only the Owner is named; the others are deliberately
written as "second account", "third account" and "fourth account", so somebody already thought about
this.

The finding was the pairing rather than any single figure. A per-account row read next to a named,
reachable `vault.sdwa5.org` points at which account is worth attacking, and four accounts against
three board members is thinner anonymisation than it looks. Nothing in it was ever a credential.

**Done on 2026-09-12 and finished on 2026-09-13.** The per-account figures are out of the table and
one sentence is left, that three accounts are on PBKDF2 and only their holders can change that.
Upgrading those three to Argon2id would be the real remedy, but it depends on the account holders, so
nothing here waits on it.

**The first pass removed the values and left the sentences that quoted them.** This file and
`CHANGELOG.md` each still carried a figure while describing its removal, and `sdwa5-vps`'s `TODO.md`
restated the whole pairing with more detail than the table had ever held. All three are corrected, and
the 2026-09-13 rewrite took the figures out of both repositories' histories as well.

## Third parties who never agreed to any of this

`sdwa5-3d/docs/sources.md` sources many figures to **the owner of another sound system**, quoted
directly from private messages, roughly 40 attributions and 49 quoted strings. Publishing it
discloses another crew's inventory, cabinet dimensions and weights, together with their own words
about it. They gave the figures to help build a model, not to be published, and what a competing
system owns is commercially theirs.

The same file cites a rental company's published datasheets, which is ordinary use of public
material and needs no decision.

**Decided on 2026-09-12, and the decision is to publish it.** The owner of GMSS and the Innschleife
crew are both known personally to the association's owner, who states that neither objects to their
inventory being public. The content was checked rather than taken on trust at the same time: all 60
distinct quoted strings in that file are dimension enumerations, cabinet names or phrases out of a
published datasheet. The longest thing anybody says is "the ones on the outside of the bottom row are
also turbo subs". There is no opinion in it, no third person, no price and no commercial term. Two of
the quotations reach past speakers into amplifiers and lighting, and those are inventory lists in the
same shape.

If that ever needs undoing, the figures can stay while the quotations go, because provenance survives
as "stated by the owner" without reproducing the message.

**The paragraph above names one file, and the same kind of content is in fifteen more.** Measured on
2026-09-14, while `sdwa5-3d` was being read for publication. Verbatim quotations of private messages,
and figures derived from them, also sit in `rosters/`, `docs/requests.md`, `docs/scenes.md`, `TODO.md`,
`CHANGELOG.md` and about twenty spec files. Almost all of it is the same shape as `sources.md` and is
covered by the same clearance, because the GMSS owner and the Innschleife crew cleared their inventory
rather than one document.

**PSL are the exception, and one inference has been taken out.** They are Pro Sound & Light, a rental
company, and this page had them down only as the source of published datasheets, which needs no
decision. `rosters/psl-next-event.yaml` went past that. It turned a statement about what they are
bringing to one event into a floor on what they own, and `docs/requests.md` restated it. A published
package is not an inventory, which that file argued itself, and neither is a load-out. Nobody asked
PSL, and what a company owns is commercially theirs. So the counts stay as what is coming to an event,
the inference comes out, and the open question of asking them outright stays in `docs/requests.md`. A
second note characterising their published page rather than citing it is now a sourcing decision, with
every technical fact in it unchanged.

**The first pass at that was incomplete, and it failed in the way this page already has a lesson
about.** `sdwa5-3d` 0.117.0 cleaned the two files it named and did not search again afterwards. Its own
changelog entry then reproduced both statements while describing their removal, that repository's
0.109.0 entry still asserted outright what PSL own, and `docs/sources.md` still carried the verdict
about their page, in the very file this section was written about. Finished in `sdwa5-3d` 0.117.1, and
re-measured across the whole working tree rather than across the files that were edited.

**Correcting the working tree was not the end of it, and the history was rewritten on 2026-09-15.**
Both statements stood in 28 of `sdwa5-3d`'s 162 commits and one of them in two commit messages, so
publishing the repository would have published them whatever the tree said. That is the same ordering
argument the email address made, and the answer was the same. `git-filter-repo` ran over file contents
and commit messages together, with 13 replacements, on `sdwa5-3d` and on this repository.

**The content is provably untouched in both.** The commit counts are 162 and 61 before and after, and
the tree at `HEAD` is `d440b3e8` and `37d1beed` before and after, so only commit objects changed. Both
were **republished rather than force-pushed**, by renaming the repository, creating it empty, pushing,
confirming the tip and then deleting the old one, which is what leaves no object cache behind.
Verified afterwards in both: seven probe phrases return zero matches over every blob and every commit
message, a pre-rewrite SHA answers `not our ref`, and a control fetch of `main` succeeds.

**Minecraft player names and UUIDs**, in `sdwa5-vps` in `minecraft-data/ops.json`,
`minecraft-data/whitelist.json` and the `OPS` and `WHITELIST` environment variables in
`docker-compose.yml`. Four pseudonyms and their UUIDs, which any server they join already sees. Low
sensitivity, and untracking the two JSON files alone would achieve nothing while the same names sit in
the compose file. It is a disclosure decision rather than a leak.

## Infrastructure detail, which is deliberate

The hostname, the IPv6 address, the published ports, the container layout, the firewall rules and the
backup design are all documented and would all become public. **That is the stated intent**, since
`TODO.md` gives "No security by obscurity" as the guideline for this exercise, and a defence that only
works while undescribed is not a defence.

Two things were worth checking against that guideline rather than assuming, and both are fine. No
credential is committed anywhere, confirmed by `gitleaks` over tree and history in all three
repositories. And the identifiers that do appear are useless without access: Vaultwarden item UUIDs
name items inside a vault, and the Google Shared Drive ID names a drive that still requires
authentication.

## What changes at the flip, which is not only who can read

Everything above is about content. Two things about a public repository are about behaviour instead,
and both were checked for `sdwa5-3d` on 2026-09-14.

**Actions become triggerable by strangers, and here they are not.** A public repository lets anyone
open a pull request, and a workflow carrying a `pull_request` trigger then executes a fork's code.
`sdwa5-3d`'s `tests.yml` triggers on `push` and `workflow_dispatch` only, so a fork's pull request runs
nothing at all, and the 330-minute `full` job carries `if: github.event_name != 'push'` on top of that.
No step in the file reads `secrets`, so there is nothing for a workflow to hand out either. Since
2026-09-14 it also declares `permissions: contents: read` rather than inheriting whatever the
organization default happens to be, because a default is not a statement.

**Every commit message used to carry an authorship trailer, and they are gone.**

**DECIDED 2026-09-15, and this reverses a decision taken the same day.** The first answer was to keep
them, on the reasoning that the attribution was the honest record of how the work was made and that a
fifth rewrite across three repositories was not worth it. The owner decided otherwise, and the deciding
argument is ordering rather than sensitivity: a trailer is permanent in every public clone the moment a
repository is published, so it is cheap to remove now and impossible to remove later.

What it amounted to, measured before removal on 2026-09-15. Of the three repositories' 376 commits,
**225 carried an attribution line and 211 carried a session link**, naming 31 distinct sittings. Only
two wordings ever occurred, and **no attribution line ever named a human**, so removing them took a
credit from nobody. The session links were opaque in any case, since fetching one without a session
cookie answers HTTP 403.

Removed from the working trees and from every commit message on 2026-09-15, in the same pass that
carried the other findings of that day's audit, and the setting that produced them is switched off for
this project so nothing new arrives. That setting is deliberately **not** committed: its whole job is
to hide the attribution, so a tracked copy of it would disclose exactly what the rewrite removed.

**How the pass was run and what proves it.** One `git-filter-repo` run per repository, over commit
messages and file contents together. The trailers came out through a message callback rather than a
text replacement, because a replacement only empties the text and leaves the blank line behind; the
callback drops whole lines and then trims what they leave. It is scoped to Claude and Anthropic on
purpose, so that an attribution line naming a **human** would survive. Measured beforehand: there was
none.

| Repository | Commits before and after | Tree at `HEAD` before and after |
|---|---:|---|
| `sdwa5` | 71 | `d95e57c5` |
| `sdwa5-3d` | 166 | `c586aec3` |
| `sdwa5-vps` | 147 | `2f562d25` |

Equal commit counts and an unchanged tree hash together say that only commit objects changed. The
working trees had been corrected by ordinary commits first, precisely so that this invariant could
hold while content was still being removed from the history.

All three were **republished rather than force-pushed**, by renaming the repository, creating it
empty, pushing, confirming the tip and then deleting the old one, which is what leaves no pre-rewrite
objects in GitHub's cache. Verified afterwards in all three: every probe term returns zero over every
blob and every commit message, the two removed paths appear in no commit at all, a pre-rewrite SHA
answers `not our ref`, and a control fetch of `main` succeeds. `sdwa5-vps`'s own suite is 184 tests
green with shellcheck clean, and this repository's link check reports no errors.

## What the 2026-09-15 audit found in the other two repositories

`sdwa5-3d` was audited in depth on 2026-09-14. The same four passes were run over this repository and
over `sdwa5-vps` on 2026-09-15: credentials three ways, the redaction patterns against the pre-rewrite
backups as a control, a pattern-free sweep for personal and infrastructure data, and the mechanics of
publication.

**A correction to the method first, because it invalidates an earlier claim.** The runs described as
"without the allowlist" were not. `gitleaks` reads a `.gitleaks.toml` found in the scan target even
when `--config` is not given, and the `git archive` export carried one. Every such run was repeated
with an explicitly empty configuration. That is also what turned the `sdwa5-vps` result from clean to
not clean.

**Credentials.** This repository and `sdwa5-3d` are clean in tree and history, with the repository
configuration, with the default rules, and with no allowlist at all. `sdwa5-vps` yields twelve findings
once its allowlist is off. Ten are the `SwagPlatformSecurity` hash manifest and are digests rather than
secrets. **Two are real**, both in `minecraft-data/server.properties` in the commit that imported the
Minecraft data directory. Both are machine-generated, both were rotated on 2026-09-08, and one of them
is regenerated on every container start, so they were dead before they were found. They are removed
from that repository's history rather than left to be published. A pattern-free sweep over every blob
in both repositories found no key material, no cloud token, no JWT, no IBAN and no telephone number.

**The redaction of 2026-09-13 held here and did not hold in `sdwa5-vps`.** Against the pre-rewrite
backup this repository's patterns hit seventeen times and hit zero times today. `sdwa5-vps` hit ten
times in the backup and **still hit three times today**, because names came back into that repository
after the rewrite rather than surviving it.

**That is the finding of the day.** The ERP address rollout added on 2026-09-14 pinned three ERP record
ids to the surnames those ids must carry, as a guard against writing to the wrong record, and its tests
carried the same names as fixtures. Alongside it the changelog retold the ERP member list, naming five
further people, three of them deactivated former members and one an external third party, together with
that third party's own postal address. None of the six holds an office and nothing on this page ever
covered them. All are out of the working tree in `sdwa5-vps` 1.39.0, the record list moved to a
gitignored file beside the script, and the names are out of the history in the same pass.

**A scanner blind spot of the opposite shape.** `sdwa5-3d` allowlisted a path that contained tracked
files. `sdwa5-vps` allowlisted a path whose files are tracked on purpose, which stopped gitleaks reading
them at all. Both are the same mistake seen from two sides, and the second is now scoped to the rule
instead of to the path. Measured with a planted key: eleven findings with no allowlist, one with the
new one, which is the planted key.

**Four things were decided rather than fixed**, all on 2026-09-15.

* **The Vaultwarden posture in [`services.md`](services.md) is down to one line.** The thinning of
  2026-09-12 removed the per-account figures and left the conclusions, and a reachable host read next
  to a named owner, a count of weaker accounts and a stated single point of failure is a targeting
  statement whatever the figures say.
* **[`google-workspace.md`](google-workspace.md) no longer says which mailbox carries which service
  credential.** One row named an account and, in the same sentence, made it the Shopware SMTP holder,
  the Let's Encrypt contact and the owner of the backup folder. No credential was ever in a repository;
  the sentence was the map to all three.
* **The four defects in the filed statutes and the Rechnungsprüfer conflict are published.** An
  association that names its own defects and fixes them stands better than one where somebody else
  finds them, and the statutes are filed with the authority in any case. The governance conflict is now
  stated by role rather than against a person, because the defect belongs to the association.
* **The two board names stay deferred to the ZVR register, with their roles and dates.** The point of
  deferring was that this repository should not be the publisher, not that the names become unfindable.
  The register is the source and remains it, and the ZVR number is in the shop's Impressum by law.
  Recorded here so the question does not come up a third time.

**What was left alone, deliberately.** The Minecraft pseudonyms and their UUIDs, already decided. The
firewall rules, open ports and SSH key fingerprints in `sdwa5-vps`, which are the stated intent of the
no-obscurity guideline, though two sentences in `ssh-hardening.md` were worth a re-read before the flip,
namely that the deploy key has no passphrase and that a superseded private key is still on disk. Both
were re-read on 2026-09-30. The first stays, because the key is read-only, scoped to one repository and
never leaves the host. The second was stale, since `/root/.ssh/` holds only the two current deploy
keys, and `sdwa5-vps` 1.50.1 corrects it. And
`minecraft-data/`, which fell under neither licence clause and now has one.

## The fourth repository, `sdwa5-dsp`, published on 2026-10-05

The DSP editor was a private repository on a co-author's personal account under the name trackdsp. It moved into
the organization as `SdWa5/dsp`, renamed to `sdwa5-dsp` like its siblings, and it went through the same passes
before anything was pushed.

**Both authors agreed to the move, to MIT, and to how they appear.** The co-author is credited by GitHub handle only.
The co-author's commits carry the noreply address of that account, and the first name came out of the tree and the
history, where it stood in a credit line, in three Windows paths of the legacy tools and in the name of a backup file on the board.

**What the rewrite removed, measured beforehand.** The business address as author or committer in 76 identity
entries, the co-author's two mail addresses in 7, the business development domain as a default URL in three browser
checks, and the authorship trailers and session links in 32 commit messages. One `git-filter-repo` run did it with
a mailmap, a text replacement and the same Claude-scoped message callback as on 2026-09-15. The tree was corrected by
an ordinary release first, so the 215 commits and the tree at `HEAD` are unchanged by the rewrite, and every probe
term returns zero over every blob and every message afterwards.

**gitleaks finds one thing with the allowlist off, and it is meant to be there.** It is the `APP_SECRET` that the
Symfony recipe commits in `.env.dev`. It signs nothing outside a developer's machine, and the board sets its own. It
is allowlisted by path rather than by commit, because the rewrite changed every commit hash.

**Kept on purpose.** The vendor editor screenshots, the menu metadata decoded from the vendor installer, the USB
captures and the configuration dumps are interoperability evidence, the test suite replays the captures, and no
vendor binary was ever committed. The board's network layout in `docs/vim3.md` follows the guideline above. It has
private addresses and the crew network's name, and the network key is not in the repository.

**Two vendor screenshots were redacted before the push.** The Open and Save As dialogs in `tools/shots/` showed the
virtual machine's share path, its folder tree and a folder named after a person. The path and the folder list are
blanked, while the dialog title and the `*.prs` filter that the vendor parity audit cites are kept. Each file had a
single version, and a second `git-filter-repo` pass on 2026-10-05 replaced it everywhere.

**A private venue's network name came out of `docs/vim3.md` and its history in the same pass.** The venue's name
stays where it is a DSP preset inside the USB captures, because the test suite replays them, and without the
network name it is only a venue preset like the others. The release commit carried both corrections first, so this
pass, too, left the commit count and the tree at the tip unchanged.

**The licence is MIT alone, unlike the siblings.** There is no CC BY-SA part, because MIT is what both authors
agreed to. The README names the vendor screenshots, the menu and dialog data read from the vendor software and the
factory configuration as not ours to license, and it says that the project is not affiliated with Thomann.

**The lock dialog stays.** The code in `dlg_TfmLockSetup.png` is the vendor default, which the owner confirmed and
`docs/vendor-parity.md` records. The vendor manual names no default.

**Published on 2026-10-05, private first and public after the checks.** `SdWa5/dsp` was created empty and
private, and only `main` was pushed, 217 commits. While it was private, its `main` matched the local tip, a fresh
clone returned zero for every removed value and a clean gitleaks run, and the first CI run was green on php, js and
secrets, with a log that holds none of the removed values. A fetch by SHA of the old repository's last tip and of
both pre-redaction tips answered `not our ref`, and a control fetch of `main` succeeded. Only then did it go public,
with secret scanning, push protection and private vulnerability reporting switched on like its siblings, and the
`not our ref` answer held for an anonymous fetch afterwards.

**The old repository stays where it is.** It is private, it holds the pre-rewrite history, and only its owner can
archive or delete it. Nothing was transferred from it, so the new repository has no cached pre-rewrite objects.

## The licence, which is a separate decision

No repository has a `LICENSE` file, and the root `README.md` says "No license specified — all rights
reserved unless stated otherwise per sub-repo". Published unchanged, that means a reader may read the
documentation and reuse none of it, not a diagram, not a script, not a spec.

**Decided on 2026-09-12 and applied to all three repositories.** MIT in `LICENSE` for the code and
configuration, CC BY-SA 4.0 in `LICENSE-docs` for the prose, documentation and data, with each
`README.md` naming which directories fall on which side. Two carve-outs are stated rather than left
implied: `sdwa5-vps/shopware-html-data/` is store-installed plugin content under its vendors' own
terms, and any mesh a `sdwa5-3d` spec reaches through `mesh_override` is third-party CAD, deliberately
uncommitted, with its provenance recorded in that repository's `docs/sources.md`.

**The first of those carve-outs was measured on 2026-09-16, and it holds.** The four plugin
directories `sdwa5-vps` carries as source are `FroshLazySizes`, `FroshPlatformFilterSearch`,
`FroshShopmon` and `SwagPlatformSecurity`, 166 files between them, and each one's own
`composer.json` declares **MIT**. Publishing them is therefore permitted rather than merely assumed,
and the carve-out's wording stays as it is because it also has to cover whatever gets vendored next.
The inventory behind this is `sdwa5-vps/docs/shopware/plugins.md`.

The same measurement found five further plugins active on the shop that no repository records. That
is a reproducibility gap and not a disclosure one, so it is tracked in `sdwa5-vps/TODO.md` rather
than on this page.

## What is left to do

The credential scan is done and gated in CI, and the commit identities were rewritten on 2026-09-08.

**The work items are done.** The commit identities were rewritten on 2026-09-08 and the private email
address was rewritten out of `sdwa5-vps`'s file contents on 2026-09-12.

**The move is done too.** On 2026-09-12 the three repositories were pushed into fresh, empty
repositories in the [SdWa5](https://github.com/SdWa5) organization and the personal originals were
deleted, which put GitHub's cache of both rewrites' pre-rewrite commits beyond reach, though not yet
beyond restoring — see the 90-day window above. They are
[docs](https://github.com/SdWa5/docs), [vps](https://github.com/SdWa5/vps) and
[3d](https://github.com/SdWa5/3d). **All three went public on 2026-09-30**, `vps` first, then `3d`
after its identity rewrite and this repository last, each with secret scanning, push protection and
private vulnerability reporting switched on.

**The last check before the flip, 2026-09-30.** Every blob and every commit message of all four private
repositories of the owner was scanned without printing values, and the redaction patterns of the
earlier passes were run again. Nothing matched in the three SdWa5 repositories apart from the four
commits above. The 37 Actions log archives, which become readable with the repository, were scanned the
same way with a positive control and came back clean, helped by `gitleaks` running with `--redact`. The
link to the `SCN-6` routing table in `sdwa5-3d/TODO.md` opens without a login. It stays, because its
owner decided on 2026-09-30 that the sheet may be publicly readable.

**Every decision on this list is made**, on 2026-09-12. The address stays because the Impressum
publishes it by law, and the `c/o <name>` prefix went with it. Two board members' names defer to the
ZVR register and the Obmann's stays, because the Impressum names him. The former board member is gone.
The Vaultwarden posture is thinned to one sentence. The Minecraft pseudonyms stay, being low
sensitivity and all-or-nothing. The licence is MIT plus CC BY-SA 4.0. The third-party gear figures are
cleared by their owners.

**Three more decisions were taken on 2026-09-14 and 2026-09-15, and nothing on this page is open.**
The full name in `sdwa5-3d/TODO.md` stays. PSL's inventory is no longer inferred from what they bring,
in the working trees and in both histories. And the commit-message authorship trailers were removed
from all three repositories, which reversed that day's first answer. All three are written up above,
with their evidence.

**The 2026-09-12 rewrite was checked on 2026-09-13 and did not hold.** What that pass actually achieved
was the file contents of two repositories. What it missed is listed under "Personal data of named
people" above, and the short version is a bare surname, every commit message, and a third repository
nobody scanned. Three further items came out of the same audit and had never been on this list at all:
the private email address in **this** repository's `TODO.md`, a stale claim in `sdwa5-vps` that the VPS
has no firewall, and a legal self-assessment of the live shop that is better kept in Drive.

**Done on 2026-09-13.** All three repositories were rewritten over contents **and** commit messages,
with `--replace-text` and `--replace-message` together, which is the pair the earlier passes did not
use. Each repository kept its commit count and its `HEAD` tree, except `sdwa5-vps`, whose tree changes
because one file is deliberately removed from it. `Mühlenstraße 24` and `Stefan Ripper` are kept,
because the Impressum publishes both by law. **`sepp` is kept as well**, decided on 2026-09-13. It is a
nickname rather than a name, it is an owner key throughout `sdwa5-3d`, and what created the exposure
was the mailbox table mapping it to a board role, which is what came out instead.

**That reasoning covered the bare nickname, and the full name is there too.** `sdwa5-3d/TODO.md` names
the owner of the second van in full, in the working tree and in 78 of that repository's 158 commits,
introduced in 0.72.2 and never in a commit message. It surfaced on 2026-09-14 through a sweep for
common given names rather than through the redaction patterns, which had no reason to carry it. **Kept,
decided on 2026-09-14 on the same ground**, namely that it reads as a nickname. Taking it out would
have cost a fourth rewrite over 78 commits.

**The 2026-09-13 rewrite was verified against the pre-rewrite backup on 2026-09-14.** All 22
replacement patterns were run over the full history of both the backup and the current repository,
file contents and commit messages together. The backup answers with 8 patterns matching, one of them
25 times, which is what proves the test itself works. `sdwa5-3d` as it stands answers with zero in
contents and zero in messages, across all 158 commits.

**One lesson is worth keeping, because it caught this list twice.** A note that documents a redaction
tends to quote the thing it redacted, and neither a tree scan of the current checkout nor `gitleaks`
will ever see it. The check that does is a grep for the removed value across every commit **and** every
commit message, in every repository at once rather than one at a time.

**A second lesson, from 2026-09-14. An allowlist can exempt tracked files while its own comment says it
does not.** `sdwa5-3d/.gitleaks.toml` skipped `^\.ddev/` on the stated ground that nothing under that
path is committed, and four files under it are. Every scan of that repository, in the working tree and
over the history alike, had been skipping them since the file was written. They turned out to be clean,
which is luck rather than a result. So a scanner's own configuration is part of what has to be read,
and the cheap check is to run it once with the allowlist off and compare the two answers.
