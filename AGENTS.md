# AGENTS.md

Generated AWS clients from NSmithy; see `README.md` for commands.

- Never hand-edit `services/*/Generated/` or the service `.csproj` files. Fix
  the generator in smithy-dotnet, or `scripts/nsaws.py`, and regenerate.
- When a sweep finds a generator bug, reduce it to a minimal model and add it
  as a regression test in smithy-dotnet, not here.
- Generic Smithy features (endpoint rules, waiters) belong in NSmithy. Only
  AWS service customizations belong in this repo.
- `reports/` is overwritten by `just sweep`; commit it when it changes.
- `generate` and `sweep` share `.sweep/work/`; do not run them concurrently.
