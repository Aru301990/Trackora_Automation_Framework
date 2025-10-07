"""
Helper utilities for Trackora automation framework.
Contains common functions used across multiple test files.
"""

import json
import time
import os
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

class TestHelpers:
    """Common helper methods for tests and page objects."""

    @staticmethod
    def load_test_data():
        """
        Loads JSON test data file for fixture and test usage.
        Provides user credentials, mock data, etc.
        Returns a parsed Python dictionary.
        """
        data_path = Path(__file__).parents[1] / "data" / "testdata.json"
        with open(data_path, "r") as f:
            return json.load(f)

    @staticmethod
    def get_user_credentials(user_type="admin"):
        """
        Get user credentials (username/password) for the specified user type.
        Default is 'admin'. If not found, uses 'admin' credentials as fallback.
        """
        test_data = TestHelpers.load_test_data()
        return test_data["users"].get(user_type, test_data["users"]["admin"])

    @staticmethod
    def wait_for_element(driver, locator, timeout=10):
        """
        Waits until an element is present and visible on the DOM.
        Returns the WebElement found. Raises TimeoutException if not found.
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Element not found within {timeout} seconds: {locator}")
        
    @staticmethod
    def wait_for_loading_overlay_to_disappear(driver, timeout=10):
        """
        Waits until any loading spinner/overlay (class '.ant-spin') disappears.
        If no spinner present or times out, proceeds without error.
        """
        try:
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin"))
            )
        except TimeoutException:
            pass

    @staticmethod
    def wait_for_element_clickable(driver, locator, timeout=10):
        """
        Waits until an element is present and clickable.
        Returns the WebElement found. Raises TimeoutException if not clickable.
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Element not clickable within {timeout} seconds: {locator}")

    @staticmethod
    def safe_click(driver, locator, timeout=10):
        """
        Waits for element to be clickable, then clicks it.
        Attempts normal click first; falls back to JavaScript click on failure.
        Returns the clicked WebElement. Use inside page objects for reliability.
        """
        element = TestHelpers.wait_for_element_clickable(driver, locator, timeout)
        try:
            element.click()
        except WebDriverException:
            driver.execute_script("arguments[0].click();", element)
        return element

    @staticmethod
    def safe_send_keys(driver, locator, text, clear_first=True, timeout=10):
        """
        Waits for element to be visible, then sends keys.
        By default, clears field before sending text.
        Use for typing into inputs, search boxes, etc.
        """
        element = TestHelpers.wait_for_element(driver, locator, timeout)
        if clear_first:
            element.clear()
        element.send_keys(text)
        return element

    @staticmethod
    def get_element_text(driver, locator, timeout=10):
        """
        Waits for element to be visible, then gets its .text property.
        Use for reading card values, labels, messages, etc.
        """
        element = TestHelpers.wait_for_element(driver, locator, timeout)
        return element.text

    @staticmethod
    def is_element_present(driver, locator):
        """
        Checks if an element is present on the DOM (does not wait).
        Returns True if found, False otherwise.
        Use for table rows, controls, or pre-click checks.
        """
        try:
            driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    @staticmethod
    def select_dropdown_by_text(driver, dropdown_locator, option_text, timeout=10):
        """
        For native <select> dropdowns:
        - Waits for dropdown element
        - Selects option by visible text using Selenium's Select API.
        """
        from selenium.webdriver.support.ui import Select
        dropdown_element = TestHelpers.wait_for_element(driver, dropdown_locator, timeout)
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)

    @staticmethod
    def select_dropdown_by_value(driver, dropdown_locator, option_value, timeout=10):
        """
        For native <select> dropdowns:
        - Waits for dropdown element
        - Selects option by value using Selenium's Select API.
        """
        from selenium.webdriver.support.ui import Select
        dropdown_element = TestHelpers.wait_for_element(driver, dropdown_locator, timeout)
        select = Select(dropdown_element)
        select.select_by_value(option_value)

    @staticmethod
    def select_custom_dropdown_option(driver, dropdown_locator, option_locator, timeout=10):
        """
        For custom dropdowns (non <select>, e.g. Ant Design):
        - Scrolls dropdown into view, waits for clickability, clicks (JS fallback if intercepted)
        - Waits for animations/overlays to finish
        - Scrolls option into view, waits for clickability, clicks (JS fallback if intercepted)
        Used for UI libraries and cases where select API can't be used.
        """

        # Wait for any loading overlays to disappear
        try:
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ant-spin"))
            )
        except TimeoutException:
            pass

        # Scroll to dropdown and wait until clickable
        TestHelpers.scroll_to_element(driver, dropdown_locator)
        dropdown_element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(dropdown_locator)
        )
        # Try normal click, fallback to JS click if intercepted
        try:
            dropdown_element.click()
        except Exception:
            driver.execute_script("arguments[0].click();", dropdown_element)
        # Wait for UI animation/overlays (can be tuned)
        time.sleep(0.5)
        # Scroll and select desired option
        TestHelpers.scroll_to_element(driver, option_locator)
        option_element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(option_locator)
        )
        try:
            option_element.click()
        except Exception:
            driver.execute_script("arguments[0].click();", option_element)

    @staticmethod
    def scroll_to_element(driver, locator):
        """
        Scrolls the browser viewport so that the targeted element is visible.
        Especially useful for elements that are off-screen due to long pages.
        """
        element = driver.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # Allow time for scroll/animation

    @staticmethod
    def wait_for_page_load(driver, timeout=30):
        """
        Waits until JavaScript document.readyState is 'complete'.
        Ensures whole page has loaded before proceeding.
        Helpful after navigation, login, or page redirects.
        """
        WebDriverWait(driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )


class DataHelpers:
    """
    Helper methods for generating and retrieving test data for parametrized tests.
    """

    @staticmethod
    def get_department_test_data():
        """
        Returns department section test data from loaded testdata.json.
        Used to automate department add/edit/delete flows.
        """
        test_data = TestHelpers.load_test_data()
        return test_data["test_data"]["departments"]

    @staticmethod
    def get_employee_test_data():
        """
        Returns employee section test data from loaded testdata.json.
        Used to automate employee add/edit/delete flows.
        """
        test_data = TestHelpers.load_test_data()
        return test_data["test_data"]["employees"]

    @staticmethod
    def get_project_test_data():
        """
        Returns project section test data from loaded testdata.json.
        Used to automate project add/edit/delete flows.
        """
        test_data = TestHelpers.load_test_data()
        return test_data["test_data"]["projects"]

    @staticmethod
    def generate_unique_name(base_name):
        """
        Generates a unique name for test entities, appending a timestamp to avoid collisions.
        Used for department/project/employee test data.
        """
        timestamp = int(time.time())
        return f"{base_name}_{timestamp}"

    @staticmethod
    def generate_unique_email(base_email):
        """
        Generates a unique email address from a base email, using a timestamp.
        Prevents duplicate user entries during repeated tests.
        """
        timestamp = int(time.time())
        username, domain = base_email.split("@")
        return f"{username}_{timestamp}@{domain}"


class WaitHelpers:
    """
    Specialized wait helpers for modals, overlays, and dynamic UI elements.
    """

    @staticmethod
    def wait_for_modal_to_appear(driver, modal_locator, timeout=10):
        """
        Waits until the modal element is visible in the DOM (shown to user).
        Use before interacting with modal dialogs.
        """
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(modal_locator)
        )

    @staticmethod
    def wait_for_modal_to_disappear(driver, modal_locator, timeout=10):
        """
        Waits until the modal element is no longer visible in the DOM (closed/hidden).
        Use after submitting or canceling modal dialogs.
        """
        return WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located(modal_locator)
        )
