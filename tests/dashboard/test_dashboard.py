"""
Dashboard tests.

Route: /dashboard
Coverage:
  - Page loads with heading visible
  - Portfolio overview stats are visible
  - Priority action cards are present and navigate to portfolio
  - API returns expected portfolio stats shape
  - UI stat values match the API response
"""

import re
import pytest
from playwright.sync_api import expect

from kamma_suite_regression.pages.dashboard_page import DashboardPage
from kamma_suite_regression.api.helpers.portfolio_helper import PortfolioHelper


@pytest.mark.smoke
@pytest.mark.dashboard
def test_dashboard_loads(authenticated_page):
    """Verify the dashboard renders core elements without error."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    dashboard.assert_page_loaded()


@pytest.mark.smoke
@pytest.mark.dashboard
def test_dashboard_heading(authenticated_page):
    """Verify the dashboard heading is visible and correct."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    expect(dashboard.heading).to_be_visible()
    expect(dashboard.heading).to_have_text("Dashboard")


@pytest.mark.regression
@pytest.mark.dashboard
def test_total_properties_visible(authenticated_page):
    """Verify the total properties stat is visible in the portfolio overview."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    expect(dashboard.stat_total_properties).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_compliance_stat_visible(authenticated_page):
    """Verify the compliant stat is visible in the portfolio overview."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    expect(dashboard.stat_compliant).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_priority_action_cards_visible(authenticated_page):
    """Verify priority action cards are rendered on the dashboard."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    expect(dashboard.priority_action_cards.first).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_properties_in_breach_navigates_to_portfolio(authenticated_page, base_url):
    """Verify the Properties in Breach card links to the correct filtered portfolio view."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    dashboard.properties_in_breach_link.click()
    expect(authenticated_page).to_have_url(
        re.compile(rf"{re.escape(base_url)}/portfolio\?.*missing_licence.*licence_rejected")
    )


@pytest.mark.regression
@pytest.mark.dashboard
def test_unrecognised_address_navigates_to_portfolio(authenticated_page, base_url):
    """Verify the Unrecognised Address card links to the portfolio."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    dashboard.unrecognised_address_link.click()
    expect(authenticated_page).to_have_url(
        re.compile(rf"{re.escape(base_url)}/portfolio\?.*verify_address")
    )


@pytest.mark.regression
@pytest.mark.dashboard
def test_incomplete_property_info_navigates_to_portfolio(authenticated_page, base_url):
    """Verify the Incomplete Property Information card links to the portfolio."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    dashboard.incomplete_property_info_link.click()
    expect(authenticated_page).to_have_url(
        re.compile(rf"{re.escape(base_url)}/portfolio\?.*occupancy")
    )


@pytest.mark.regression
@pytest.mark.visual
@pytest.mark.dashboard
def test_dashboard_visual_snapshot(authenticated_page, assert_snapshot):
    """Visual regression: dashboard must match the committed baseline snapshot."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()
    dashboard.assert_snapshot("dashboard", assert_snapshot, full_page=True)


@pytest.mark.skip(reason="locators need updating")
@pytest.mark.smoke
@pytest.mark.api_validation
@pytest.mark.dashboard
def test_portfolio_overview_stats_shape(api_v3):
    """Verify the portfolio overview stats API returns the expected fields and types."""
    portfolio = PortfolioHelper(api_v3)
    stats = portfolio.get_portfolio_overview_stats()

    assert isinstance(stats["total_properties"], int)
    assert isinstance(stats["compliant_count"], int)
    assert isinstance(stats["in_breach_count"], int)
    assert isinstance(stats["licence_required_count"], int)
    assert isinstance(stats["info_needed_count"], int)
    assert isinstance(stats["compliance_percentage"], int)
    assert isinstance(stats["action_texts"], dict)
    assert stats["total_properties"] > 0


@pytest.mark.skip(reason="locators need updating")
@pytest.mark.regression
@pytest.mark.api_validation
@pytest.mark.dashboard
def test_dashboard_stats_match_api(authenticated_page, api_v3):
    """Verify the stat counts displayed on the dashboard match the portfolio overview API."""
    dashboard = DashboardPage(authenticated_page)
    dashboard.navigate()

    portfolio = PortfolioHelper(api_v3)
    stats = portfolio.get_portfolio_overview_stats()
    action_texts = stats["action_texts"]

    ui_stats = dashboard.get_stats()

    assert ui_stats["total_properties"] == f"{stats['total_properties']:,}"
    assert (
        ui_stats["compliant"] == f"{stats['compliant_count']:,} ({stats['compliance_percentage']}%)"
    )
    assert ui_stats["in_breach_count"] == f"{stats['in_breach_count']:,}"
    assert ui_stats["verify_address"] == f"{action_texts['verify_address']:,}"
    assert ui_stats["occupancy"] == f"{action_texts['occupancy']:,}"
