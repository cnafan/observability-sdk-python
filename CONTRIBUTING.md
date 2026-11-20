# Contributing to observability-sdk-python

## Prerequisites

- Python 3.10 or later
- Git

Install the local package in editable mode with `python -m pip install -e .`.

## API and signal-definition changes

- Keep `openan_observability_sdk` as the supported public API surface.
- Keep the A2A, workflow, and agent YAML files in sync with the Java SDK.
- When a signal definition changes, increment the applicable YAML version and update the English and Chinese API references and development guides.
- Treat removal or tightening of a published signal name, attribute, type, requiredness, or metric dimension as a breaking change.
- Do not expose private implementation modules as public API.

## Commits and pull requests

- Use Conventional Commit messages, for example `feat(sdk): add exporter option` or `fix(validation): reject invalid metric dimension`.
- Sign every commit off with DCO: `git commit -s -m "..."`.
- Describe the change, compatibility impact, and verification results in the pull request.
- Do not push commits directly to the upstream repository; submit pull requests from a personal fork.
