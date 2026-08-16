# HR Salary

Python application for salary calculation and related data handling based on CSV exports from `hr_sql_en`.

## Repository structure

```text
hr_salary/
├── src/hr_salary/          # Application source package
│   ├── ui/                 # User-interface code
│   ├── services/           # Salary/business logic
│   ├── models/             # Domain/data models
│   ├── database/           # Database access and persistence
│   ├── reports/            # Reports and exports
│   ├── utils/              # Shared utilities
│   └── resources/          # Application resources
├── tests/
│   ├── unit/               # Unit tests
│   ├── integration/        # Integration tests
│   └── regression/         # Regression tests
├── docs/                   # Project and user documentation
├── scripts/                # Developer/maintenance scripts
├── installer/              # Installation-related files
├── data/                   # Local/sample data; production/private data is not committed
├── .github/workflows/      # Reserved for workflows; no Actions workflow enabled by default
├── pyproject.toml
└── README.md
```

## Development rule

`main` is the stable branch. New work should be developed on feature/fix branches and merged only after local verification. GitHub Actions are not required by default.

See `docs/development_rules.md` for the repository rules.
