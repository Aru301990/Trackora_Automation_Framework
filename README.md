# Trackora Selenium + Pytest Automation Framework

> **About this framework**  
This project automates the UI testing of the Trackora web application using **Selenium**, **Pytest**, and **pytest-html**.  
All tests use a robust Page Object Model and deliver detailed HTML reports with screenshots, logs, and environment info.  
It supports role-based workflows (Admin, Manager, Employee) and is designed for ease of extension and maintenance.

---

## ✨ Features

- **Multi-user Flows:**  
  Role-based login and workflows for Admin, Manager, Employee.
- **Page Object Model (POM):**  
  All pages are modeled in separate files for clarity and reuse.
- **Config-driven:**  
  Settings, credentials, and environment can be quickly managed in `.yaml` and `.json`.
- **Reporting:**  
  HTML reports (with auto-open option), detailed logs, and screenshots for each failure.
- **Reusable Utilities:**  
  Waits, dropdowns, scrolling, data generation, and locators are centralized for DRY code.
- **Full Coverage:**  
  Tests for Dashboard, Revenue Panel, Employee, Department, Timesheet, and Project modules.
- **Test Prioritization:**
  Supports test case ordering using the `pytest-order` plugin, allowing control of test execution order.

---

## 🧱 Project Structure

> **Below is the actual directory and file layout as seen in VS Code—each item explained.**

```python

trackora_automation_framework/          # Root folder
├── conftest.py             # Pytest configuration, fixtures, and hooks (test setup/teardown, reporting, etc.)
├── dependencies.txt        # Required Python packages for the framework
├── pytest.ini              # Pytest settings, markers, logging, and reporting
├── README.md               # Framework and project documentation


├── config/
│   └── config.yaml         # Central configuration (browser, waits, base URLs, user settings)


├── data/
│   └── testdata.json       # All user credentials and sample test data


├── driver/
│   └── chromedriver-win64/
│       ├── chromedriver.exe               # Chrome WebDriver binary (match version to browser)
│       ├── LICENSE.chromedriver
│       └── THIRD_PARTY_NOTICES.chromedriver
# Add other webdriver executables for other browsers (Firefox, Edge, etc.)


├── pages/
│   ├── base_page.py              # All page objects inherit this common class
│   ├── dashboard_page.py         # Dashboard module interactions
│   ├── department_page.py        # Department management page object
│   ├── employee_page.py          # Employee management object
│   ├── login_page.py             # Login workflow page object
│   ├── project_page.py           # Project management page object
│   ├── revenue_panel_page.py     # Revenue analytics page object
│   ├── timesheet_page.py         # Timesheet management page object
│   ├── __init__.py               # For package compatibility
│   └── modals/                   # All modal/dialog objects for popups
│       ├── add_department_modal.py
│       ├── add_employee_modal.py
│       ├── add_project_modal.py
│       ├── edit_department_modal.py
│       ├── edit_project_modal.py
│       ├── manage_assigned_employees_modal.py
│       └── __init__.py


├── reports/
│   ├── report_<timestamp>.html        # HTML reports for each test session
│   └── screenshots/                   # Screenshots attached on test failure
│       └── test_<test_name>_<timestamp>.png


├── tests/
│   ├── admin_dashboard.py             # Tests for dashboard functionality (admin role)
│   ├── admin_login.py                 # Admin login verification tests
│   ├── admin_revenue_panel.py         # Revenue panel and analytics tests
│   ├── admin_employee.py              # Employee management tests
│   ├── admin_department.py            # Department module tests
│   ├── admin_timesheet.py             # Timesheet admin workflow tests
│   ├── admin_project.py               # Project management tests
│   ├── __init__.py
│   └── __pycache__/                   # Compiled Python bytecode (auto-generated, never edit)


├── utils/
│   ├── helpers.py                     # Shared test helpers (waits, dropdowns, unique data, scrolling)
│   ├── locators.py                    # All selectors, organized by page/module
│   ├── __init__.py
│   └── __pycache__/                   # Python bytecode cache (ignore)


├── .pytest_cache/                     # Pytest internal cache folder for reruns, never manually modify
│   └── ...                           # Contains cache files for pytest state tracking


├── __pycache__/                       # Python bytecode cache (ignore)
│   └── conftest.cpython-313-pytest-8.4.1.pyc


```

---

## 🔧 Setup

> **Step-by-step checklist to get started:**

1. **Pre-requisites:**  
   - Python 3.10 or newer  
   - Chrome or Firefox browser installed, keep the corresponding webdriver in `driver/`  
   - Git (for source control and collaboration)

2. **Install Requirements:**  

```bash

# Clone the repository

git clone <repository-url>
cd trackora_automation_framework

# Install all dependencies

pip install -r dependencies.txt

```

3. **Configure the Framework:**  
- Edit `config/config.yaml` for browser, base URL, and general settings.
- Add user credentials and any required sample data to `data/testdata.json`.
- Ensure `chromedriver.exe` (or other driver) matches browser version and is placed in `driver/`.

---

## 🚀 Usage

> **Run and debug tests with these common commands:**

### Running Tests

```bash
# Run all tests
pytest

# Run specific user type tests
pytest -m admin
pytest -m manager  
pytest -m employee

# Run specific module tests
pytest -m dashboard
pytest -m revenue
pytest -m employees
pytest -m timesheet
pytest -m project

# Run smoke tests
pytest -m smoke

# Run with HTML report auto-open
pytest --auto-open-report

# Run specific test file
pytest tests/test_admin_dashboard.py

# Run a single test case in a file
pytest tests/test_admin_dashboard.py::test_verify_total_business_count
```

> **Marker usage:**  
> Markers (in `pytest.ini`) help you run only specific roles or modules, and manage test scope.

---

## 🏗️ How Tests Are Organized

- **Page objects** reside in `pages/` and use locators from `utils/locators.py`.
- **Modal dialogs/popup forms** are built out in their own files within `pages/modals/`.
- **All tests live in the `tests/` directory**, one file per module or feature (following naming conventions like `admin_dashboard.py`).
- **Helpers (`utils/helpers.py`)** centralize waiting logic, scrolling, dropdown handling, and unique data creation.
- **Test data and credentials** must be added and updated only in `data/testdata.json`.
- **Browser drivers** should always match your browser version and be updated in the `driver/` folder.

---

## 📝 Reporting & Debugging

- Every test session produces an HTML report in the `reports/` folder.
- **Screenshots** of failed tests are saved in `reports/screenshots/` and attached to the HTML report for fast debugging.
- **Live logging**—log output sent both to the console and embedded in reports (configurable via `pytest.ini`).
- **Test environment metadata** (browser, URL, user, etc.) automatically included in each report.
- **Automatic cleanup:** Old reports are auto-deleted after a configurable threshold (see `MAX_REPORTS` in `conftest.py`).

> **Tip:**  
> For troubleshooting, review the screenshots and logs attached to failing scenarios.  
> Always check the report after test runs—it's the fastest way to spot issues and confirm coverage.

---

## 🧪 What’s Covered (Test Scope)

- **Dashboard**: Metrics, year/week views, tab navigation.
- **Revenue Panel**: Filtering, export, pagination, and accurate data display.
- **Employee Management**: CRUD, pagination, modal flows, export, shared resources.
- **Department**: List display, add/edit/delete flows.
- **Timesheet**: Filtering, approval/rejection flows, modal management, import/export.
- **Project**: CRUD for projects, pagination, assignment management.

- **Module - Manager**
- **Manager Employee Management**: pagination, export, Reset, shared resources.

> **Add new test files or modules as your app grows—update README.md every time!**

---

## 🤝 How to Contribute

- **Follow the project structure** shown above—put new pages in `pages/`, new tests in `tests/`, and share utilities in `utils/`.
- **Add new selectors to `locators.py`**.
- **If you create a new module, implement a page object and test file.**
- **Tag your tests** with meaningful markers (as defined in `pytest.ini`) to support focused runs.
- **Document your work**—write docstrings in your page objects and update README with major additions.
- **Run all tests before pushing**—all failures must be captured and explained.

---

## 📌 Essential Notes & Reminders

- Never hard-code credentials: always keep them in `data/testdata.json`.
- Use **explicit waits** and scroll actions (provided in `helpers.py`) for robust UI test execution.
- All screenshots and logs are crucial for debugging in CI/CD pipelines and local runs.
- Auto-generated `.pytest_cache/` and `__pycache__/` folders are for internal use; you do NOT need to manually edit or review their contents.

---

