"""
Locators for Trackora application elements.
Organized by page for easy maintenance, reusability, and readability.
Provides all By-locators for Selenium page objects and modals.
"""

from selenium.webdriver.common.by import By

# ==========================
# Login Page Locators
# ==========================
class LoginPageLocators:
    """Locators for elements on the Login Page."""
    USERNAME_INPUT = (By.ID, "email")  # Input field for username/email
    PASSWORD_INPUT = (By.ID, "password")  # Input field for password
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")  # Login button
    ERROR_MESSAGE = (By.XPATH, "//div[@class='Toastify__toast-body']")  # Element showing errors (toast)
    PAGE_TITLE = (By.TAG_NAME, "title")  # HTML title for login page

# ==========================
# Dashboard Page Locators
# ==========================
class DashboardPageLocators:
    """Locators for the main Dashboard page, including navigation, metrics, and user profile."""
    # Navigation tab buttons
    DASHBOARD_TAB = (By.XPATH, "//a[@class='nav-link active']")
    REVENUE_PANEL_TAB = (By.XPATH, "//a[@href='/RevenuePanel']")
    EMPLOYEE_TAB = (By.XPATH, "//a[@href='/employees']")
    TIMESHEET_TAB = (By.XPATH, "//a[@href='/timesheet']")
    PROJECT_TAB = (By.XPATH, "//a[@href='/project']")

    # Controls for switching between Year/Week views
    YEAR_RADIO_BUTTON = (By.XPATH, "//input[@type='radio' and @value='year']")
    WEEK_RADIO_BUTTON = (By.XPATH, "//input[@type='radio' and @value='week']")

    # Metric Cards
    TOTAL_EXPENSES_CARD = (By.XPATH, "//div[@class='metric-card'][1]")
    TOTAL_EXPENSES_VALUE = (By.XPATH, "//div[@class='metric-card'][1]//div[@class='metric-amount']")
    TOTAL_REVENUE_CARD = (By.XPATH, "//div[@class='metric-card'][2]")
    TOTAL_REVENUE_VALUE = (By.XPATH, "//div[@class='metric-card'][2]//div[@class='metric-amount']")
    TOTAL_PROFIT_CARD = (By.XPATH, "//div[@class='metric-card'][3]")
    TOTAL_PROFIT_VALUE = (By.XPATH, "//div[@class='metric-card'][3]//div[@class='metric-amount']")

    # User Info/Logout
    USER_PROFILE = (By.XPATH, "//button[@type='button']")
    LOGOUT_BUTTON = (By.XPATH, "//strong[text()='Logout']")


# ==========================
# Revenue Panel Page Locators
# ==========================
class RevenuePanelPageLocators:
    """Locators for the Revenue Panel page, including dynamic filter options and cards."""
    PAGE_TITLE = (By.XPATH, "//p[@class='revenue-head']")  # Revenue panel heading/title
    DEPARTMENT_DROPDOWN = (By.XPATH, "//div[contains(@class, 'filter-section') and .//label[text()='Department:']]//div[contains(@class, 'ant-select-selector')]")  # Custom department dropdown input
    # Commenting the locator for MONTH_INPUT since the Month field in app has been changed to Year field    
    # MONTH_INPUT = (By.XPATH, "//input[@id='monthInput']")  # Month picker input
    YEAR_INPUT = (By.XPATH, "//div[contains(@class, 'filter-section')]//div[contains(@class, 'ant-picker')]//input[@placeholder='Select year']")  # Custom year input
    WEEK_DROPDOWN = (By.XPATH, "//div[contains(@class, 'filter-section') and .//label[text()='Week:']]//div[contains(@class, 'ant-select-selector')]")  # Custom week dropdown input
    #SEARCH_BUTTON = (By.XPATH, "//button[contains(text(), 'Search')]")
    CLEAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Clear')]")  # 'Clear' filter button
    EXPORT_BUTTON = (By.XPATH, "//span[contains(text(), 'Export')]")  # Export button

    # ------- Dynamic locator methods for dropdown options -------
    @staticmethod
    def department_option_locator(department_name):
        """
        Locator for a specific department option in the dropdown, matched by visible text.
        Usage: locators.department_option_locator("Java")
        """
        return (By.XPATH, f"//div[@class='ant-select-item-option-content' and normalize-space(text())='{department_name}']")

    @staticmethod
    def week_option_locator(week_number):
        """
        Locator for a specific week option by 'week <number>' text (case-insensitive).
        Usage: locators.week_option_locator(1)
        """
        return (By.XPATH, f"//div[contains(@class, 'ant-select-item-option-content') and contains(text(), 'week {week_number}')]")    

    # Data display / pagination
    # EMPLOYEE_CARDS = (By.XPATH, "//div[@class='col-md-6 col-lg-10']")  # Cards for employee revenue
    EMPLOYEE_CARDS = (By.XPATH, "//div[@class='ant-table-wrapper']")
    PAGINATION_CONTROLS = (By.XPATH, "//ul[@aria-label='Pagination']")
    NEXT_PAGE_BUTTON = (By.XPATH, "//a[@class='page-link' and text()='Next']")
    PREVIOUS_PAGE_BUTTON = (By.XPATH, "//a[@class='page-link' and text()='Previous']")
    PAGINATION_PAGE_NUMBERS = (By.XPATH, "//ul[@aria-label='Pagination']//li[@class='page-item']//a[@role='button' and not(contains(@aria-label, 'Next page')) and not(contains(@aria-label, 'Previous page'))]")
    PAGINATION_ACTIVE_PAGE_NUMBER = (By.XPATH, "//ul[@aria-label='Pagination']//li[@class='page-item active']//a[@role='button' and @aria-current='page']")
    # EXPORT_SUCCESS_MESSAGE = (By.XPATH, "")     # Success message not yet implemented


# ==========================
# Employee Page Locators
# ==========================
class EmployeePageLocators:
    """Locators for Employee Management page and tabs."""
    PAGE_TITLE = (By.XPATH, "//span[contains(text(), 'Employees')]")
    ADD_EMPLOYEES_BUTTON = (By.XPATH, "//button[contains(text(), 'Add Employees')]")
    EXPORT_BUTTON = (By.XPATH, "//button[contains(text(), 'Export')]")
    RESET_BUTTON = (By.XPATH, "//button[contains(text(), 'Reset')]")
    SHARED_RESOURCES_TOGGLE = (By.ID, "shared-resources")  # Shared resources toggle switch

    # Employee list and pagination
    EMPLOYEE_LIST = (By.CLASS_NAME, "employee-list")
    EMPLOYEE_CARDS = (By.CLASS_NAME, "employee-card")
    PAGINATION_CONTROLS = (By.CLASS_NAME, "pagination")

    # Tab navigation
    EMPLOYEE_TAB = (By.XPATH, "//tab[contains(text(), 'Employee')]")
    DEPARTMENT_TAB = (By.XPATH, "//tab[contains(text(), 'Department')]")


# ==========================
# Department Page Locators
# ==========================
class DepartmentPageLocators:
    """Locators for Department Management page and actions."""
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Department')]")
    ADD_NEW_DEPARTMENT_BUTTON = (By.XPATH, "//button[contains(text(), 'Add New Department')]")

    # Department list/table and CRUD action buttons
    DEPARTMENT_LIST = (By.CLASS_NAME, "department-list")
    DEPARTMENT_TABLE = (By.TAG_NAME, "table")
    EDIT_BUTTONS = (By.XPATH, "//button[contains(text(), 'Edit')]")
    DELETE_BUTTONS = (By.XPATH, "//button[contains(text(), 'Delete')]")


# ==========================
# Timesheet Page Locators
# ==========================
class TimesheetPageLocators:
    """Locators for Timesheet Management page and actions."""
    PAGE_TITLE = (By.XPATH, "//h3[contains(text(), 'Manage Timesheet')]")

    # Dropdowns/filters
    PROJECT_DROPDOWN = (By.ID, "project-dropdown")
    EMPLOYEES_DROPDOWN = (By.ID, "employees-dropdown")
    MONTH_INPUT = (By.ID, "month-input")
    WEEK_DROPDOWN = (By.ID, "week-dropdown")

    # Page actions
    LOAD_TIMESHEET_BUTTON = (By.XPATH, "//button[contains(text(), 'Load Timesheet')]")
    IMPORT_BUTTON = (By.XPATH, "//button[contains(text(), 'Import')]")
    EXPORT_BUTTON = (By.XPATH, "//button[contains(text(), 'Export')]")

    # Timesheet display
    TIMESHEET_TABLE = (By.CLASS_NAME, "timesheet-table")
    WEEK_TABS = (By.CLASS_NAME, "week-tabs")
    EDIT_ICONS = (By.XPATH, "//i[contains(@class, 'edit-icon')]")
    DELETE_ICONS = (By.XPATH, "//i[contains(@class, 'delete-icon')]")

    # Totals display
    MONTH_TOTAL = (By.ID, "month-total")
    WEEK_TOTAL = (By.ID, "week-total")


# ==========================
# Project Page Locators
# ==========================
class ProjectPageLocators:
    """Locators for Project Management page and actions."""
    PAGE_TITLE = (By.XPATH, "//h3[contains(text(), 'Projects')]")
    ADD_PROJECT_BUTTON = (By.XPATH, "//button[contains(text(), 'Add Project')]")

    # Filters for searching projects
    SKILL_DROPDOWN = (By.ID, "skill-filter")
    DEPARTMENT_DROPDOWN = (By.ID, "department-filter")
    MANAGER_DROPDOWN = (By.ID, "manager-filter")
    PROJECT_STATUS_DROPDOWN = (By.ID, "project-status-filter")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit')]")
    RESET_BUTTON = (By.XPATH, "//button[contains(text(), 'Reset')]")

    # Project list and pagination
    PROJECT_TABLE = (By.CLASS_NAME, "project-table")
    PROJECT_ROWS = (By.XPATH, "//table//tr")
    PAGINATION_CONTROLS = (By.CLASS_NAME, "pagination")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
    PREVIOUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Previous')]")


# ==========================
# Modal Locators for Add/Edit/Assign dialogs
# ==========================
class AddEmployeeModalLocators:
    """Locators for the Add Employee modal dialog."""
    MODAL = (By.CLASS_NAME, "add-employee-modal")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "confirm-password")
    DEPARTMENT_DROPDOWN = (By.ID, "department")
    PRIMARY_SKILL_DROPDOWN = (By.ID, "primary-skill")
    SECONDARY_SKILL_DROPDOWN = (By.ID, "secondary-skill")
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Save Details')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")

class AddDepartmentModalLocators:
    """Locators for the Add Department modal dialog."""
    MODAL = (By.CLASS_NAME, "add-department-modal")
    MANAGER_DROPDOWN = (By.ID, "manager")
    DESCRIPTION_INPUT = (By.ID, "description")
    DEPARTMENT_NAME_INPUT = (By.ID, "department-name")
    OK_BUTTON = (By.XPATH, "//button[contains(text(), 'OK')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")

class EditDepartmentModalLocators:
    """Locators for the Edit Department modal dialog."""
    MODAL = (By.CLASS_NAME, "edit-department-modal")
    MANAGER_DROPDOWN = (By.ID, "manager")
    DESCRIPTION_INPUT = (By.ID, "description")
    DEPARTMENT_NAME_INPUT = (By.ID, "department-name")
    OK_BUTTON = (By.XPATH, "//button[contains(text(), 'OK')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")

class AddProjectModalLocators:
    """Locators for the Add Project modal dialog."""
    MODAL = (By.CLASS_NAME, "add-project-modal")
    PROJECT_NAME_INPUT = (By.ID, "project-name")
    PROJECT_DESCRIPTION_INPUT = (By.ID, "project-description")
    CLIENT_NAME_INPUT = (By.ID, "client-name")
    START_DATE_INPUT = (By.ID, "start-date")
    END_DATE_INPUT = (By.ID, "end-date")
    ADD_PROJECT_BUTTON = (By.XPATH, "//button[contains(text(), 'Add Project')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")

class ManageAssignedEmployeesModalLocators:
    """Locators for the Manage Assigned Employees modal dialog."""
    MODAL = (By.CLASS_NAME, "manage-employees-modal")
    SEARCH_EMPLOYEES_INPUT = (By.ID, "search-employees")
    SEARCH_ROLES_INPUT = (By.ID, "search-roles")
    SEARCH_SKILLS_INPUT = (By.ID, "search-skills")
    EMPLOYEE_LIST = (By.CLASS_NAME, "employee-list")
    ASSIGN_BUTTON = (By.XPATH, "//button[contains(text(), 'Assign')]")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(), 'Remove')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Cancel')]")


# ==========================
# Manager Employees Page Locators
# ==========================
class ManagerEmployeesPageLocators:
    """Locators for Manager Employee page and tabs."""
    PAGE_TITLE = (By.XPATH, "//span[contains(text(), 'Employees')]")
    EXPORT_BUTTON = (By.XPATH, "//button[contains(text(), 'Export')]")
    RESET_BUTTON = (By.XPATH, "//button[contains(text(), 'Reset')]")
    SHARED_RESOURCES_TOGGLE = (By.XPATH, "//div[@class='toggle-thumb']")  # Shared resources toggle switch


# Manager Employee list and pagination
    EMPLOYEE_LIST = (By.CLASS_NAME, "employee-list")
    EMPLOYEE_CARDS = (By.CLASS_NAME, "employee-card")
    PAGINATION_CONTROLS = (By.CLASS_NAME, "pagination")


    # ==========================
    # Manager Project Page Locators
    # ==========================
class MangerProjectPageLocators:
    """Locators for Project Management page and actions."""
    PAGE_TITLE = (By.XPATH, "//h3[contains(text(), 'Projects')]")
    ADD_PROJECT_BUTTON = (By.XPATH, "//span[@class='px-2']")

    # Filters for searching projects
    SKILL_DROPDOWN = (By.XPATH, "(//select[@class='form-select custom-select'])[5]")
    DEPARTMENT_DROPDOWN = (By.XPATH,"//div[@class='card']//div[2]//select[1]")
    MANAGER_DROPDOWN = (By.XPATH,"(//select[@class='form-select custom-select'])[4]")
    PROJECT_STATUS_DROPDOWN = (By.XPATH,"(//select[@class='form-select custom-select'])[3]")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Submit']")
    RESET_BUTTON = (By.XPATH, "//button[normalize-space()='Reset']")

    # Project list and pagination
    PROJECT_TABLE = (By.XPATH, "//body/div[@id='root']/div[@class='app-container d-flex']"
    "/div[@class='main-content flex-grow-1 d-flex flex-column']/div[@class='page-content"
    " flex-grow-1']/div[@class='container-"
    "fluid']/div[@class='card']/div[@class='card-body card-body']/div[1]")
    PROJECT_ROWS = (By.XPATH, "//table//tr")
    PAGINATION_CONTROLS = (By.CLASS_NAME, "pagination")
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Next')]")
    PREVIOUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Previous')]")

class ManagerAddProjectModalLocators:
    """Locators for the Manager Add Project modal dialog."""
    MODAL = (By.XPATH, "//div[@class='ant-modal-content']")
    PROJECT_NAME_INPUT = (By.ID, "projectForm_projectName")
    PRIMARY_OWNER_INPUT = (By.XPATH, "//span[@title='Select Primary Owner']")
    SELECTED_PRIMARY_OWNER = (By.CSS_SELECTOR, "span.ant-select-selection-item")
    SECONDARY_OWNER_INPUT = (By.XPATH, "//span[@title='Select Secondary Owner']")
    DOMAIN_INPUT = (By.XPATH, "//span[@title='Select Domain']")
    DEPARTMENT_INPUT = (By.XPATH, "//span[@title='Select Department']")
    PROJECT_DESCRIPTION_INPUT = (By.ID, "project-description")
    CLIENT_NAME_INPUT = (By.ID, "client-name")
    START_DATE_INPUT = (By.XPATH, "//input[@id='projectForm_startDate']")
    END_DATE_INPUT = (By.XPATH, "//input[@id='projectForm_endDate']")
    ADD_PROJECT_BUTTON = (By.XPATH, "(//span[contains(text(),'Add Project')])[3]")
    CANCEL_BUTTON = (By.XPATH, "//span[normalize-space()='Cancel']")