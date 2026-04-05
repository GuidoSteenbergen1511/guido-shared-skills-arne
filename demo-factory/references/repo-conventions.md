# Repo Conventions

## Purpose
Detect and respect existing naming and structure patterns in the repo before creating new demo folders.

## Rules
- If `Demo_XX_*` exists, use that pattern for new demos.
- Do not introduce `01_Quick_Wins/` unless it already exists or is explicitly requested.
- Keep numbering consistent and do not reuse demo numbers.

## Detection Steps
1. List directories under `Demo_Package/`.
2. If any folder matches `Demo_\d+_`, treat that as the canonical pattern.
3. If no pattern exists, default to `Demo_XX_*`.
