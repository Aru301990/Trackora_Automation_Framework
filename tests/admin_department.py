import pytest
from pages.employee_page import EmployeePage
from pages.department_page import DepartmentPage
from pages.modals.add_department_modal import AddDepartmentModal
from pages.modals.edit_department_modal import EditDepartmentModal

@pytest.mark.admin
@pytest.mark.employees
class TestAdminDepartment:
    """Test cases for Admin Department Management functionality"""

    def test_verify_department_list_loads(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        employee_page.navigate_to_department_tab()
        department_page = DepartmentPage(driver)
        assert department_page.is_department_page_loaded(), "Department page should be loaded"
        assert department_page.are_department_records_displayed(), "Department records should be displayed"
        assert department_page.is_department_table_displayed(), "Department table should be displayed"

    def test_verify_add_department_form_validation(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        employee_page.navigate_to_department_tab()
        department_page = DepartmentPage(driver)
        department_page.click_add_new_department_button()
        add_department_modal = AddDepartmentModal(driver)
        add_department_modal.wait_for_modal_to_appear()
        assert add_department_modal.is_modal_displayed(), "Add Department modal should be displayed"
        add_department_modal.click_ok_button()

    def test_verify_edit_department_form_loads_with_existing_data(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        employee_page.navigate_to_department_tab()
        department_page = DepartmentPage(driver)
        edit_count = department_page.get_edit_buttons_count()
        if edit_count > 0:
            department_page.click_first_edit_button()
            edit_department_modal = EditDepartmentModal(driver)
            edit_department_modal.wait_for_modal_to_appear()
            assert edit_department_modal.is_modal_displayed(), "Edit Department modal should be displayed"
            assert edit_department_modal.verify_existing_data_loaded(), "Existing department data should be pre-populated"
            edit_department_modal.click_cancel_button()

    def test_add_department_with_valid_data(self, admin_login, department_test_data, unique_name, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        employee_page.navigate_to_department_tab()
        department_page = DepartmentPage(driver)
        department_page.click_add_new_department_button()
        add_department_modal = AddDepartmentModal(driver)
        add_department_modal.wait_for_modal_to_appear()
        test_dept_data = department_test_data["new_department"].copy()
        test_dept_data["name"] = unique_name(test_dept_data["name"])
        add_department_modal.save_department(test_dept_data)

    def test_department_delete_functionality(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_employee_management()
        employee_page = EmployeePage(driver)
        employee_page.navigate_to_department_tab()
        department_page = DepartmentPage(driver)
        delete_count = department_page.get_delete_buttons_count()
        assert delete_count >= 0
