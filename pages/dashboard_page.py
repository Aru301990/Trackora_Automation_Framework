"""
Dashboard page object for Trackora application.
Defines UI interactions and verifications relevant to the main Dashboard page.
"""

from pages.base_page import BasePage
from utils.locators import DashboardPageLocators
from selenium.common.exceptions import NoAlertPresentException

class DashboardPage(BasePage):
    """Page object representing the Dashboard page."""

    def __init__(self, driver):
        """
        Initializes the DashboardPage.
        
        Args:
            driver: Selenium WebDriver instance from test fixture.
        """
        super().__init__(driver)
        self.locators = DashboardPageLocators()  # Dashboard specific locators

    def is_dashboard_loaded(self):
        """
        Verifies that the dashboard page is loaded by checking visibility
        of a key metric card (Total Expenses card).
        
        Returns:
            True if dashboard is loaded, else False.
        """
        return self.is_element_visible(self.locators.TOTAL_EXPENSES_CARD)

    def select_year_view(self):
        """
        Selects the 'Year' radio button on dashboard to switch view.
        """
        self.click_element(self.locators.YEAR_RADIO_BUTTON)

    def select_week_view(self):
        """
        Selects the 'Week' radio button on dashboard to switch view.
        """
        self.click_element(self.locators.WEEK_RADIO_BUTTON)

    def get_total_expenses_value(self):
        """
        Reads and returns the total expenses value displayed on the dashboard.
        """
        return self.get_element_text(self.locators.TOTAL_EXPENSES_VALUE)

    def get_total_revenue_value(self):
        """
        Reads and returns the total revenue value displayed on the dashboard.
        """
        return self.get_element_text(self.locators.TOTAL_REVENUE_VALUE)

    def get_total_profit_value(self):
        """
        Reads and returns the total profit value displayed on the dashboard.
        """
        return self.get_element_text(self.locators.TOTAL_PROFIT_VALUE)

    def is_total_expenses_card_visible(self):
        """
        Checks if the total expenses metric card is visible.
        """
        return self.is_element_visible(self.locators.TOTAL_EXPENSES_CARD)

    def is_total_revenue_card_visible(self):
        """
        Checks if the total revenue metric card is visible.
        """
        return self.is_element_visible(self.locators.TOTAL_REVENUE_CARD)

    def is_total_profit_card_visible(self):
        """
        Checks if the total profit metric card is visible.
        """
        return self.is_element_visible(self.locators.TOTAL_PROFIT_CARD)

    def navigate_to_revenue_panel(self):
        """
        Navigates the browser to the Revenue Panel page via navigation tab.
        """
        self.click_element(self.locators.REVENUE_PANEL_TAB)

    def navigate_to_employee_management(self):
        """
        Navigates the browser to the Employee Management page via navigation tab.
        """
        self.click_element(self.locators.EMPLOYEE_TAB)

    def navigate_to_timesheet(self):
        """
        Navigates the browser to the Timesheet page via navigation tab.
        """
        self.click_element(self.locators.TIMESHEET_TAB)

    def navigate_to_project_management(self):
        """
        Navigates the browser to the Project Management page via navigation tab.
        """
        self.click_element(self.locators.PROJECT_TAB)

    def select_filter_scope(self, scope_value):
        """
        Selects a value in the filter scope dropdown menu on the dashboard.

        Args:
            scope_value: Value string to select in the scope dropdown.
        """
        self.select_dropdown_by_value(self.locators.FILTER_BY_SCOPE_DROPDOWN, scope_value)

    def logout(self):
        """
        Logs out the currently logged-in user by interacting with user profile and logout button.
        """
        self.click_element(self.locators.USER_PROFILE)
        self.click_element(self.locators.LOGOUT_BUTTON)
