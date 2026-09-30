1. improve docs [docs](docs)
    1. keep docs split by topic — one service/topic per file (like docs/shopware/); split future files if they grow too
       big
2. [sdwa5-vps/TODO.md](sdwa5-vps/TODO.md)
3. [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
4. Cleanup and refresh Google Drive together with this repo and all sub repos
    1. the account's My Drive root holds **four files all named `AmpLimiterCalc.csv`**, re-measured 2026-09-08 with
       three distinct sizes, 7700, 7718 and 7432 bytes with the last appearing twice at the same timestamp. So they
       are **hand-kept versions rather than redundant copies**, and only one pair is a true duplicate. Reconciling
       them is a reading job rather than a delete. `Audio Routing.xlsx` sits there too rather than in the shared
       drive, which is why the `SdWa5:` rclone remote cannot see it without a `--drive-team-drive ""` override.
       Deleting or renaming anything needs a write scope, since that remote is `scope = drive.readonly`. See `SIG-1`
       in [sdwa5-3d/TODO.md](sdwa5-3d/TODO.md)
