"""
Department page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import DepartmentPageLocators

class DepartmentPage(BasePage):
    """Department page class"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DepartmentPageLocators()
    
    def is_department_page_loaded(self):
        """Check if department page is loaded"""
        return self.is_element_visible(self.locators.PAGE_TITLE)
    
    def click_add_new_department_button(self):
        """Click Add New Department button"""
        self.click_element(self.locators.ADD_NEW_DEPARTMENT_BUTTON)
    
    def is_department_list_displayed(self):
        """Check if department list is displayed"""
        return self.is_element_visible(self.locators.DEPARTMENT_LIST)
    
    def is_department_table_displayed(self):
        """Check if department table is displayed"""
        return self.is_element_visible(self.locators.DEPARTMENT_TABLE)
    
    def get_edit_buttons_count(self):
        """Get count of edit buttons"""
        elements = self.driver.find_elements(*self.locators.EDIT_BUTTONS)
        return len(elements)
    
    def get_delete_buttons_count(self):
        """Get count of delete buttons"""
        elements = self.driver.find_elements(*self.locators.DELETE_BUTTONS)
        return len(elements)
    
    def click_first_edit_button(self):
        """Click the first edit button"""
        edit_buttons = self.driver.find_elements(*self.locators.EDIT_BUTTONS)
        if edit_buttons:
            edit_buttons[0].click()
    
    def click_first_delete_button(self):
        """Click the first delete button"""
        delete_buttons = self.driver.find_elements(*self.locators.DELETE_BUTTONS)
        if delete_buttons:
            delete_buttons[0].click()
    
    def are_department_records_displayed(self):
        """Check if department records are displayed"""
        return self.is_department_table_displayed() and self.get_edit_buttons_count() > 0