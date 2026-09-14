1. improve docs [docs](docs)
    1. keep docs split by topic — one service/topic per file (like docs/shopware/); split future files if they grow too
       big
2. go public with all sdwa5 repos
    1. github account/org plan (DECIDED)
        1. create GitHub Organization `sdwa5` + admin account on @sdwa5.org (domain already wired to google workspace)
            1. use role address (e.g. git@sdwa5.org)
            2. apply for GitHub non-profit discount
        2. then: transfer all three sdwa5 repos into the org
            1. Scan content for sensitive stuff (guideline: No security by obscurity) and decide transfer method.
               **Secret scanning is done and automated** — see the `secrets` job in
               [.github/workflows/docs.yml](.github/workflows/docs.yml), run over the working tree and the full history
               of all three repos on 2026-09-08 with gitleaks 8.30.1. This repo and `sdwa5-3d` came back with zero
               findings in tree and history. `sdwa5-vps` had two real ones in `minecraft-data/server.properties`, both
               rotated, and ten false positives from a Shopware plugin's hash manifest, allowlisted by path.
               **The judgement half is written up in [docs/going-public.md](docs/going-public.md)**, item by item with
               its evidence and a recommendation. **The identity half is done**: all three histories were rewritten on
               2026-09-08, so every commit in every repository now carries one identity. **That rewrite touched author
               and committer fields and not file contents, which is a distinction 0.7.0 stated too broadly.** Measured
               on 2026-09-12, the private address is still in **74 of `sdwa5-vps`'s 113 commits**, in `README.md`,
               `monitoring/lib.sh`, `.env.example`, `docs/monitoring.md` and `docs/infrastructure.md`. The tree is
               clean and `gitleaks` does not catch it, because an email is not a credential. **That second rewrite is
               done, in `sdwa5-vps` 1.30.0 on 2026-09-12**, with the tree hash unchanged at `c887c215`, 113 commits
               before and after and zero commits on `origin/main` still holding it. What is left of it belongs to
               GitHub rather than to git, namely that the repositories are published by a fresh push into the new
               organization rather than by a transfer, which is what clears the force-pushed commits from GitHub's
               cache. See the step below.
               Everything else is a decision rather than a defect, namely a private residential address and a former board member's
               name in `docs/organization.md`, the per-account Vaultwarden posture in `docs/services.md` read next to
               those names, and four Minecraft pseudonyms. **The other crew's gear figures in
               `sdwa5-3d/docs/sources.md` are decided and cleared**, by their owners and against the content, which is
               60 quoted strings holding nothing but dimensions, cabinet names and datasheet phrases
            2. **DONE on 2026-09-12.** The organization exists as [SdWa5](https://github.com/SdWa5), belonging to the
               Verein rather than to a personal account, with `mail@sdwa5.org` as its contact. All three repositories
               were **created empty and pushed into**, never transferred, because a transfer moves the same object
               store and would have carried both history rewrites' pre-rewrite commits across. The three personal
               repositories were deleted afterwards, which is what removed that cache. Verified: each new repository's
               `main` matches its local `HEAD`, and zero commits on `SdWa5/vps` hold the private address.
               [docs](https://github.com/SdWa5/docs), [vps](https://github.com/SdWa5/vps) and
               [3d](https://github.com/SdWa5/3d), all still private
        3. **DONE on 2026-09-12.** MIT in `LICENSE` for code and configuration, CC BY-SA 4.0 in `LICENSE-docs` for
           prose, documentation and data, in all three repositories, with each `README.md` naming which directories
           fall on which side. Two carve-outs are stated rather than left implied: `sdwa5-vps/shopware-html-data/` is
           store-installed plugin content under its vendors' terms, and any mesh a `sdwa5-3d` spec reaches through
           `mesh_override` is third-party CAD, deliberately uncommitted
        4. **DONE on 2026-09-13, on the second attempt.** The 2026-09-12 rewrite took the names out of the file
           contents of `docs` and `vps` and stopped there. An audit on 2026-09-13 found a bare surname that the
           full-name rules never matched, sitting in 40 of `docs`'s 45 commits and in the working tree; every
           commit **message**, which `--replace-text` does not reach and `--replace-message` does; and a deputy's
           full name as a test fixture in 153 of `3d`'s 154 commits, in the repository the earlier pass had
           declared clean without scanning it. The same audit found the private email address in **this**
           repository's `TODO.md` history, which no rewrite had ever been scoped to. All three repositories were
           rewritten again over contents and messages together. See
           [docs/going-public.md](docs/going-public.md)
    2. configure repos as public
        1. **`sdwa5-3d` was audited for publication on 2026-09-14 and one decision is open.** Three passes over
           the working tree, all 10 648 blobs in the history and all 158 commit messages. No credential anywhere,
           by `gitleaks` with the repo config, with the default rules and with no allowlist at all. No street
           address, postcode, phone number, IP address, IBAN or key material. The 2026-09-13 redaction was
           verified against the pre-rewrite backup, 8 of 22 patterns matching there and 0 here. Four things came
           out of it and three are fixed in `sdwa5-3d` 0.117.0, namely a `gitleaks` allowlist that exempted four
           tracked files, three links to the deleted personal account, and an inference about what PSL own. The
           full name in that repo's `TODO.md` is decided and stays. **Two things are open and both have to be
           settled before the flip rather than by it, and one of the two is done.** The two PSL statements that
           0.117.0 and 0.117.1 removed from the working tree also stood in 28 of its commits, and **the history
           of both repositories was rewritten on 2026-09-15**, with the commit counts and the `HEAD` trees
           unchanged and both repositories republished rather than force-pushed. **What is still open is the
           authorship trailers in 119 of its commit messages**, which go public with the repository and cannot
           be taken back afterwards. See [docs/going-public.md](docs/going-public.md)
        2. **the billing block is gone and CI executes again, measured 2026-09-14.** This item used to say that
           every run in all three repos failed within 2 to 4 seconds with "The job was not started because recent
           account payments have failed or your spending limit needs to be increased", measured 2026-09-08, and
           that no job had ever executed. That no longer holds. Runs complete in all three repositories from
           2026-09-13 onwards, so the pipelines are verified on GitHub for the first time. What going public still
           buys is the metering itself, because all three repos are **private** and a public repository gets
           Actions minutes free and unlimited, plus a four-core runner where a private one has two
        2. the consumption is measured and it is `sdwa5-3d` that spends it. One **push** costs about 2 h 15 m, which is
           the `phpunit` job alone on a runner against 23 minutes locally, and `static` now adds to that. One
           **nightly** costs about 548 minutes, because `full` runs 6 h 1 m and is then killed at GitHub's 6-hour job
           ceiling. Three consecutive nightlies were cancelled that way, 5 to 7 September, so roughly 1 644 minutes
           bought nothing. Filed for that repo as well. **The first executed push confirms the figure and the core
           count is why**: on run `34759228276`, 2026-09-13, `phpunit` was cancelled at its own 90-minute timeout
           after 90 m 16 s, on a commit that already carried the parallel `ShippedScenesTest` and the JIT. See
           `TOOL-20` in [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
        3. until they are public, the cross-repo half of the link check cannot run in CI. `sdwa5-vps` and `sdwa5-3d` are
           gitignored sibling directories rather than submodules, so CI clones them separately, and a private clone
           needs a `SIBLING_REPOS_TOKEN` secret with read access. Without it the job stays green and warns that those
           links were skipped rather than checked. Making the repos public removes the need for the token entirely
3. [sdwa5-vps/TODO.md](sdwa5-vps/TODO.md)
4. [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
5. Cleanup and refresh Google Drive together with this repo and all sub repos
    1. the account's My Drive root holds **four files all named `AmpLimiterCalc.csv`**, re-measured 2026-09-08 with
       three distinct sizes, 7700, 7718 and 7432 bytes with the last appearing twice at the same timestamp. So they
       are **hand-kept versions rather than redundant copies**, and only one pair is a true duplicate. Reconciling
       them is a reading job rather than a delete. `Audio Routing.xlsx` sits there too rather than in the shared
       drive, which is why the `SdWa5:` rclone remote cannot see it without a `--drive-team-drive ""` override.
       Deleting or renaming anything needs a write scope, since that remote is `scope = drive.readonly`. See `SIG-1`
       in [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
