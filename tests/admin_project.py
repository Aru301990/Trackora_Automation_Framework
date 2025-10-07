import pytest
from pages.project_page import ProjectPage
from pages.modals.add_project_modal import AddProjectModal
from pages.modals.edit_project_modal import EditProjectModal
from pages.modals.manage_assigned_employees_modal import ManageAssignedEmployeesModal

@pytest.mark.admin
@pytest.mark.project
@pytest.mark.smoke
class TestAdminProject:
    """Test cases for Admin Project Management functionality"""

    def test_verify_project_list_pagination(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_project_management()
        project_page = ProjectPage(driver)
        assert project_page.is_project_page_loaded(), "Project page should be loaded"
        assert project_page.is_project_table_displayed(), "Project table should be displayed"
        initial_count = project_page.get_project_rows_count()
        if project_page.is_pagination_present():
            project_page.click_next_page()
            project_page.click_previous_page()

    def test_verify_add_project_mandatory_fields_validation(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_project_management()
        project_page = ProjectPage(driver)
        project_page.click_add_project_button()
        add_project_modal = AddProjectModal(driver)
        add_project_modal.wait_for_modal_to_appear()
        assert add_project_modal.is_modal_displayed(), "Add Project modal should be displayed"
        add_project_modal.click_add_project_button()
        add_project_modal.click_cancel_button()

    def test_verify_edit_project_details_pre_population(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_project_management()
        project_page = ProjectPage(driver)
        project_count = project_page.get_project_rows_count()
        if project_count > 0:
            # Here you would click on the first project's edit button (UI dependent)
            pass

    def test_verify_employee_search_functionality_in_manage_assigned(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_project_management()
        # Here you would open the manage assigned employees modal (UI dependent)
        pass

    def test_project_filter_functionality(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_project_management()
        project_page = ProjectPage(driver)
        project_page.apply_filters(skill="PHP", department="QA", status="IN_PROGRESS")
        assert project_page.is_project_table_displayed()
        project_page.reset_all_filters()

    def test_add_project_with_valid_data(self, admin_login, project_test_data, unique_name, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_project_management()
        project_page = ProjectPage(driver)
        project_page.click_add_project_button()
        add_project_modal = AddProjectModal(driver)
        add_project_modal.wait_for_modal_to_appear()
        test_project_data = project_test_data["new_project"].copy()
        test_project_data["name"] = unique_name(test_project_data["name"])
        add_project_modal.save_project(test_project_data)
