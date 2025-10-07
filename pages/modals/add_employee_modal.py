"""
Add Employee Modal page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import AddEmployeeModalLocators
from utils.helpers import WaitHelpers

class AddEmployeeModal(BasePage):
    """Add Employee Modal class"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AddEmployeeModalLocators()
        self.wait_helpers = WaitHelpers()
    
    def is_modal_displayed(self):
        """Check if modal is displayed"""
        return self.is_element_visible(self.locators.MODAL)
    
    def wait_for_modal_to_appear(self):
        """Wait for modal to appear"""
        return self.wait_helpers.wait_for_modal_to_appear(self.driver, self.locators.MODAL)
    
    def enter_first_name(self, first_name):
        """Enter first name"""
        self.send_keys_to_element(self.locators.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name):
        """Enter last name"""
        self.send_keys_to_element(self.locators.LAST_NAME_INPUT, last_name)
    
    def enter_email(self, email):
        """Enter email"""
        self.send_keys_to_element(self.locators.EMAIL_INPUT, email)
    
    def enter_password(self, password):
        """Enter password"""
        self.send_keys_to_element(self.locators.PASSWORD_INPUT, password)
    
    def enter_confirm_password(self, confirm_password):
        """Enter confirm password"""
        self.send_keys_to_element(self.locators.CONFIRM_PASSWORD_INPUT, confirm_password)
    
    def select_department(self, department):
        """Select department from dropdown"""
        self.select_dropdown_by_text(self.locators.DEPARTMENT_DROPDOWN, department)
    
    def select_primary_skill(self, skill):
        """Select primary skill from dropdown"""
        self.select_dropdown_by_text(self.locators.PRIMARY_SKILL_DROPDOWN, skill)
    
    def select_secondary_skill(self, skill):
        """Select secondary skill from dropdown"""
        self.select_dropdown_by_text(self.locators.SECONDARY_SKILL_DROPDOWN, skill)
    
    def click_save_button(self):
        """Click Save Details button"""
        self.click_element(self.locators.SAVE_BUTTON)
    
    def click_cancel_button(self):
        """Click Cancel button"""
        self.click_element(self.locators.CANCEL_BUTTON)
    
    def fill_employee_details(self, employee_data):
        """Fill all employee details"""
        self.enter_first_name(employee_data.get("first_name", ""))
        self.enter_last_name(employee_data.get("last_name", ""))
        self.enter_email(employee_data.get("email", ""))
        self.enter_password(employee_data.get("password", "password123"))
        self.enter_confirm_password(employee_data.get("password", "password123"))
        
        if employee_data.get("department"):
            self.select_department(employee_data["department"])
        if employee_data.get("primary_skill"):
            self.select_primary_skill(employee_data["primary_skill"])
        if employee_data.get("secondary_skill"):
            self.select_secondary_skill(employee_data["secondary_skill"])
    
    def save_employee(self, employee_data):
        """Fill details and save employee"""
        self.fill_employee_details(employee_data)
        self.click_save_button()