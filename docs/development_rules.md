# HR Salary Development Rules

## Mandatory core rules

1. **Documentation is mandatory.** Every repository must contain a `docs/` folder from the beginning of development. Documentation must be updated with relevant software changes.
2. **Version control is mandatory.** Every accepted software change must have a recorded version impact. The repository must keep `VERSION`, `CHANGELOG.md`, and an application version module.
3. **Semantic versioning.** Use `MAJOR.MINOR.PATCH` version numbers.
   - MAJOR: incompatible architectural or product changes.
   - MINOR: backward-compatible features or significant enhancements.
   - PATCH: bug fixes and small backward-compatible changes.
4. **Stable main branch.** `main` is the stable branch. Feature and bug-fix work should normally be developed on named branches and merged only after local verification.
5. **Python source layout.** Application code lives under `src/hr_salary/` rather than the repository root.
6. **Separation of concerns.** UI, services/business logic, models, database, reports, utilities, and resources remain separated modules.
7. **Tests are separated.** Tests belong under `tests/unit`, `tests/integration`, and `tests/regression` as appropriate.
8. **No secrets or production HR data in Git.** Credentials, personal employee records, salary records, private exports, and runtime databases must not be committed.
9. **Documentation accompanies releases.** User-facing, database, setup, or workflow changes require matching documentation/release notes.
10. **GitHub Actions are optional.** Local verification is allowed and no Actions workflow is required unless specifically approved for the project.

These rules are structural project requirements and are not optional conventions.
