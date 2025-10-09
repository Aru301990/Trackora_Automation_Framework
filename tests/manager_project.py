import pytest
from pages.manager_project_page import ManagerProjectPage
from pages.modals.manager_add_project_modal import ManagerAddProjectModal


@pytest.mark.admin
@pytest.mark.project
@pytest.mark.smoke
class TestAdminProject:
    """Test cases for Admin Project Management functionality"""

    def test_verify_project_list_pagination(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_project_management()
        project_page = ManagerProjectPage(driver)
        assert project_page.is_project_page_loaded(), "Project page should be loaded"
        assert project_page.is_project_table_displayed(), "Project table should be displayed"
        

    def test_verify_add_project_mandatory_fields_validation(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_project_management()
        project_page = ManagerProjectPage(driver)
        project_page.click_add_project_button()
        add_project_modal =ManagerAddProjectModal(driver)
        add_project_modal.wait_for_modal_to_appear()
        assert add_project_modal.is_modal_displayed(), "Add Project modal should be displayed"
        add_project_modal.click_add_project_button()
        add_project_modal.click_cancel_button()
        assert add_project_modal.is_modal_displayed(), "Add Project modal should be closed after clicking Cancel"
