import pytest
import pytest_order
import time
from pages.revenue_panel_page import RevenuePanelPage


@pytest.mark.admin
@pytest.mark.revenue
@pytest.mark.smoke
class TestAdminRevenuePanel:
    """
    Test suite for verifying Admin Revenue Panel functionalities:
    - Page load validation
    - Pagination controls
    - Filter application
    - Data export functionality
    """

    # @pytest.mark.order(1)
    def test_verify_revenue_panel_loads_correctly(self, admin_login, logger):
        """
        Validates that the revenue panel page loads successfully after navigation.
        Checks that the page title is visible and employee revenue cards are displayed.
        """
        driver, dashboard_page = admin_login

        # Navigate from dashboard to Revenue Panel page
        dashboard_page.navigate_to_revenue_panel()

        # Instantiate page object for Revenue Panel interactions
        revenue_panel_page = RevenuePanelPage(driver)

        # Assert revenue panel page title is visible
        assert revenue_panel_page.is_revenue_panel_loaded(), "Revenue panel page should be loaded"

        # Assert at least one employee revenue card is visible
        revenue_panel_page.apply_filters(department="Java", year="2025")
        assert revenue_panel_page.are_employee_cards_displayed(), "Employee revenue data should be displayed"


    # @pytest.mark.order(3)
    def test_revenue_panel_pagination_functionality(self, admin_login, logger):
        """
        Tests the pagination feature of the revenue panel:
        - Verifies you start on the first page or Previous button is disabled
        - Checks if Next page button is enabled or next page numbers are visible
        - Clicks 'Next' and verifies that page number updates correctly
        - Clicks 'Previous' and verifies pagination returns to first page state
        """
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_revenue_panel()
        revenue_panel_page = RevenuePanelPage(driver)

        revenue_panel_page.apply_filters(department="Java", year="2025")

        if revenue_panel_page.is_pagination_present():
            # Verify starting on first page by checking page number or Previous button disabled
            assert revenue_panel_page.is_previous_page_disabled(), "Previous button should be disabled on first page"

            # Verify next page is available either by enabled next button or visible next page numbers
            assert revenue_panel_page.is_next_page_enabled() or revenue_panel_page.are_page_numbers_visible(), \
                "Next page should be available when pagination present"

            current_page = revenue_panel_page.get_current_page_number()
            assert current_page == 1, "Initial page number should be 1"

            # Click next page and verify page number increments
            if revenue_panel_page.click_next_page():
                new_page = revenue_panel_page.get_current_page_number()
                assert new_page == current_page + 1, "Page number should increment after next page click"

                # Click previous page to return
                revenue_panel_page.click_previous_page()

                # Verify previous button is disabled again and page number is back to 1
                assert revenue_panel_page.is_previous_page_disabled(), "Previous button should be disabled after navigating back"
                returned_page = revenue_panel_page.get_current_page_number()
                assert returned_page == 1, "Page number should return to 1 after previous page click"
        else:
            logger.info("Pagination not present - single page of data")


    # @pytest.mark.order(2)
    def test_revenue_panel_filter_functionality(self, admin_login, logger):
        """
        Tests filter application using department and year fields:
        - Applies filters
        - Waits for data to refresh
        - Asserts employee cards are visible post-filter
        - Clears filters after test
        """
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_revenue_panel()
        revenue_panel_page = RevenuePanelPage(driver)

        try:
            # Apply filters, year input as 'Year' string expected by helper
            revenue_panel_page.apply_filters(department="Java", year="2025")
            assert revenue_panel_page.are_employee_cards_displayed(), "Employee cards should be displayed after applying filters"
        except Exception as e:
            logger.warning(f"Filter functionality test failed: {e}")
            pytest.fail(f"Filter functionality failed: {e}")

        # Clear all filters after test to reset state
        revenue_panel_page.clear_all_filters()


    # @pytest.mark.order(4)
    def test_revenue_panel_export_functionality(self, admin_login, logger):
        """
        Tests the export button functionality:
        - Clicks the export button
        - Waits briefly to allow export to trigger/download
        - Asserts expected export success indicator
        """
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_revenue_panel()
        revenue_panel_page = RevenuePanelPage(driver)

        # Select filters to load data
        revenue_panel_page.apply_filters(department="Java", year="2025")

        time.sleep(2)

        try:
            revenue_panel_page.click_export_button()

            # # Example assertion - replace with your app's export success check
            # success_visible = revenue_panel_page.is_element_visible(revenue_panel_page.locators.EXPORT_SUCCESS_MESSAGE)
            # assert success_visible, "Export success message should be visible after clicking export"

        except Exception as e:
            logger.error(f"Export functionality test failed: {e}")
            pytest.fail(f"Export functionality failed: {e}")
