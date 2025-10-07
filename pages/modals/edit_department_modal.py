"""
Edit Department Modal page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import EditDepartmentModalLocators
from utils.helpers import WaitHelpers

class EditDepartmentModal(BasePage):
    """Edit Department Modal class"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = EditDepartmentModalLocators()
        self.wait_helpers = WaitHelpers()
    
    def is_modal_displayed(self):
        """Check if modal is displayed"""
        return self.is_element_visible(self.locators.MODAL)
    
    def wait_for_modal_to_appear(self):
        """Wait for modal to appear"""
        return self.wait_helpers.wait_for_modal_to_appear(self.driver, self.locators.MODAL)
    
    def get_current_manager(self):
        """Get currently selected manager"""
        element = self.wait_for_element(self.locators.MANAGER_DROPDOWN)
        return element.get_attribute("value")
    
    def enter_description(self, description):
        """Enter department description"""
        self.send_keys_to_element(self.locators.DESCRIPTION_INPUT, description)
    
    def get_current_description(self):
        """Get current description value"""
        element = self.wait_for_element(self.locators.DESCRIPTION_INPUT)
        return element.get_attribute("value")
    
    def enter_department_name(self, department_name):
        """Enter department name"""
        self.send_keys_to_element(self.locators.DEPARTMENT_NAME_INPUT, department_name)
    
    def get_current_department_name(self):
        """Get current department name value"""
        element = self.wait_for_element(self.locators.DEPARTMENT_NAME_INPUT)
        return element.get_attribute("value")
    
    def click_ok_button(self):
        """Click OK button"""
        self.click_element(self.locators.OK_BUTTON)
    
    def click_cancel_button(self):
        """Click Cancel button"""
        self.click_element(self.locators.CANCEL_BUTTON)
    
    def verify_existing_data_loaded(self):
        """Verify that existing data is pre-populated"""
        return (self.get_current_manager() and 
                self.get_current_description() and 
                self.get_current_department_name())