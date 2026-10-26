# SdWa5

## Dolibarr

**Every Dolibarr change ships with its REST API.** A feature, setting or action of an SdWa5 Dolibarr module that a
person can use in the UI also gets an endpoint in the module's `class/api_<module>.class.php`, in the same change,
wherever an API makes sense. A core Dolibarr feature we extend gets its missing endpoint through one of our modules,
and a core endpoint that already covers it is reused. Follow the pattern of
`sdwa5-pmtools/class/api_pmtools.class.php`. **Why:** the goal is a new UI on top of Dolibarr that talks only to the
API, so every UI-only feature is a gap that blocks it (decided 2026-10-26).
