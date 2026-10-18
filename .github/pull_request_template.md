## What

<!-- What does this PR change? One or two sentences. -->

## Why

<!-- Why is this change needed? -->

## Type of change

- [ ] Feature
- [ ] Bug fix
- [ ] Refactor (no behaviour change)
- [ ] Tests only
- [ ] Docs / configuration

## Checklist

- [ ] Targets `main` from a short-lived branch
- [ ] Commits show the TDD cycle: failing test → minimal code → refactor
- [ ] `pre-commit run --all-files` passes
- [ ] `python -m pytest` passes
- [ ] New code has tests, including failure cases (invalid input, unknown cities, bad keys)
- [ ] Public modules, classes and functions have Google-style docstrings
- [ ] No duplicated logic: shared code lives in a reusable component