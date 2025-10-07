"""
Manage Assigned Employees Modal page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import ManageAssignedEmployeesModalLocators
from utils.helpers import WaitHelpers

class ManageAssignedEmployeesModal(BasePage):
    """Manage Assigned Employees Modal class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ManageAssignedEmployeesModalLocators()
        self.wait_helpers = WaitHelpers()

    def is_modal_displayed(self):
        """Check if modal is displayed"""
        return self.is_element_visible(self.locators.MODAL)

    def wait_for_modal_to_appear(self):
        """Wait for modal to appear"""
        return self.wait_helpers.wait_for_modal_to_appear(self.driver, self.locators.MODAL)

    def search_employees(self, employee_name):
        """Search for employees by name"""
        self.send_keys_to_element(self.locators.SEARCH_EMPLOYEES_INPUT, employee_name)

    def search_by_roles(self, role):
        """Search by roles"""
        self.send_keys_to_element(self.locators.SEARCH_ROLES_INPUT, role)

    def search_by_skills(self, skill):
        """Search by primary skills"""
        self.send_keys_to_element(self.locators.SEARCH_SKILLS_INPUT, skill)

    def search_by_secondary_skills(self, skill):
        """Search by secondary skills"""
        self.send_keys_to_element(self.locators.SECONDARY_SKILLS_INPUT, skill)

    def is_employee_list_displayed(self):
        """Check if employee list is displayed"""
        return self.is_element_visible(self.locators.EMPLOYEE_LIST)

    def click_assign_button(self):
        """Click Assign button"""
        self.click_element(self.locators.ASSIGN_BUTTON)

    def click_remove_button(self):
        """Click Remove button"""
        self.click_element(self.locators.REMOVE_BUTTON)

    def click_cancel_button(self):
        """Click Cancel button"""
        self.click_element(self.locators.CANCEL_BUTTON)

    def search_and_assign_employee(self, employee_name):
        """Search for employee and assign"""
        self.search_employees(employee_name)
        # Wait for search results
        import time
        time.sleep(2)
        self.click_assign_button()

    def search_by_multiple_criteria(self, employee_name=None, role=None, primary_skill=None, secondary_skill=None):
        """Search using multiple criteria"""
        if employee_name:
            self.search_employees(employee_name)
        if role:
            self.search_by_roles(role)
        if primary_skill:
            self.search_by_skills(primary_skill)
        if secondary_skill:
            self.search_by_secondary_skills(secondary_skill)
