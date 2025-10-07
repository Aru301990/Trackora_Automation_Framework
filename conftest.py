import pytest
import yaml
import os
import glob
import time
import webbrowser
import logging
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# If using webdriver-manager, uncomment the next two lines:
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from pathlib import Path
from urllib.parse import urlparse

# Import page objects and helpers to use in fixtures and hooks
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.revenue_panel_page import RevenuePanelPage
from pages.employee_page import EmployeePage
from pages.department_page import DepartmentPage
from pages.timesheet_page import TimesheetPage
from pages.project_page import ProjectPage
from utils.helpers import TestHelpers

# ---------------- Logging Setup ----------------
# Set up the root logger for pytest; log messages go to console, HTML, and captured log.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

# ---------------- Global Vars ----------------
# Maximum number of HTML reports to keep; older ones are deleted.
MAX_REPORTS = 49
_latest_report_path = None  # Stores path to latest HTML report for viewing/open
_auto_open_report = False   # Controls auto-opening of HTML report after tests

# ---------------- Configuration Fixtures ----------------

@pytest.fixture(scope="session")
def config():
    """
    Loads YAML configuration for the framework from config/config.yaml.
    Provides access to browser, base_url, waits, etc. for all tests.
    """
    config_path = Path(__file__).parent / "config" / "config.yaml"
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="session")
def test_data():
    """
    Loads test data and credentials from data/testdata.json.
    Returns dict for test parametrization and user login.
    """
    return TestHelpers.load_test_data()

# ---------------- Browser Setup Fixtures ----------------

@pytest.fixture
def setup(config, logger):
    """
    Responsible for browser initialization and cleanup for each test:
      - Loads settings from config.yaml
      - Starts Chrome or Firefox, with incognito/private based on clear_cache
      - Navigates to base_url and waits for page to load
      - Yields driver instance for the test
    On teardown, closes the browser.
    """
    browser = config["browser"].lower()
    base_url = config["base_url"]
    implicit_wait = config.get("implicit_wait", 10)
    clear_cache = config.get("clear_cache", True)

    # --- Browser selection ---
    if browser == "chrome":
        chrome_options = ChromeOptions()

        # Disable data breach warnings for passwords
        chrome_options.add_argument("--disable-features=PasswordManager,CredentialsEnableService,PasswordStore")

        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--allow-insecure-localhost")
        chrome_options.add_argument("--ignore-ssl-errors")
        
        base_url = config["base_url"]
        parsed_url = urlparse(base_url)
        origin = f"{parsed_url.scheme}://{parsed_url.netloc}"

        chrome_options.add_argument(f"--unsafely-treat-insecure-origin-as-secure={origin}")

        # Disable Chrome password manager popups and infobars
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            # "profile.default_content_setting_values.notifications": 2  # Optional: block notifications
        }
        chrome_options.add_experimental_option("prefs", prefs)

        if clear_cache:
            chrome_options.add_argument("--incognito")
            logger.info("Launching Chrome in incognito mode (clear_cache=true).")
        else:
            logger.info("Launching Chrome in normal mode (clear_cache=false).")
        # By default, uses system chromedriver. Uncomment for webdriver-manager usage.
        driver = webdriver.Chrome(
            service=Service(),
            options=chrome_options
        )
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        if clear_cache:
            firefox_options.add_argument("--private")
            logger.info("Launching Firefox in private mode (clear_cache=true).")
        else:
            logger.info("Launching Firefox in normal mode (clear_cache=false).")
        driver = webdriver.Firefox(
            service=Service(),
            options=firefox_options
        )
    else:
        raise ValueError(f"Browser {browser} not supported")

    # --- Driver common setup ---
    driver.maximize_window()
    driver.implicitly_wait(implicit_wait)
    driver.get(base_url)
    logger.info(f"Navigated to {base_url}")
    TestHelpers.wait_for_page_load(driver)

    yield driver  # Pass browser instance to the test

    # Cleanup after test
    driver.quit()

@pytest.fixture
def logger(request):
    """
    Provides a test-scoped logger for each test function.
    Log messages are captured in pytest logs and attached to the HTML report.
    """
    return logging.getLogger(request.node.name)

# ---------------- Login Fixtures ----------------

@pytest.fixture
def login_page(setup):
    """
    Provides an instance of the LoginPage object for login operations.
    """
    return LoginPage(setup)

@pytest.fixture
def admin_login(setup, login_page, logger):
    """
    Logs in using admin user credentials before starting a test.
    Returns driver and DashboardPage object for further actions.
    """
    credentials = login_page.login_as_user_type("admin")
    logger.info(f"Logged in as admin: {credentials['username']}")
    base_page = BasePage(setup)  # Use the BasePage with your driver
    alert_text = base_page.handle_login_popup_alert(timeout=5)
    if alert_text:
        logger.info(f"Login popup alert dismissed with text: {alert_text}")
    return setup, DashboardPage(setup)

@pytest.fixture
def manager_login(setup, login_page, logger):
    """
    Logs in using manager user credentials before starting a test.
    Returns driver and DashboardPage object for further actions.
    """
    credentials = login_page.login_as_user_type("manager")
    logger.info(f"Logged in as manager: {credentials['username']}")
    base_page = BasePage(setup)  # Use the BasePage with your driver
    alert_text = base_page.handle_login_popup_alert(timeout=5)
    if alert_text:
        logger.info(f"Login popup alert dismissed with text: {alert_text}")
    return setup, DashboardPage(setup)

@pytest.fixture
def employee_login(setup, login_page, logger):
    """
    Logs in using employee user credentials before starting a test.
    Returns driver and DashboardPage object for further actions.
    """
    credentials = login_page.login_as_user_type("employee")
    logger.info(f"Logged in as employee: {credentials['username']}")
    base_page = BasePage(setup)  # Use the BasePage with your driver
    alert_text = base_page.handle_login_popup_alert(timeout=5)
    if alert_text:
        logger.info(f"Login popup alert dismissed with text: {alert_text}")
    return setup, DashboardPage(setup)

# ---------------- Page Object Fixtures ----------------

@pytest.fixture
def dashboard_page(setup):
    """
    Provides an instance of DashboardPage object based on initialized driver.
    """
    return DashboardPage(setup)

@pytest.fixture
def revenue_panel_page(setup):
    """
    Provides an instance of RevenuePanelPage object based on initialized driver.
    """
    return RevenuePanelPage(setup)

@pytest.fixture
def employee_page(setup):
    """
    Provides an instance of EmployeePage object based on initialized driver.
    """
    return EmployeePage(setup)

@pytest.fixture
def department_page(setup):
    """
    Provides an instance of DepartmentPage object based on initialized driver.
    """
    return DepartmentPage(setup)

@pytest.fixture
def timesheet_page(setup):
    """
    Provides an instance of TimesheetPage object based on initialized driver.
    """
    return TimesheetPage(setup)

@pytest.fixture
def project_page(setup):
    """
    Provides an instance of ProjectPage object based on initialized driver.
    """
    return ProjectPage(setup)

# ---------------- Data Fixtures ----------------

@pytest.fixture
def admin_credentials(test_data):
    """
    Fetches admin credentials from loaded test_data fixture.
    """
    return test_data["users"]["admin"]

@pytest.fixture
def manager_credentials(test_data):
    """
    Fetches manager credentials from loaded test_data fixture.
    """
    return test_data["users"]["manager"]

@pytest.fixture
def employee_credentials(test_data):
    """
    Fetches employee credentials from loaded test_data fixture.
    """
    return test_data["users"]["employee"]

@pytest.fixture
def department_test_data(test_data):
    """
    Fetches department-related test data for test setup.
    """
    return test_data["test_data"]["departments"]

@pytest.fixture
def employee_test_data(test_data):
    """
    Fetches employee-related test data for test setup.
    """
    return test_data["test_data"]["employees"]

@pytest.fixture
def project_test_data(test_data):
    """
    Fetches project-related test data for test setup.
    """
    return test_data["test_data"]["projects"]

# ---------------- Utility Fixtures ----------------

@pytest.fixture
def unique_name():
    """
    Provides access to the unique name generator for test data (returns function).
    """
    from utils.helpers import DataHelpers
    return DataHelpers.generate_unique_name

@pytest.fixture
def unique_email():
    """
    Provides access to the unique email generator for test data (returns function).
    """
    from utils.helpers import DataHelpers
    return DataHelpers.generate_unique_email

# ---------------- Pytest Hooks ----------------

def pytest_addoption(parser):
    """
    Registers custom CLI option (--auto-open-report) and INI option (auto_open_report)
    for controlling automatic opening of HTML report after tests.
    """
    parser.addoption(
        "--auto-open-report",
        action="store_true",
        default=False,
        help="Automatically open the HTML report in a browser after test run",
    )
    parser.addini(
        "auto_open_report",
        help="Enable/Disable auto open report (true/false)",
        default="false",
    )

def pytest_configure(config):
    """
    Pytest hook called to configure the test run before tests start:
      - Creates reports/ directory
      - Determines whether to auto-open the report based on CLI or ini
      - Sets up HTML report filename and location
      - Cleans up old report files based on MAX_REPORTS
    """
    global _auto_open_report, _latest_report_path

    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    # CLI flag overrides pytest.ini
    if config.getoption("--auto-open-report"):
        _auto_open_report = True
    else:
        auto_open_setting = config.getini("auto_open_report")
        _auto_open_report = (auto_open_setting.lower() == "true")

    # --- Report file setup ---
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_file = os.path.join(reports_dir, f"report_{timestamp}.html")
    config.option.htmlpath = report_file
    config.option.self_contained_html = True

    # Remove older reports if above threshold
    cleanup_old_reports(reports_dir)
    _latest_report_path = report_file

def pytest_sessionfinish(session, exitstatus):
    """
    Pytest hook after session completes:
      - Prints the location of HTML report
      - Opens it in default browser if auto-open is enabled
    """
    global _latest_report_path, _auto_open_report

    if _latest_report_path and os.path.exists(_latest_report_path):
        print(f"\nTest Report Generated: {_latest_report_path}\n")
        if _auto_open_report:
            try:
                time.sleep(1)
                webbrowser.open(f"file://{_latest_report_path}")
                print("Auto-opened test report in default browser.")
            except Exception as e:
                print(f"Failed to auto-open report: {e}")
        else:
            print("Auto-open disabled (controlled by pytest.ini / CLI).")
    else:
        print("Report file not found after test run.")

def cleanup_old_reports(reports_dir):
    """
    Deletes oldest HTML reports so that only MAX_REPORTS are retained.
    Prevents disk bloat and keeps report directory clean.
    """
    report_files = sorted(
        glob.glob(os.path.join(reports_dir, "report_*.html")),
        key=os.path.getctime,
    )
    logging.info(f"Found {len(report_files)} report files to evaluate for cleanup in {reports_dir}")

    while len(report_files) > MAX_REPORTS:
        oldest = report_files.pop(0)
        try:
            os.remove(oldest)
            logging.info(f"Deleted old report: {oldest}")
        except Exception as e:
            logging.error(f"Error deleting {oldest}: {e}")

def pytest_metadata(metadata):
    """
    Adds custom project, environment, and run metadata to the pytest-html report.
    Pulls data from config.yaml if available.
    """
    try:
        cfg_path = Path(__file__).parent / "config" / "config.yaml"
        with open(cfg_path, "r") as f:
            cfg = yaml.safe_load(f)
    except Exception:
        cfg = {}

    # Inject custom metadata from YAML config
    metadata["Project"] = "Trackora Automation Framework"
    metadata["Application"] = "Trackora"
    metadata["Environment"] = cfg.get("env", "Unknown")
    metadata["Browser"] = cfg.get("browser", "Chrome")
    metadata["Base URL"] = cfg.get("base_url", "https://example.com")
    metadata["Clear Cache"] = str(cfg.get("clear_cache", False))
    metadata["Start Time"] = time.strftime("%Y-%m-%d %H:%M:%S")

    # Add OS username for traceability
    metadata["Executed By"] = os.getenv("USERNAME") or os.getenv("USER") or "Unknown"
    return metadata

# ---------------- Screenshot on Failure ----------------

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook called after each test phase (setup/call/teardown):
      - If the test fails, capture screenshot (if browser available)
      - Attach screenshot to HTML report for easy debugging
      - Log screenshot path using the logger fixture
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup", None)
        test_logger = item.funcargs.get("logger", logging.getLogger(item.name))

        if driver:
            # Prepare screenshots directory
            screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Save screenshot with test name + timestamp
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            destination = os.path.join(screenshots_dir, file_name)

            try:
                driver.save_screenshot(destination)
                test_logger.error(f"Screenshot saved to: {destination}")
                if hasattr(report, "extra"):
                    report.extra.append(extras.png(destination, name="Failure Screenshot"))
                else:
                    report.extras = [extras.png(destination, name="Failure Screenshot")]
            except Exception as e:
                test_logger.error(f"Failed to capture screenshot: {e}")

# ---------------- Test Collection Ordering Hook ----------------

def pytest_collection_modifyitems(items):
    """
    Pytest hook to reorder collected test items to enforce a specific module execution order.
    Modules listed earlier in 'module_order' will have their tests run first,
    overriding the default alphabetical or discovery ordering.
    Test functions within each module still respect their individual @pytest.mark.order decorators.
    """
    module_order = [
        "admin_login",
        "admin_dashboard",
        "admin_revenue_panel",
    ]

    def get_module_order(item):
        mod_name = item.module.__name__.split('.')[-1]
        try:
            return module_order.index(mod_name)
        except ValueError:
            return len(module_order)
    
    items.sort(key=get_module_order)

# ---------------- HTML Report Customization ----------------

def pytest_html_report_title(report):
    """
    Sets a custom title for the HTML test report for branding and clarity.
    """
    report.title = "Trackora Selenium Pytest Test Report"

def pytest_html_results_summary(prefix, summary, postfix):
    """
    Adds a framework information footer to the HTML report for traceability.
    """
    prefix.extend([
        f"Framework: Trackora Selenium-Pytest | Generated at {time.strftime('%Y-%m-%d %H:%M:%S')}"
    ])
