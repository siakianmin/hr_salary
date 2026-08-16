# HR Salary Architecture

The application follows a `src/` package layout.

- `src/hr_salary/ui/` — presentation and desktop user-interface components.
- `src/hr_salary/services/` — salary calculation and business rules.
- `src/hr_salary/models/` — domain/data models.
- `src/hr_salary/database/` — persistence, schemas, migrations, and repositories.
- `src/hr_salary/reports/` — report generation and exports.
- `src/hr_salary/utils/` — shared helpers without business ownership.
- `src/hr_salary/resources/` — tracked static resources only.

Business calculations must not be embedded directly in UI code. Database access must remain outside UI widgets. Version identity is defined in `src/hr_salary/version.py` and mirrored in the root `VERSION` file and `CHANGELOG.md`.
