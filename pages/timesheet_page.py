"""
Timesheet page object for Trackora application.
"""

from pages.base_page import BasePage
from utils.locators import TimesheetPageLocators

class TimesheetPage(BasePage):
    """Timesheet page class"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = TimesheetPageLocators()
    
    def is_timesheet_page_loaded(self):
        """Check if timesheet page is loaded"""
        return self.is_element_visible(self.locators.PAGE_TITLE)
    
    def select_project(self, project_name):
        """Select project from dropdown"""
        self.select_dropdown_by_text(self.locators.PROJECT_DROPDOWN, project_name)
    
    def select_employee(self, employee_name):
        """Select employee from dropdown"""
        self.select_dropdown_by_text(self.locators.EMPLOYEES_DROPDOWN, employee_name)
    
    def select_month(self, month_date):
        """Select month using date picker"""
        self.send_keys_to_element(self.locators.MONTH_INPUT, month_date)
    
    def select_week(self, week_number):
        """Select week from dropdown"""
        self.select_dropdown_by_text(self.locators.WEEK_DROPDOWN, f"Week {week_number}")
    
    def click_load_timesheet_button(self):
        """Click Load Timesheet button"""
        self.click_element(self.locators.LOAD_TIMESHEET_BUTTON)
    
    def click_import_button(self):
        """Click Import button"""
        self.click_element(self.locators.IMPORT_BUTTON)
    
    def click_export_button(self):
        """Click Export button"""
        self.click_element(self.locators.EXPORT_BUTTON)
    
    def is_timesheet_table_displayed(self):
        """Check if timesheet table is displayed"""
        return self.is_element_visible(self.locators.TIMESHEET_TABLE)
    
    def are_week_tabs_displayed(self):
        """Check if week tabs are displayed"""
        return self.is_element_visible(self.locators.WEEK_TABS)
    
    def get_month_total(self):
        """Get month total value"""
        return self.get_element_text(self.locators.MONTH_TOTAL)
    
    def get_week_total(self):
        """Get week total value"""
        return self.get_element_text(self.locators.WEEK_TOTAL)
    
    def click_first_edit_icon(self):
        """Click first edit icon"""
        edit_icons = self.driver.find_elements(*self.locators.EDIT_ICONS)
        if edit_icons:
            edit_icons[0].click()
    
    def click_first_delete_icon(self):
        """Click first delete icon"""
        delete_icons = self.driver.find_elements(*self.locators.DELETE_ICONS)
        if delete_icons:
            delete_icons[0].click()
    
    def load_timesheet_data(self, project=None, employee=None, month=None, week=None):
        """Load timesheet with specified parameters"""
        if project:
            self.select_project(project)
        if employee:
            self.select_employee(employee)
        if month:
            self.select_month(month)
        if week:
            self.select_week(week)
        self.click_load_timesheet_button()