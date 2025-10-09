"""
Add Project Modal page object for Trackora application.
"""

from pages.base_page import BasePage

from utils.helpers import WaitHelpers
from utils.locators import ManagerAddProjectModalLocators

class ManagerAddProjectModal(BasePage):
    """Add Project Modal class"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ManagerAddProjectModalLocators()
        self.wait_helpers = WaitHelpers()
    
    def is_modal_displayed(self):
        """Check if modal is displayed"""
        return self.is_element_visible(self.locators.MODAL)
    
    def wait_for_modal_to_appear(self):
        """Wait for modal to appear"""
        return self.wait_helpers.wait_for_modal_to_appear(self.driver, self.locators.MODAL)
    
    def enter_project_name(self, project_name):
        """Enter project name"""
        self.send_keys_to_element(self.locators.PROJECT_NAME_INPUT, project_name)
        
    def enter_project_description(self, description):
        """Enter project description"""
        self.send_keys_to_element(self.locators.PROJECT_DESCRIPTION_INPUT, description)
    
    def enter_client_name(self, client_name):
        """Enter client name"""
        self.send_keys_to_element(self.locators.CLIENT_NAME_INPUT, client_name)
    
    def enter_start_date(self, start_date):
        """Enter start date"""
        self.send_keys_to_element(self.locators.START_DATE_INPUT, start_date)
    
    def enter_end_date(self, end_date):
        """Enter end date"""
        self.send_keys_to_element(self.locators.END_DATE_INPUT, end_date)
    
    def click_add_project_button(self):
        """Click Add Project button"""
        self.click_element(self.locators.ADD_PROJECT_BUTTON)
    
    def click_cancel_button(self):
        """Click Cancel button"""
        self.click_element(self.locators.CANCEL_BUTTON)
    
    def fill_project_details(self, project_data):
        """Fill all project details"""
        if project_data.get("name"):
            self.enter_project_name(project_data["name"])
        if project_data.get("description"):
            self.enter_project_description(project_data["description"])
        if project_data.get("client_name"):
            self.enter_client_name(project_data["client_name"])
        if project_data.get("start_date"):
            self.enter_start_date(project_data["start_date"])
        if project_data.get("end_date"):
            self.enter_end_date(project_data["end_date"])
    
    def save_project(self, project_data):
        """Fill details and save project"""
        self.fill_project_details(project_data)
        self.click_add_project_button()