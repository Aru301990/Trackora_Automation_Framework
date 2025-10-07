"""
Login page object for Trackora application.
Defines interactions and verifications with the login UI elements.
"""

from pages.base_page import BasePage
from utils.locators import LoginPageLocators
from utils.helpers import TestHelpers

class LoginPage(BasePage):
    """Page object representing the Login page and its behavior."""

    def __init__(self, driver):
        """
        Initializes the LoginPage by setting driver and locators.
        
        Args:
            driver: Selenium WebDriver instance from test fixture.
        """
        super().__init__(driver)
        self.locators = LoginPageLocators()  # Locators specific to login page elements

    def enter_username(self, username):
        """
        Enters the username (email) text into the username input box.

        Args:
            username: The username or email string to enter.
        """
        self.send_keys_to_element(self.locators.USERNAME_INPUT, username)

    def enter_password(self, password):
        """
        Enters the password text into the password input box.

        Args:
            password: The password string to enter.
        """
        self.send_keys_to_element(self.locators.PASSWORD_INPUT, password)

    def click_login_button(self):
        """
        Clicks the Login button to submit the login form.
        """
        self.click_element(self.locators.LOGIN_BUTTON)

    def login(self, username, password):
        """
        Performs the full login sequence:
        - Enters username
        - Enters password
        - Clicks login button
        - Waits for subsequent page to fully load

        Args:
            username: Username/email string to login
            password: Password string
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_page_load()

    def login_as_user_type(self, user_type="admin"):
        """
        Logs in using credentials for a specific user type loaded from test data.
        Defaults to 'admin' if no user_type specified.

        Args:
            user_type: String key specifying user type, e.g. 'admin', 'manager', 'employee'.

        Returns:
            credentials dictionary used (with 'username' and 'password')
        """
        credentials = TestHelpers.get_user_credentials(user_type)
        self.login(credentials["username"], credentials["password"])
        return credentials

    def is_login_page_loaded(self):
        """
        Checks that all key login page elements (username, password, login button)
        are visible on the page, indicating the page is loaded.

        Returns:
            True if elements are visible, False otherwise.
        """
        return (self.is_element_visible(self.locators.USERNAME_INPUT) and
                self.is_element_visible(self.locators.PASSWORD_INPUT) and
                self.is_element_visible(self.locators.LOGIN_BUTTON))

    def get_error_message(self):
        """
        Retrieves any error message displayed on the login page,
        typically after a failed login attempt.

        Returns:
            The error message text if visible, otherwise None.
        """
        if self.is_element_visible(self.locators.ERROR_MESSAGE):
            return self.get_element_text(self.locators.ERROR_MESSAGE)
        return None

    def is_error_displayed(self):
        """
        Checks if an error message element is displayed on the login page.

        Returns:
            True if error message is visible, False otherwise.
        """
        return self.is_element_visible(self.locators.ERROR_MESSAGE)
    
    def is_invalid_credentials_error_displayed(self):
        """
        Returns True if the error message specifically matches 'Invalid email or password'.
        """
        error_message = self.get_error_message()
        return error_message is not None and "Invalid email or password" in error_message

