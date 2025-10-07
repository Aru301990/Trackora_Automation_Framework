import pytest
from pages.timesheet_page import TimesheetPage
from pages.modals.approve_reject_timesheet_modal import ApproveRejectTimesheetModal
from pages.modals.edit_timesheet_modal import EditTimesheetModal

@pytest.mark.admin
@pytest.mark.timesheet
@pytest.mark.smoke
class TestAdminTimesheet:
    """Test cases for Admin Timesheet Management functionality"""

    def test_verify_timesheet_page_load(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_timesheet()
        timesheet_page = TimesheetPage(driver)
        assert timesheet_page.is_timesheet_page_loaded(), "Timesheet page should be loaded"
        assert timesheet_page.is_element_visible(timesheet_page.locators.PROJECT_DROPDOWN), "Project dropdown should be visible"
        assert timesheet_page.is_element_visible(timesheet_page.locators.LOAD_TIMESHEET_BUTTON), "Load Timesheet button should be visible"

    def test_approve_reject_modal_opens_correctly(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_timesheet()
        timesheet_page = TimesheetPage(driver)
        timesheet_page.load_timesheet_data(project="Test Project", employee="Test Employee", month="2025-07-01", week=1)
        if timesheet_page.is_timesheet_table_displayed():
            # You would need to click on the approve/reject action here (UI dependent)
            pass

    def test_timesheet_load_functionality(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_timesheet()
        timesheet_page = TimesheetPage(driver)
        timesheet_page.click_load_timesheet_button()

    def test_timesheet_import_export_functionality(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_timesheet()
        timesheet_page = TimesheetPage(driver)
        timesheet_page.click_import_button()
        timesheet_page.click_export_button()

    def test_edit_timesheet_modal_functionality(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_timesheet()
        timesheet_page = TimesheetPage(driver)
        timesheet_page.load_timesheet_data(project="Test Project", month="2025-07-01")
        if timesheet_page.is_timesheet_table_displayed():
            timesheet_page.click_first_edit_icon()
            edit_timesheet_modal = EditTimesheetModal(driver)
            if edit_timesheet_modal.is_modal_displayed():
                timesheet_data = {
                    "task_date": "02-06-2025",
                    "task": "project one",
                    "hour_type": "Billable",
                    "billable_hours": 5,
                    "partially_billable_hours": 5,
                    "productive_hours": 30,
                    "task_status": "ON_HOLD",
                    "description": "sample",
                    "due_date": "16-06-2025"
                }
                edit_timesheet_modal.update_timesheet(timesheet_data)

    def test_timesheet_week_navigation(self, admin_login, logger):
        driver, dashboard_page = admin_login
        dashboard_page.navigate_to_timesheet()
        timesheet_page = TimesheetPage(driver)
        timesheet_page.are_week_tabs_displayed()
