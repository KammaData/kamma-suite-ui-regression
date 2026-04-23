"""
Portfolio page tests.

Route: /portfolio
Coverage:
  - Overview stats are visible
  - Compliance progress bar is visible
  - Priority action cards are present
  - Priority action cards navigate to correct filtered views
"""

import re
import pytest
from playwright.sync_api import expect

from kamma_suite_regression.pages.portfolio_page import PortfolioPage


@pytest.mark.smoke
@pytest.mark.dashboard
def test_portfolio_overview_stats_visible(authenticated_page):
    """Verify the portfolio overview stats are visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.stat_total_properties).to_be_visible()
    expect(portfolio.stat_compliant).to_be_visible()
    expect(portfolio.stat_not_compliant).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_compliance_progress_bar_visible(authenticated_page):
    """Verify the compliance progress bar is visible."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.compliance_progress_bar).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_priority_action_cards_visible(authenticated_page):
    """Verify priority action cards are rendered on the portfolio page."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.priority_action_cards.first).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_properties_in_breach_visible(authenticated_page):
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.properties_in_breach_link).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_unrecognised_address_visible(authenticated_page):
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.unrecognised_address_link).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_incomplete_property_info_visible(authenticated_page):
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.incomplete_property_info_link).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_properties_in_breach_navigates(authenticated_page, base_url):
    """Verify the Properties in Breach card links to the correct filtered view."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.properties_in_breach_link.click()
    expect(authenticated_page).to_have_url(
        re.compile(rf"{re.escape(base_url)}/portfolio\?.*missing_licence.*licence_rejected")
    )


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_unrecognised_address_navigates(authenticated_page, base_url):
    """Verify the Unrecognised Address card links to the correct filtered view."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.unrecognised_address_link.click()
    expect(authenticated_page).to_have_url(re.compile(rf"{re.escape(base_url)}/portfolio\?.*verify_address"))


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_incomplete_property_info_navigates(authenticated_page, base_url):
    """Verify the Incomplete Property Information card links to the correct filtered view."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.incomplete_property_info_link.click()
    expect(authenticated_page).to_have_url(re.compile(rf"{re.escape(base_url)}/portfolio\?.*occupancy"))


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_filtered_by_occupancy(authenticated_page):
    """Verify the portfolio page loads correctly when filtered by occupancy."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate(filters="tableFilters[action_text][values][0]=occupancy")
    expect(portfolio.stat_total_properties).to_be_visible()
    expect(portfolio.priority_action_cards.first).to_be_visible()


# --- Add property ---

@pytest.mark.smoke
@pytest.mark.dashboard
def test_portfolio_add_property_button_visible(authenticated_page):
    """Verify the Add New Property button is visible on the portfolio page."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.add_property_button).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_add_property_button_text(authenticated_page):
    """Verify the Add New Property button has the correct label."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    expect(portfolio.add_property_button).to_have_text("Add New Property")


@pytest.mark.regression
@pytest.mark.dashboard
def test_portfolio_add_property_button_opens_modal(authenticated_page):
    """Verify clicking the Add New Property button opens a modal dialog."""
    portfolio = PortfolioPage(authenticated_page)
    portfolio.navigate()
    portfolio.add_property_button.click()
    authenticated_page.wait_for_load_state("networkidle")
    expect(authenticated_page.locator("div.fi-modal[role='dialog']")).to_have_class(re.compile("fi-modal-open"))


