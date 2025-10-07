"""
Add Department Modal page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import AddDepartmentModalLocators
from utils.helpers import WaitHelpers

class AddDepartmentModal(BasePage):
    """Add Department Modal class"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AddDepartmentModalLocators()
        self.wait_helpers = WaitHelpers()
    
    def is_modal_displayed(self):
        """Check if modal is displayed"""
        return self.is_element_visible(self.locators.MODAL)
    
    def wait_for_modal_to_appear(self):
        """Wait for modal to appear"""
        return self.wait_helpers.wait_for_modal_to_appear(self.driver, self.locators.MODAL)
    
    def select_manager(self, manager_name):
        """Select manager from dropdown"""
        self.select_dropdown_by_text(self.locators.MANAGER_DROPDOWN, manager_name)
    
    def enter_description(self, description):
        """Enter department description"""
        self.send_keys_to_element(self.locators.DESCRIPTION_INPUT, description)
    
    def enter_department_name(self, department_name):
        """Enter department name"""
        self.send_keys_to_element(self.locators.DEPARTMENT_NAME_INPUT, department_name)
    
    def click_ok_button(self):
        """Click OK button"""
        self.click_element(self.locators.OK_BUTTON)
    
    def click_cancel_button(self):
        """Click Cancel button"""
        self.click_element(self.locators.CANCEL_BUTTON)
    
    def fill_department_details(self, department_data):
        """Fill all department details"""
        if department_data.get("manager"):
            self.select_manager(department_data["manager"])
        if department_data.get("description"):
            self.enter_description(department_data["description"])
        if department_data.get("name"):
            self.enter_department_name(department_data["name"])
    
    def save_department(self, department_data):
        """Fill details and save department"""
        self.fill_department_details(department_data)
        self.click_ok_button()