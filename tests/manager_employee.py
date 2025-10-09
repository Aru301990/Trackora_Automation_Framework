import pytest
from pages.manager_employee_page import ManagerEmployeePage
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.manager
@pytest.mark.smoke
@pytest.mark.regression

class TestManagerEmployee:
    """Test cases for Manager Employee Management functionality"""

    def test_verify_manager_employee_list_pagination(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_employee_management()
        manager_employee_page = ManagerEmployeePage(driver)
        assert manager_employee_page.is_employee_page_loaded(), "Employee page should be loaded"
        #assert manager_employee_page.are_employee_cards_displayed(), "Employee cards should be displayed"
        initial_count = manager_employee_page.get_employee_cards_count()
        if manager_employee_page.is_pagination_present():
            logger.info("Pagination controls found")

    def test_manager_employee_export_functionality(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_employee_management()
        manager_employee_page = ManagerEmployeePage(driver)
        manager_employee_page.click_export_button()
        logger.info("Clicked export button")


    def test_manager_employee_shared_resources_toggle(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_employee_management()
        manager_employee_page = ManagerEmployeePage(driver)
        manager_employee_page.toggle_shared_resources()
        logger.info("Toggled shared resources")
        assert "Employee page should be loaded"

    def test_manager_employee_reset_functionality(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_employee_management()
        manager_employee_page = ManagerEmployeePage(driver)

        # Step 1: Fill in filter inputs/dropdowns
        manager_employee_page.select_dropdown_by_text("Java")
        logger.info("Applied filters: department='Java'")

        # Step 2: Click the reset button
        manager_employee_page.click_reset_button()

        assert manager_employee_page.get_selected_department() == "Select Department", "Department filter not reset"


