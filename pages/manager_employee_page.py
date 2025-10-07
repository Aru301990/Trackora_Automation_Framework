"""
Manager Employee page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import ManagerEmployeesPageLocators

class ManagerEmployeePage(BasePage):
    """Employee page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ManagerEmployeesPageLocators()
    
    def is_employee_page_loaded(self):
        """Check if employee page is loaded"""
        return self.is_element_visible(self.locators.PAGE_TITLE)
    
    def click_export_button(self):
        """Click export button"""
        self.click_element(self.locators.EXPORT_BUTTON)
    
    def click_reset_button(self):
        """Click reset button"""
        self.click_element(self.locators.RESET_BUTTON)
    
    def toggle_shared_resources(self):
        """Toggle shared resources switch"""
        self.click_element(self.locators.SHARED_RESOURCES_TOGGLE)

    def get_employee_cards_count(self):
        """Get count of employee cards"""
        elements = self.driver.find_elements(*self.locators.EMPLOYEE_CARDS)
        return len(elements)

    def are_employee_cards_displayed(self):
        """Check if employee cards are displayed"""
        return self.get_employee_cards_count() > 0
    
    def is_pagination_present(self):
        """Check if pagination is present"""
        return self.is_element_present(self.locators.PAGINATION_CONTROLS)