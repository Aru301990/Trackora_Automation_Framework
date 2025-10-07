"""
Project page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import ProjectPageLocators

class ProjectPage(BasePage):
    """Project page class"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProjectPageLocators()
    
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
    
    def get_project_rows_count(self):
        """Get count of project rows"""
        elements = self.driver.find_elements(*self.locators.PROJECT_ROWS)
        return len(elements) - 1  # Subtract header row
    
    def is_pagination_present(self):
        """Check if pagination is present"""
        return self.is_element_present(self.locators.PAGINATION_CONTROLS)
    
    def click_next_page(self):
        """Click next page button"""
        if self.is_element_present(self.locators.NEXT_BUTTON):
            self.click_element(self.locators.NEXT_BUTTON)
            return True
        return False
    
    def click_previous_page(self):
        """Click previous page button"""
        if self.is_element_present(self.locators.PREVIOUS_BUTTON):
            self.click_element(self.locators.PREVIOUS_BUTTON)  
            return True
        return False
    
    def apply_filters(self, skill=None, department=None, manager=None, status=None):
        """Apply multiple filters"""
        if skill:
            self.select_skill_filter(skill)
        if department:
            self.select_department_filter(department)
        if manager:
            self.select_manager_filter(manager)
        if status:
            self.select_project_status_filter(status)
        self.click_submit_button()
    
    def reset_all_filters(self):
        """Reset all applied filters"""
        self.click_reset_button()