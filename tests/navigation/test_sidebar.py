"""
Sidebar navigation tests.

Route: /exports (starting point for all sidebar tests)
Coverage:
  - Sidebar nav is visible
  - Dashboard link navigates correctly
  - Monitor group expands to show portfolio link
  - My Portfolio link navigates correctly
  - Exports link is active/highlighted on the exports page
  - Quick Check group toggles open and closed
"""

import re
import pytest
from playwright.sync_api import expect

from kamma_suite_regression.pages.export_page import ExportPage
from kamma_suite_regression.pages.sidebar_page import SidebarPage


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def sidebar(authenticated_page):
    """Navigate to the exports page and return a SidebarPage."""
    ExportPage(authenticated_page).navigate()
    return SidebarPage(authenticated_page)


# ---------------------------------------------------------------------------
# Sidebar visibility
# ---------------------------------------------------------------------------

@pytest.mark.smoke
@pytest.mark.navigation
def test_sidebar_navigation_visible(sidebar):
    """Sidebar nav is rendered on the page."""
    expect(sidebar.sidebar_navigation).to_be_visible()


# ---------------------------------------------------------------------------
# Dashboard link
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.navigation
def test_dashboard_link_navigates_correctly(sidebar, base_url):
    """Clicking the Dashboard link routes to /dashboard."""
    sidebar.click_dashboard()
    sidebar.page.wait_for_load_state("networkidle")
    expect(sidebar.page).to_have_url(re.compile(rf"{re.escape(base_url)}/dashboard"))


# ---------------------------------------------------------------------------
# Monitor group
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.navigation
def test_monitor_group_expand(sidebar):
    """Expanding the Monitor group reveals the My Portfolio link."""
    sidebar.expand_monitor_group()
    expect(sidebar.my_portfolio_link).to_be_visible()


@pytest.mark.regression
@pytest.mark.navigation
def test_my_portfolio_link_navigates_correctly(sidebar, base_url):
    """Clicking My Portfolio routes to /portfolio."""
    sidebar.expand_monitor_group()
    sidebar.click_my_portfolio()
    sidebar.page.wait_for_load_state("networkidle")
    expect(sidebar.page).to_have_url(re.compile(rf"{re.escape(base_url)}/portfolio"))


# ---------------------------------------------------------------------------
# Exports link state
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.navigation
def test_exports_link_is_active(sidebar):
    """Exports nav item has the active class when on the exports page."""
    expect(sidebar.exports_nav_item).to_have_class(re.compile(r"fi-active"))


# ---------------------------------------------------------------------------
# Quick Check group
# ---------------------------------------------------------------------------

@pytest.mark.regression
@pytest.mark.navigation
def test_quick_check_group_toggle_close(sidebar):
    """Toggling the Quick Check group adds fi-collapsed to the group item."""
    sidebar.toggle_quick_check_group()
    expect(sidebar.quick_check_group).to_have_class(re.compile(r"fi-collapsed"))


@pytest.mark.regression
@pytest.mark.navigation
def test_quick_check_group_toggle_open(sidebar):
    """Toggling the Quick Check group twice returns it to expanded state."""
    sidebar.toggle_quick_check_group()
    sidebar.toggle_quick_check_group()
    expect(sidebar.quick_check_group).not_to_have_class(re.compile(r"fi-collapsed"))
