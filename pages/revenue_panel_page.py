"""
Revenue Panel page object for Trackora application.
Defines interactions and validations for the Revenue Panel UI components.
"""

from pages.base_page import BasePage
from utils.locators import RevenuePanelPageLocators
from utils.helpers import TestHelpers
from datetime import datetime
import time
from selenium.webdriver.common.keys import Keys

class RevenuePanelPage(BasePage):
    """Page object representing the Revenue Panel page."""

    def __init__(self, driver):
        """
        Initializes the RevenuePanelPage.
        
        Args:
            driver: Selenium WebDriver instance from test fixture.
        """
        super().__init__(driver)
        self.locators = RevenuePanelPageLocators()  # Locators specific to revenue panel

    def is_revenue_panel_loaded(self):
        """
        Verifies that the Revenue Panel page is loaded by checking visibility of the page title.
        
        Returns:
            True if page title element visible, False otherwise.
        """
        return self.is_element_visible(self.locators.PAGE_TITLE)

    def select_department(self, department_name):
        """
        Opens the department dropdown by clicking the container element,
        waits for overlays/spinners to disappear, then clicks the desired option.

        Selects a department from the custom dropdown using dynamic option locators.
        
        Args:
            department_name: The visible text of the department option to select.
        """
        # Wait for any loading overlays or spinners to disappear
        TestHelpers.wait_for_loading_overlay_to_disappear(self.driver)

        # Click the dropdown container (not just arrow) to open options
        dropdown_locator = self.locators.DEPARTMENT_DROPDOWN
        option_locator = self.locators.department_option_locator(department_name)

        # Click dropdown to open options
        TestHelpers.safe_click(self.driver, dropdown_locator)

        # Wait for the option to be clickable instead of fixed sleep
        TestHelpers.wait_for_element_clickable(self.driver, option_locator, timeout=10)

        # Select the option by clicking it    
        # TestHelpers.select_custom_dropdown_option(self.driver, dropdown_locator, option_locator)
        TestHelpers.safe_click(self.driver, option_locator)

    # Commented out the code for select_month since the Month field in app has been changed to Year field
    # def select_month(self, month_name):
    #     """
    #     Selects month using the native <input type="month"> element by converting 
    #     input like 'June, 2025' to 'YYYY-MM' string format and sending keys.
        
    #     Args:
    #         month_name: Month and year string in format like 'June, 2025'.
    #     """
    #     # Convert "June, 2025" to "2025-06" format required by month input
    #     month_date = datetime.strptime(month_name, "%B, %Y").strftime("%Y-%m")
    #     self.send_keys_to_element(self.locators.MONTH_INPUT, month_date)


    def select_year(self, year_str):
        """
        Selects the year by typing it into the editable year input field.

        Args:
            year_str (str): The year string, e.g. '2025'.
        """
        year_input_locator = self.locators.YEAR_INPUT

        # Click dropdown to open options
        TestHelpers.safe_click(self.driver, year_input_locator)

        # Wait for the option to be clickable instead of fixed sleep
        TestHelpers.wait_for_element_clickable(self.driver, year_input_locator, timeout=10)

        TestHelpers.wait_for_element(self.driver, year_input_locator).clear()

        # Use safe_send_keys helper to enter the year (clears field before typing)
        TestHelpers.safe_send_keys(self.driver, year_input_locator, year_str)

        # Press Enter key to confirm selection
        TestHelpers.wait_for_element(self.driver, year_input_locator).send_keys(Keys.ENTER)

    def select_week(self, week_number):
        """
        Selects week from the custom dropdown using dynamic option locators.

        Args:
            week_number: Numeric week identifier (e.g. 1,2,3).
        """
        dropdown_locator = self.locators.WEEK_DROPDOWN
        option_locator = self.locators.week_option_locator(week_number)

        # Click dropdown to open options
        TestHelpers.safe_click(self.driver, dropdown_locator)

        # Wait for the option to be clickable instead of fixed sleep
        TestHelpers.wait_for_element_clickable(self.driver, option_locator, timeout=10)

        # TestHelpers.select_custom_dropdown_option(self.driver, dropdown_locator, option_locator)
        TestHelpers.safe_click(self.driver, option_locator)

    # The commented out method below was presumably a search trigger for filters.
    # def click_search_button(self):
    #     """Click search button"""
    #     self.click_element(self.locators.SEARCH_BUTTON)

    def click_clear_button(self):
        """
        Clicks the 'Clear' button to reset all filter selections.
        """
        element = TestHelpers.wait_for_element_clickable(self.driver, self.locators.CLEAR_BUTTON)
        element.click()

    def click_export_button(self):
        """
        Clicks the 'Export' button to export data from Revenue Panel.
        """
        element = TestHelpers.wait_for_element_clickable(self.driver, self.locators.EXPORT_BUTTON)
        element.click()

    def get_employee_cards_count(self):
        """
        Counts the number of employee cards currently displayed.

        Returns:
            Integer count of employee cards found.
        """
        # Wait for employee cards container or at least the first card visible (optional)
        TestHelpers.wait_for_element(self.driver, self.locators.EMPLOYEE_CARDS, timeout=5)
        elements = self.driver.find_elements(*self.locators.EMPLOYEE_CARDS)
        return len(elements)

    def are_employee_cards_displayed(self):
        """
        Checks if any employee cards are displayed.

        Returns:
            True if at least one employee card exists, False otherwise.
        """
        return self.get_employee_cards_count() > 0

    def click_next_page(self):
        """
        Clicks the 'Next' pagination button if present to load next page.

        Returns:
            True if next page button clicked, False if not present.
        """
        if self.is_element_present(self.locators.NEXT_PAGE_BUTTON):
            element = TestHelpers.wait_for_element_clickable(self.driver, self.locators.NEXT_PAGE_BUTTON)
            element.click()
            return True
        return False

    def click_previous_page(self):
        """
        Clicks the 'Previous' pagination button if present to load previous page.

        Returns:
            True if previous page button clicked, False if not present.
        """
        if self.is_element_present(self.locators.PREVIOUS_PAGE_BUTTON):
            element = TestHelpers.wait_for_element_clickable(self.driver, self.locators.PREVIOUS_PAGE_BUTTON)
            element.click()
            return True
        return False

    def is_pagination_present(self):
        """
        Checks for the presence of pagination controls on the Revenue Panel page.
        Scrolls to pagination element to improve detection reliability.

        Returns:
            True if pagination controls present, False otherwise.
        """
        TestHelpers.scroll_to_element(self.driver, self.locators.PAGINATION_CONTROLS)
        return self.is_element_present(self.locators.PAGINATION_CONTROLS)
    
    def is_previous_page_disabled(self):
        """
        Returns True if the 'Previous' button is disabled, otherwise False.
        """
        try:
            element = self.wait_for_element(self.locators.PREVIOUS_PAGE_BUTTON, timeout=5)
            
            # Get the value of the aria-disabled attribute
            aria_disabled_value = element.get_attribute("aria-disabled") or ""
            
            # Check if aria-disabled is 'true', which means the button is disabled
            if aria_disabled_value == "true":
                return True
            
            # If aria-disabled is not 'true', check if the element is enabled
            return not element.is_enabled()
        except Exception:
            return True  # If button not found, treat as disabled

    def is_next_page_enabled(self):
        """
        Returns True if the 'Next' button is enabled, otherwise False.
        """
        try:
            element = self.wait_for_element(self.locators.NEXT_PAGE_BUTTON, timeout=5)
            
            # Get the value of the aria-disabled attribute
            aria_disabled_value = element.get_attribute("aria-disabled") or ""
            
            # If aria-disabled is 'false', the button is enabled
            if aria_disabled_value == "false":
                return True
            
            # Otherwise, check if the element is enabled and class doesn't contain 'disabled'
            class_attr = element.get_attribute("class") or ""
            return element.is_enabled() and "disabled" not in class_attr.lower()
        except Exception:
            return False  # If the button is not found, treat as disabled


    def are_page_numbers_visible(self):
        """
        Checks if page number elements are visible in the pagination.
        """
        return self.is_element_present(self.locators.PAGINATION_PAGE_NUMBERS)

    def get_current_page_number(self):
        """
        Returns the currently active page number as integer.
        """
        element = self.wait_for_element(self.locators.PAGINATION_ACTIVE_PAGE_NUMBER, timeout=5)
        return int(element.text.strip())

    def apply_filters(self, department=None, year=None, week=None):
        """
        Applies multiple filters by selecting department, year, and week if provided.
        Note: Search button click commented out (may require implementation). Month field changed to Year field, hence commented out select_month.

        Args:
            department: Department name string to filter by (optional).
            month: Month string in 'Month, Year' format (optional).
            year: Year string in 'YYYY' format (optional).
            week: Numeric week filter (optional).
        """
        if department:
            self.select_department(department)
        # Commented out the code for select_month since the Month field in app has been changed to Year field
        # if month:
        #     self.select_month(month)
        if year:
            self.select_year(year)
        if week:
            self.select_week(week)
        # self.click_search_button()  # Uncomment if search is triggered manually

    def clear_all_filters(self):
        """
        Clears all applied filters by clicking the 'Clear' button.
        """
        self.click_clear_button()
