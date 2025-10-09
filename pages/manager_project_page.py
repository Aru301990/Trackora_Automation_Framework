"""
Manager Project page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import MangerProjectPageLocators

class ManagerProjectPage(BasePage):
    """Project page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MangerProjectPageLocators()

    def is_project_page_loaded(self):
        """Check if project page is loaded"""
        return self.is_element_visible(self.locators.PAGE_TITLE)
    
    def click_add_project_button(self):
        """Click Add Project button"""
        self.click_element(self.locators.ADD_PROJECT_BUTTON)
        
    def select_skill_filter(self, skill):
        """Select skill from filter dropdown"""
        self.select_dropdown_by_text(self.locators.SKILL_DROPDOWN, skill)
    
    def select_department_filter(self, department):
        """Select department from filter dropdown"""
        self.select_dropdown_by_text(self.locators.DEPARTMENT_DROPDOWN, department)
    
    def select_manager_filter(self, manager):
        """Select manager from filter dropdown"""  
        self.select_dropdown_by_text(self.locators.MANAGER_DROPDOWN, manager)
    
    def select_project_status_filter(self, status):
        """Select project status from filter dropdown"""
        self.select_dropdown_by_text(self.locators.PROJECT_STATUS_DROPDOWN, status)
    
    def click_submit_button(self):
        """Click Submit button"""
        self.click_element(self.locators.SUBMIT_BUTTON)
    
    def click_reset_button(self):
        """Click Reset button"""
        self.click_element(self.locators.RESET_BUTTON)

    def is_project_table_displayed(self):
        """Check if project table is displayed"""
        return self.is_element_visible(self.locators.PROJECT_TABLE)