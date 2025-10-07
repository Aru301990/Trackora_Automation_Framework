import pytest
import pytest_order
from pages.dashboard_page import DashboardPage


@pytest.mark.admin
@pytest.mark.dashboard
@pytest.mark.smoke
class TestAdminDashboard:
    """
    Contains test cases focused on verifying the Admin Dashboard page features.
    Marked with admin, dashboard, and smoke for targeted test execution.
    """

    # @pytest.mark.order(1)
    def test_verify_total_expenses_count_year_view(self, admin_login, logger):
        """
        Verifies that the total expenses card is visible and displays a valid numeric value 
        when the Year view is selected on the dashboard.
        """
        driver, dashboard_page = admin_login
        logger.info("Starting test: Verify total expenses count in year view")

        assert dashboard_page.is_dashboard_loaded(), "Dashboard page should be loaded"

        dashboard_page.select_year_view()

        assert dashboard_page.is_total_expenses_card_visible(), "Total expenses card should be visible"

        total_expenses_value = dashboard_page.get_total_expenses_value()

        assert total_expenses_value, "Total expenses value should be displayed"
        assert any(char.isdigit() for char in total_expenses_value), "Total expenses value should contain numbers"

    # @pytest.mark.order(2)
    def test_verify_total_revenue_year_view(self, admin_login, logger):
        """
        Verifies that the total revenue card is visible and displays a valid value (numbers or currency)
        when the Year view is selected on the dashboard.
        """
        driver, dashboard_page = admin_login
        logger.info("Starting test: Verify total revenue in year view")

        assert dashboard_page.is_dashboard_loaded(), "Dashboard page should be loaded"

        dashboard_page.select_year_view()

        assert dashboard_page.is_total_revenue_card_visible(), "Total revenue card should be visible"

        total_revenue_value = dashboard_page.get_total_revenue_value()

        assert total_revenue_value, "Total revenue value should be displayed"
        assert any(char.isdigit() for char in total_revenue_value) or "₹" in total_revenue_value, \
            "Total revenue value should contain numbers or currency symbol"

    # @pytest.mark.order(3)
    def test_dashboard_all_metric_cards_visible(self, admin_login, logger):
        """
        Verifies visibility of all metric cards on the dashboard:
        Total Expenses, Total Revenue, and Total Profit.
        Also verifies that their displayed values are non-empty.
        """
        driver, dashboard_page = admin_login
        logger.info("Starting test: All metric cards visibility")

        assert dashboard_page.is_total_expenses_card_visible(), "Total expenses card should be visible"
        assert dashboard_page.is_total_revenue_card_visible(), "Total revenue card should be visible"
        assert dashboard_page.is_total_profit_card_visible(), "Total profit card should be visible"

        expenses_value = dashboard_page.get_total_expenses_value()
        revenue_value = dashboard_page.get_total_revenue_value()
        profit_value = dashboard_page.get_total_profit_value()

        assert expenses_value, "Expenses value should not be empty"
        assert revenue_value, "Revenue value should not be empty"
        assert profit_value, "Profit value should not be empty"

    # @pytest.mark.order(4)
    def test_dashboard_navigation_tabs(self, admin_login, logger):
        """
        Verifies navigation tabs on the dashboard correctly route to respective pages:
        Revenue Panel, Employee Management, Timesheet, and Project Management.
        Uses browser back navigation after each tab click to return to dashboard.
        """
        driver, dashboard_page = admin_login
        logger.info("Starting test: Dashboard navigation tabs")

        dashboard_page.navigate_to_revenue_panel()
        assert "revenue" in driver.current_url.lower(), "Should navigate to Revenue Panel page"
        print("Revenue Panel page URL is:", driver.current_url)
        driver.back()

        dashboard_page.navigate_to_employee_management()
        assert "employee" in driver.current_url.lower(), "Should navigate to Employee Management page"
        print("Employee Management page URL is:", driver.current_url)
        driver.back()

        dashboard_page.navigate_to_timesheet()
        assert "timesheet" in driver.current_url.lower(), "Should navigate to Timesheet page"
        print("Timesheet page URL is:", driver.current_url)
        driver.back()

        dashboard_page.navigate_to_project_management()
        assert "project" in driver.current_url.lower(), "Should navigate to Project Management page"
        print("Project Management page URL is:", driver.current_url)
        driver.back()
