"""
Add Project Modal page object for Trackora application.
"""

from pages.base_page import BasePage

from utils.helpers import WaitHelpers
from utils.locators import ManagerAddProjectModalLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

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
    
    def get_all_status_elements(self):
        # Adjust this selector based on your HTML
        return self.driver.find_elements(By.CSS_SELECTOR, ".project-status")
    
    def enter_project_name(self, project_name):
        """Enter project name"""
        self.send_keys_to_element(self.locators.PROJECT_NAME_INPUT, project_name)

    def get_text_from_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located(locator)
        )
        return element.text.strip()
    
    def get_selected_primary_owner(self):
        """Get the selected primary owner text"""
        return self.get_text_from_element(self.locators.SELECTED_PRIMARY_OWNER)
    
    def enter_primary_owner(self, primary_owner):
        """Enter primary owner"""
        self.select_dropdown_by_text(self.locators.PRIMARY_OWNER_INPUT, primary_owner)
        time.sleep(1)  # Wait for selection to register
    

    


    

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
        if project_data.get("primary_owner"):
            self.enter_primary_owner(project_data["primary_owner"])
        if project_data.get("secondary_owner"):
            self.enter_secondary_owner(project_data["secondary_owner"])
        if project_data.get("domain"):
            self.enter_domain(project_data["domain"])
        if project_data.get("department"):
            self.enter_department(project_data["department"])
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