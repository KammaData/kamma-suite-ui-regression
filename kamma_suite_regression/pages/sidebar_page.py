from playwright.sync_api import Page
from kamma_suite_regression.pages.base_page import BasePage


class SidebarPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.sidebar_navigation = page.locator("nav.fi-sidebar-nav")
        self.dashboard_link = self.sidebar_navigation.locator('a[href$="/dashboard"]')
        self.monitor_group = self.sidebar_navigation.locator('li[data-group-label="Monitor"]')
        self.my_portfolio_link = self.sidebar_navigation.locator('a[href$="/portfolio"]')
        self.exports_link = self.sidebar_navigation.locator('a[href$="/exports"]')
        self.exports_nav_item = self.sidebar_navigation.locator('li.fi-sidebar-item:has(a[href$="/exports"])')
        self.quick_check_group = self.sidebar_navigation.locator('li[data-group-label="Quick Check"]')
        self.manage_company_link = page.locator('a[href*="sso.kammadata.com"]').first

    def click_dashboard(self):
        self.dashboard_link.click()

    def expand_monitor_group(self):
        self.monitor_group.locator(".fi-sidebar-group-btn").click()

    def click_my_portfolio(self):
        self.my_portfolio_link.click()

    def click_exports(self):
        self.exports_link.click()

    def toggle_quick_check_group(self):
        self.quick_check_group.locator(".fi-sidebar-group-btn").click()
