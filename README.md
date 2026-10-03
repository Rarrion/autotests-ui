# UI Course Automation Tests

This project implements automated UI tests for
the [UI Course Test Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login). The
tests are written using **Python**, **Pytest**, **Playwright** and **Allure**. The test application's source code is
available on [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course).

## Project Overview

The goal of this project is to automate the testing of the UI Course application: registration, authorization, the
dashboard and the courses pages. The tests are built on the Page Object, Page Component and Page Factory patterns, so
the test code stays readable and easy to maintain.

Project structure:

- `tests` - test scenarios grouped by application area
- `pages` - Page Objects
- `components` - Page Components (authentication forms, navigation, charts, views and others)
- `elements` - Page Factory elements (button, input, text and others) with Allure steps and UI coverage tracking
- `fixtures` - Pytest fixtures for browsers, pages and Allure
- `tools` - utilities: Allure helpers, logger, routes, Playwright mocks
- `testdata` - files used by the tests
- `config.py` - project settings based on Pydantic Settings

## Getting Started

### Clone the Repository

To get started, clone the project repository using Git:

```bash
git clone https://github.com/Rarrion/autotests-ui.git
cd autotests-ui
```

### Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. Follow the instructions for your operating
system:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

Once the virtual environment is activated, install the project dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

If you're running Playwright for the first time, install the required browsers:

```bash
playwright install
```

### Configure the Project

The project settings are stored in the `.env` file in the project root and are loaded by `config.py`. The default values
are ready to use, change them only if needed:

- `APP_URL` - URL of the application under test
- `HEADLESS` - run browsers in headless mode (`true`) or with a visible window (`false`)
- `BROWSERS` - list of browsers to run the tests in, for example `["chromium","webkit"]`
- `TEST_USER.EMAIL`, `TEST_USER.USERNAME`, `TEST_USER.PASSWORD` - test user data
- `TEST_DATA.IMAGE_PNG_FILE` - path to the image used in the course creation tests
- `UI_COVERAGE_APPS` - applications tracked by the UI coverage tool

## Running the Tests

### Running the Tests with Allure Report Generation

To run the tests and generate Allure results, use the following command:

```bash
pytest -m regression --alluredir=./allure-results
```

To run a part of the test suite, use another marker: `authorization`, `registration`, `dashboard` or `courses`. To run
the tests in parallel, add the `--numprocesses 2` option.

### Viewing the Allure Report

After the tests have been executed, you can generate and view the Allure report with:

```bash
allure serve allure-results
```

This command will open the Allure report in your default web browser.

### UI Coverage Report

The project uses [ui-coverage-tool](https://github.com/Nikita-Filonov/ui-coverage-tool) to measure which elements of
the application are covered by the tests. After a test run, generate the coverage report with:

```bash
ui-coverage-tool save-report
```

Then open the generated `coverage.html` file in your browser.

## CI/CD

The tests run automatically on GitHub Actions on every push and pull request to the `main` branch, the workflow is
described in `.github/workflows/tests.yml`. The Allure report with the run history is published
to [GitHub Pages](https://rarrion.github.io/autotests-ui/), and the UI coverage report is attached to each workflow run
as the `coverage-report` artifact. A GitLab CI configuration is available in `.gitlab-ci.yml`.
