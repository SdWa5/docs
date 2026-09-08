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
               **What is left is the judgement half a scanner cannot do**: Minecraft player names, member names in
               `docs/`, and the VPS hostname and IPv6 address. None is a credential, so each is a disclosure decision
               rather than a leak
            2. bestcodename/sdwa5-vps (https://github.com/bestcodename/sdwa5-vps/) -> sdwa5/vps
            3. bestcodename/sdwa5 (https://github.com/bestcodename/sdwa5) -> sdwa5/docs
            4. bestcodename/sdwa5-3d (https://github.com/bestcodename/sdwa5-3d/) -> sdwa5/3d — this one was missing from
               the list above and exists on GitHub, so a transfer that covers only the first two leaves it behind
        3. decide a licence, or decide deliberately not to have one. `README.md` currently says "No license specified —
           all rights reserved unless stated otherwise per sub-repo", which means a public reader may read the docs and
           legally reuse nothing from them. For a non-profit publishing its own ops documentation that is probably not
           the intent, and it needs the owner's call rather than a default
    2. configure repos as public
        1. **going public is what unblocks CI, and CI is blocked right now.** Every workflow run in all three repos
           fails within 2 to 4 seconds with "The job was not started because recent account payments have failed or
           your spending limit needs to be increased", measured 2026-09-08. No job has executed, including runs that
           predate this work, so nothing in any of the three pipelines is verified on GitHub. All three repos are
           **private**, so Actions minutes are metered, and **a public repository gets them free and unlimited**.
           Needs a billing action in the account first: check Billing & plans
        2. the consumption is measured and it is `sdwa5-3d` that spends it. One **push** costs about 2 h 15 m, which is
           the `phpunit` job alone on a runner against 23 minutes locally, and `static` now adds to that. One
           **nightly** costs about 548 minutes, because `full` runs 6 h 1 m and is then killed at GitHub's 6-hour job
           ceiling. Three consecutive nightlies were cancelled that way, 5 to 7 September, so roughly 1 644 minutes
           bought nothing. Filed for that repo as well
        3. until they are public, the cross-repo half of the link check cannot run in CI. `sdwa5-vps` and `sdwa5-3d` are
           gitignored sibling directories rather than submodules, so CI clones them separately, and a private clone
           needs a `SIBLING_REPOS_TOKEN` secret with read access. Without it the job stays green and warns that those
           links were skipped rather than checked. Making the repos public removes the need for the token entirely
3. [sdwa5-vps/TODO.md](sdwa5-vps/TODO.md)
4. [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
5. Cleanup and refresh Google Drive together with this repo and all sub repos
    1. the account's My Drive root holds four copies of `AmpLimiterCalc.csv` plus both `Drivers.csv` and `drivers.csv`,
       measured 2026-09-08. `Audio Routing.xlsx` sits there too rather than in the shared drive, which is why the
       `SdWa5:` rclone remote cannot see it without a `--drive-team-drive ""` override. See `SIG-1` in
       [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
