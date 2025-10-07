import pytest
from pages.manager_employee_page import ManagerEmployeePage

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

    def test_manager_employee_shared_resources_toggle(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_employee_management()
        manager_employee_page = ManagerEmployeePage(driver)
        initial_count = manager_employee_page.get_employee_cards_count()
        manager_employee_page.toggle_shared_resources()

    def test_manager_employee_reset_functionality(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_employee_management()
        manager_employee_page = ManagerEmployeePage(driver)
        manager_employee_page.click_reset_button()