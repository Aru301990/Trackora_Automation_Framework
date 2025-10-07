"""
Edit Project Modal page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import EditProjectModalLocators
from utils.helpers import WaitHelpers

class EditProjectModal(BasePage):
    """Edit Project Modal class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = EditProjectModalLocators()
        self.wait_helpers = WaitHelpers()

    def is_modal_displayed(self):
        """Check if modal is displayed"""
        return self.is_element_visible(self.locators.MODAL)

    def wait_for_modal_to_appear(self):
        """Wait for modal to appear"""
        return self.wait_helpers.wait_for_modal_to_appear(self.driver, self.locators.MODAL)

    def get_current_project_name(self):
        """Get current project name value"""
        element = self.wait_for_element(self.locators.PROJECT_NAME_INPUT)
        return element.get_attribute("value")

    def enter_project_name(self, project_name):
        """Enter project name"""
        self.send_keys_to_element(self.locators.PROJECT_NAME_INPUT, project_name)

    def get_current_project_description(self):
        """Get current project description value"""
        element = self.wait_for_element(self.locators.PROJECT_DESCRIPTION_INPUT)
        return element.get_attribute("value")

    def enter_project_description(self, description):
        """Enter project description"""
        self.send_keys_to_element(self.locators.PROJECT_DESCRIPTION_INPUT, description)

    def click_update_button(self):
        """Click Update button"""
        self.click_element(self.locators.UPDATE_BUTTON)

    def click_delete_button(self):
        """Click Delete button"""
        self.click_element(self.locators.DELETE_BUTTON)

    def click_cancel_button(self):
        """Click Cancel button"""
        self.click_element(self.locators.CANCEL_BUTTON)

    def update_project_details(self, project_data):
        """Update project details"""
        if project_data.get("name"):
            self.enter_project_name(project_data["name"])
        if project_data.get("description"):
            self.enter_project_description(project_data["description"])

    def save_changes(self, project_data=None):
        """Update details and save changes"""
        if project_data:
            self.update_project_details(project_data)
        self.click_update_button()

    def delete_project(self):
        """Delete the project"""
        self.click_delete_button()
        # Handle confirmation dialog if present

    def verify_existing_data_loaded(self):
        """Verify that existing data is pre-populated"""
        return (self.get_current_project_name()
            and self.get_current_project_description())
