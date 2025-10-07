import pytest
import pytest_order
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.admin
@pytest.mark.smoke
class TestAdminLogin:
    """
    Contains test cases to verify Admin login functionality.
    Includes tests for successful login and invalid login scenarios.
    Marked as 'admin' and 'smoke' for selective test runs.
    """

    # @pytest.mark.order(1)
    def test_admin_login_success(self, setup, logger, test_data):
        """
        Tests successful admin login workflow.
        """
        driver = setup  # WebDriver instance from fixture
        login_page = LoginPage(driver)  # Login page object
        admin_credentials = test_data["users"]["admin"]  # Admin user credentials

        logger.info("Starting admin login success test")

        # Check that login page is displayed before proceeding
        assert login_page.is_login_page_loaded(), "Login page should be loaded"

        # Perform the login with valid credentials
        login_page.login(admin_credentials["username"], admin_credentials["password"])

        dashboard_page = DashboardPage(driver)  # Dashboard object for post-login checks

        # Handle any browser alert popup (e.g., welcome message)
        alert_message = dashboard_page.handle_login_popup_alert()
        if alert_message:
            logger.info(f"Login popup alert displayed: {alert_message}")
        else:
            logger.info("No login popup alert displayed.")

        # Verify that dashboard UI loaded successfully after login
        assert dashboard_page.is_dashboard_loaded(), "Dashboard page should load after admin login"

        # Additional assertion example, check URL contains dashboard keyword
        assert "dashboard" in driver.current_url.lower(), "URL should contain 'dashboard' after login"

        logger.info("Admin login test passed")

    # @pytest.mark.order(2)
    def test_admin_login_invalid_credentials(self, setup, logger):
        """
        Tests login failure behavior with invalid credentials.
        """
        driver = setup
        login_page = LoginPage(driver)

        logger.info("Starting admin login invalid credentials test")

        # Confirm login page is loaded prior to submitting invalid login
        assert login_page.is_login_page_loaded(), "Login page should be loaded"

        # Submit invalid credentials intentionally
        login_page.login("invalid_user", "invalid_pass")

        # Assert that error indicator/message is shown on login page
        assert login_page.is_error_displayed(), "Error message should be displayed with invalid credentials"

        # Retrieve and log the actual error message content
        error_message = login_page.get_error_message()
        logger.info(f"Error message displayed: {error_message}")

        # Assert error message text contains expected phrases (example)
        assert login_page.is_invalid_credentials_error_displayed(), \
            "Expected 'Invalid email or password' error message."
