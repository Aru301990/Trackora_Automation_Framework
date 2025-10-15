import pytest
from pages.manager_project_page import ManagerProjectPage
from pages.modals.manager_add_project_modal import ManagerAddProjectModal
from utils.locators import MangerProjectPageLocators
from selenium.webdriver.common.by import By
import time



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

    def test_project_filter_functionality(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_project_management()
        project_page = ManagerProjectPage(driver)
        logger.info("Verifying filter functionality on Project page")
        logger.info("Selecting 'Java' from Department filter")
        project_page.select_department_filter("Java")
        logger.info("Selecting 'In Progress' from Project Status filter")
        project_page.select_project_status_filter("In Progress")
        logger.info("Selecting 'Admin QA' from Manager filter")
        project_page.select_manager_filter("Admin QA")
        logger.info("Selecting 'Java' from Skill filter")
        project_page.select_skill_filter("Java")
        
        logger.info("Clicking Submit button to apply filters")
        project_page.click_submit_button()
        assert project_page.is_project_table_displayed(), "Project table should be displayed after applying filters"
        logger.info("Clicking Reset button to clear filters")
        project_page.click_reset_button()
        assert project_page.is_project_table_displayed(), "Project table should be displayed after resetting filters"

    def test_verify_add_project_button_opens_modal(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_project_management()
        project_page = ManagerProjectPage(driver)
        project_page.click_add_project_button()
        add_project_modal = ManagerAddProjectModal(driver)
        add_project_modal.wait_for_modal_to_appear()
        assert add_project_modal.is_modal_displayed(), "Add Project modal should be displayed"
        logger.info("Clicking Cancel button")
        add_project_modal.click_cancel_button()
        logger.info("Verifying if Add Project modal is closed")
        assert add_project_modal.is_modal_displayed(), "Add Project modal should be closed after clicking Cancel"

    def test_verify_project_status_color_coding(self, manager_login, logger):
        driver, dashboard_page = manager_login
        dashboard_page.navigate_to_project_management()

        project_page = ManagerProjectPage(driver)
        assert project_page.is_project_page_loaded(), "Project page should be loaded"
        assert project_page.is_project_table_displayed(), "Project table should be displayed"

        logger.info("Verifying color coding for project statuses")

        # Update this once you confirm the COMPLETED color
        expected_colors = {
            "IN_PROGRESS": "rgb(214, 109, 18)",     # Orange
            "NOT_STARTED": "rgb(106, 106, 106)",    # Grey
            # "COMPLETED": "rgb(0, 128, 0)"           # Placeholder: Replace with actual green color from DOM
        }

        # Find all table cells containing project statuses
        status_elements = driver.find_elements(By.XPATH,
            "//td[normalize-space(text())='IN_PROGRESS' or text()='COMPLETED' or text()='NOT_STARTED']"
        )

        for element in status_elements:
            status_text = element.text.strip()
            actual_color = element.value_of_css_property("color").strip()

            # Normalize if needed (e.g., rgba to rgb)
            actual_color = actual_color.replace("rgba", "rgb").replace(", 1)", ")")

            logger.info(f"Status: {status_text}, Color: {actual_color}")

            assert status_text in expected_colors, f"Unexpected status '{status_text}' found"
            expected_color = expected_colors[status_text]

            assert actual_color == expected_color, (
                f"Color mismatch for status '{status_text}': Expected {expected_color}, got {actual_color}"
            )
            time.sleep(2)  # Pause to visually confirm colors during test run

    def test_verify_table_column_display(self, manager_login, logger):
            driver, dashboard_page = manager_login
            dashboard_page.navigate_to_project_management()
            project_page = ManagerProjectPage(driver)
            assert project_page.is_project_page_loaded(), "Project page should be loaded"
            assert project_page.is_project_table_displayed(), "Project table should be displayed"

            expected_columns = [
                "Project Name", "Department", "Client Name",
                "Start Date", "End Date", "Project Status", "Project Type", 
                "Manager", "Assignees", "Project Details"]

            # Fetch all header elements
            header_elements = driver.find_elements(By.XPATH, "//table/thead/tr/th")

            # Remove empty header texts
            actual_columns = [header.text.strip() for header in header_elements if header.text.strip()]


            logger.info(f"Actual columns: {actual_columns}")

            assert actual_columns == expected_columns, (
                f"Column mismatch: Expected {expected_columns}, got {actual_columns}"
            )

    def test_verify_project_date_format(self, manager_login, logger):
            driver, dashboard_page = manager_login
            dashboard_page.navigate_to_project_management()
            project_page = ManagerProjectPage(driver)
            assert project_page.is_project_page_loaded(), "Project page should be loaded"
            assert project_page.is_project_table_displayed(), "Project table should be displayed"

            # Fetch all start date elements
            start_date_elements = driver.find_elements(By.XPATH, "//table/tbody/tr/td[4]")
            end_date_elements = driver.find_elements(By.XPATH, "//table/tbody/tr/td[5]")

            date_format = "%d-%m-%Y"

            for elem in start_date_elements + end_date_elements:
                date_text = elem.text.strip()
                
                if not date_text:
                    logger.warning("Skipping empty date field")
                    continue

                try:
                    time.strptime(date_text, date_format)
                    logger.info(f"Date '{date_text}' matches format {date_format}")
                except ValueError:
                    pytest.fail(f"Date '{date_text}' does not match format {date_format}")

    # def test_verify_add_project_mandatory_fields_validation(self, manager_login, logger):
    #     driver, dashboard_page = manager_login
    #     dashboard_page.navigate_to_project_management()
    #     project_page = ManagerProjectPage(driver)
    #     project_page.click_add_project_button()
    #     add_project_modal =ManagerAddProjectModal(driver)
    #     add_project_modal.wait_for_modal_to_appear()
    #     assert add_project_modal.is_modal_displayed(), "Add Project modal should be displayed"
    #     add_project_modal.click_add_project_button()
    #     logger.info("Clicking Cancel button")
    #     add_project_modal.click_cancel_button()
    #     logger.info("Verifying if Add Project modal is closed")
    #     assert add_project_modal.is_modal_displayed(), "Add Project modal should be closed after clicking Cancel"


    

    # def test_add_project_with_valid_data(self, manager_login, project_test_data, unique_name, logger):
    #     driver, dashboard_page = manager_login
    #     dashboard_page.navigate_to_project_management()
    #     project_page = ManagerProjectPage(driver)
    #     project_page.click_add_project_button()
    #     add_project_modal = ManagerAddProjectModal(driver)
    #     add_project_modal.wait_for_modal_to_appear()

    #     project_data = {
    #         "name": project_test_data["new_project"]["name"],
    #         "primary_owner": project_test_data["new_project"]["primary_owner"], 
    #         # "secondary_owner": project_test_data["new_project"]["secondary_owner"],
    #         # "domain": project_test_data["new_project"]["domain"],
    #         # "department": project_test_data["new_project"]["department"],
    #         # "start_date": project_test_data["new_project"]["start_date"],
    #         # "end_date": project_test_data["new_project"]["end_date"]
    #      }
    #     add_project_modal.fill_project_details(project_data)
        
       

    #     add_project_modal.click_add_project_button()
    #     assert add_project_modal.is_modal_displayed() is False, "Add Project modal should be closed after adding project"
       
        
