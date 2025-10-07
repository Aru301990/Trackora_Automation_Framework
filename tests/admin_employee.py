import pytest
from pages.employee_page import EmployeePage
from pages.modals.add_employee_modal import AddEmployeeModal

@pytest.mark.admin
@pytest.mark.employees
@pytest.mark.smoke
class TestAdminEmployee:
    """Test cases for Admin Employee Management functionality"""

    def test_verify_employee_list_pagination(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        assert employee_page.is_employee_page_loaded(), "Employee page should be loaded"
        assert employee_page.are_employee_cards_displayed(), "Employee cards should be displayed"
        initial_count = employee_page.get_employee_cards_count()
        if employee_page.is_pagination_present():
            logger.info("Pagination controls found")

    def test_verify_add_employee_form_loads_correctly(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        employee_page.click_add_employees_button()
        add_employee_modal = AddEmployeeModal(driver)
        add_employee_modal.wait_for_modal_to_appear()
        assert add_employee_modal.is_modal_displayed(), "Add Employee modal should be displayed"
        assert add_employee_modal.is_element_visible(add_employee_modal.locators.FIRST_NAME_INPUT), "First name input should be visible"
        assert add_employee_modal.is_element_visible(add_employee_modal.locators.EMAIL_INPUT), "Email input should be visible"
        assert add_employee_modal.is_element_visible(add_employee_modal.locators.SAVE_BUTTON), "Save button should be visible"
        add_employee_modal.click_cancel_button()

    def test_employee_export_functionality(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        employee_page.click_export_button()

    def test_employee_shared_resources_toggle(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        initial_count = employee_page.get_employee_cards_count()
        employee_page.toggle_shared_resources()

    def test_employee_reset_functionality(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        employee_page.click_reset_button()
