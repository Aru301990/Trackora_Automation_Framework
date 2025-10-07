"""
Base page class containing common functionality for all pages.
Provides reusable actions and checks for Selenium page objects.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from utils.helpers import TestHelpers

class BasePage:
    """
    Base class for all page object models.
    Provides common methods (waits, clicks, input, checks) for Trackora pages.
    All app page objects should inherit from this for DRY/reusability.
    """

    def __init__(self, driver):
        """
        Initializes base page object with Selenium driver,
        default explicit wait, and a helpers instance for all utility methods.
        - driver: Selenium WebDriver instance (provided by fixture)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Default 10s for explicit waits
        self.helpers = TestHelpers()           # Utility helpers (static methods)

    def handle_login_popup_alert(self, timeout=5):
        """
        Detect and accept any browser alert popup present.
        Returns alert text if alert was present, else None.
        """
        try:
            alert = WebDriverWait(self.driver, timeout).until(lambda d: d.switch_to.alert)
            alert_text = alert.text
            alert.accept()
            return alert_text
        except (NoAlertPresentException, TimeoutException):
            return None

    def wait_for_element(self, locator, timeout=10):
        """
        Waits for an element to be visible in the DOM.
        Returns the element WebElement when found.
        Usage: page.wait_for_element(page.locators.SOME_ELEMENT)
        """
        return self.helpers.wait_for_element(self.driver, locator, timeout)

    def wait_for_element_clickable(self, locator, timeout=10):
        """
        Waits for an element to be visible and clickable.
        Returns element WebElement.
        Usage: page.wait_for_element_clickable(page.locators.BUTTON)
        """
        return self.helpers.wait_for_element_clickable(self.driver, locator, timeout)

    def click_element(self, locator, timeout=10):
        """
        Waits for element to be clickable and clicks it.
        Returns element after click.
        Usage: page.click_element(page.locators.BUTTON)
        """
        return self.helpers.safe_click(self.driver, locator, timeout)

    def send_keys_to_element(self, locator, text, clear_first=True, timeout=10):
        """
        Waits for input element, clears it (by default), then types text.
        Usage: page.send_keys_to_element(page.locators.INPUT, "some value")
        """
        return self.helpers.safe_send_keys(self.driver, locator, text, clear_first, timeout)

    def get_element_text(self, locator, timeout=10):
        """
        Gets .text from an element after waiting for visibility.
        Usage: val = page.get_element_text(page.locators.CARD)
        """
        return self.helpers.get_element_text(self.driver, locator, timeout)

    def is_element_present(self, locator):
        """
        Checks if element located by locator exists in DOM (does not wait).
        Returns True if present, False otherwise.
        Usage: if page.is_element_present(page.locators.TITLE): ...
        """
        return self.helpers.is_element_present(self.driver, locator)

    def is_element_visible(self, locator, timeout=5):
        """
        Checks if the element is visible. Waits up to timeout seconds.
        Returns True if visible, False otherwise.
        Usage: if page.is_element_visible(page.locators.PANEL): ...
        """
        try:
            self.wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def scroll_to_element(self, locator):
        """
        Scrolls the page viewport to bring the element into view.
        Useful for off-screen elements and long pages.
        Usage: page.scroll_to_element(page.locators.BUTTON)
        """
        self.helpers.scroll_to_element(self.driver, locator)

    def select_dropdown_by_text(self, dropdown_locator, option_text):
        """
        Select option by visible text in a native <select> dropdown.
        Usage: page.select_dropdown_by_text(page.locators.DROPDOWN, "Option A")
        """
        self.helpers.select_dropdown_by_text(self.driver, dropdown_locator, option_text)

    def select_dropdown_by_value(self, dropdown_locator, option_value):
        """
        Select option by 'value' in a native <select> dropdown.
        Usage: page.select_dropdown_by_value(page.locators.DROPDOWN, "option1")
        """
        self.helpers.select_dropdown_by_value(self.driver, dropdown_locator, option_value)

    def get_page_title(self):
        """
        Gets the current browser tab's page title.
        Usage: title = page.get_page_title()
        """
        return self.driver.title

    def get_current_url(self):
        """
        Gets current browser page URL.
        Usage: url = page.get_current_url()
        """
        return self.driver.current_url

    def refresh_page(self):
        """
        Refreshes the current web page.
        Usage: page.refresh_page()
        """
        self.driver.refresh()

    def wait_for_page_load(self, timeout=30):
        """
        Waits for the entire page (document.readyState == 'complete').
        Ensures navigation/load/redirects are done before proceeding.
        Usage: page.wait_for_page_load()
        """
        self.helpers.wait_for_page_load(self.driver, timeout)
