# Kamma Suite UI Regression Tests

This repo contains automated tests for the Kamma Suite web application. The tests run a real browser (Chromium) against the app, click through pages, check that data looks right, and catch visual regressions before they reach users.

Tests are written in Python using [Playwright](https://playwright.dev/python/) for browser automation and [pytest](https://docs.pytest.org/) as the test runner.

---

## What gets tested

- **Authentication** — login flows, session handling, error states
- **Dashboard** — portfolio stats, priority cards, licence needs widget
- **API validation** — checks that what the UI displays matches what the API actually returns
- **Visual snapshots** — screenshot comparisons to catch unexpected layout changes

---

## First-time setup

You need Python 3.9+ installed. Then:

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install the Chromium browser Playwright uses
playwright install chromium

# 4. Set up your credentials (see the Authentication section below)
cp .env.testing .env.testing.local
# Open .env.testing.local and fill in your username and password
```

---

## Authentication

The tests need credentials to log in to the app. These live in environment files that are **not committed to git** (they contain passwords).

Copy the template for whichever environment you want to test against and fill in your details:

```bash
cp .env.testing .env.testing.local   # for the testing environment
cp .env.staging .env.staging.local   # for staging
```

The `.local` files are gitignored. Open the file you created and set:

```
SUITE_USERNAME=your-email@example.com
SUITE_PASSWORD=your-password
KAMMA_APIV3_TOKEN=your-api-token       # needed for API validation tests
KAMMA_PS_API_GROUP_ID=51               # property set group ID
```

**Session caching:** After the first successful login, the browser session (cookies + local storage) is saved to `test_data/auth_state.json`. Subsequent runs reuse this, so you won't need to log in every time. If you get auth errors, delete that file and let the tests log in fresh:

```bash
rm test_data/auth_state.json
```

---

## Running tests

```bash
# Run all tests against the testing environment
pytest --env=testing

# Run against staging instead
pytest --env=staging

# Run only smoke tests (fast, critical-path checks)
pytest -m smoke --env=testing

# Run with a named HTML report saved to reports/
pytest --env=testing --report-name=my_run

# Run with a visible browser window (useful for debugging)
pytest --headed --env=testing

# Update visual snapshot baselines
pytest --update-snapshots --env=testing
```

If you don't pass `--env`, it defaults to `testing`.

---

## Environments

| Name    | URL                                  |
|---------|--------------------------------------|
| testing | https://liam-suite.kammadata.org     |
| staging | https://suite-staging.kammadata.io   |

---

## Test reports

HTML reports are automatically generated after each run and saved to the `reports/` folder with a timestamp. Pass `--report-name` to give the report a meaningful name:

```bash
pytest --env=testing -m smoke --report-name=smoke_before_release
```

Screenshots are captured on test failure. Videos are kept when a test fails. These appear inside the HTML report.

---

## Repo structure

```
kamma-suite-ui-regression/
│
├── tests/                        # All test files live here
│   ├── auth/                     # Login and session tests
│   └── dashboard/                # Dashboard UI, API, and visual tests
│
├── kamma_suite_regression/       # Shared code used by the tests
│   ├── pages/                    # Page Object classes (one per page/component)
│   ├── fixtures/                 # Pytest fixtures for setup (auth, browser contexts)
│   ├── api/helpers/              # Helpers that call the Kamma API directly
│   ├── request_utility/          # Low-level HTTP clients (browser session + token-based)
│   └── generic_utilities/        # General helpers (polling, data comparison, random data)
│
├── test_data/                    # Runtime data (auth_state.json goes here — gitignored)
├── snapshots/                    # Visual regression baseline images
├── reports/                      # Generated HTML reports (gitignored)
│
├── conftest.py                   # Global pytest config, CLI options, report setup
├── pytest.ini                    # Pytest settings (markers, screenshot/video behaviour)
├── requirements.txt              # Python dependencies
├── .env.testing                  # Credential template for the testing environment
└── .env.staging                  # Credential template for staging
```

### Key concepts

**Page Objects** (`kamma_suite_regression/pages/`) — Each page or major component in the app has a corresponding Python class. These classes wrap Playwright selectors and actions so test files stay readable and don't repeat themselves.

**Fixtures** (`kamma_suite_regression/fixtures/`) — Pytest fixtures handle setup and teardown. The `authenticated_page` fixture gives each test a fresh browser tab that's already logged in. The `api_v3` fixture provides a token-based API client for backend calls.

**API helpers** (`kamma_suite_regression/api/helpers/`) — These call the Kamma API directly (not through the browser) to fetch the data that the UI should be showing. Tests use them to verify that what's displayed on screen matches what the API returns.

---

## Test markers

Markers let you run a targeted subset of tests:

| Marker           | What it selects                          |
|------------------|------------------------------------------|
| `smoke`          | Fast, must-pass checks                   |
| `regression`     | Full regression suite                    |
| `visual`         | Screenshot comparison tests              |
| `api_validation` | Tests that cross-check UI against API    |
| `auth`           | Login and session tests                  |
| `dashboard`      | Dashboard page tests                     |

Run a specific marker with `-m`:

```bash
pytest -m visual --env=testing
pytest -m "smoke and dashboard" --env=testing
```

---

## Code style

The project uses [Ruff](https://docs.astral.sh/ruff/) for linting. To check your code before committing:

```bash
ruff check .
```
