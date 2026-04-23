"""
Licence Needs widget tests.

Route: /dashboard
Coverage:
  - Widget title and description are visible
  - Mandatory, Additional, Selective badges are displayed
  - Each section has licensed and unlicensed links visible
  - Each section may have a licences applied link
  - Link hrefs point to correct filtered portfolio views
"""

import pytest
from playwright.sync_api import expect

from kamma_suite_regression.pages.licence_needs_widget import LicenceNeedsWidget


@pytest.mark.smoke
@pytest.mark.dashboard
def test_licence_needs_title(authenticated_page):
    """Verify the Current Licence Needs widget title is visible."""
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.title).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_licence_needs_description(authenticated_page):
    """Verify the widget description is visible and correct."""
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.description).to_be_visible()
    expect(widget.description).to_contain_text("Properties requiring a licence, based on rules in effect today")


@pytest.mark.regression
@pytest.mark.dashboard
def test_licence_needs_badges_visible(authenticated_page):
    """Verify all three licence type badges are displayed."""
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.badge_mandatory).to_be_visible()
    expect(widget.badge_additional).to_be_visible()
    expect(widget.badge_selective).to_be_visible()


# --- Mandatory section ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_mandatory_licensed_link_visible(authenticated_page):
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.mandatory_licensed_link).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_mandatory_unlicensed_link_visible(authenticated_page):
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.mandatory_unlicensed_link).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_mandatory_applied_link_visible(authenticated_page):
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.mandatory_applied_link).to_be_visible()


# --- Additional section ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_additional_licensed_link_visible(authenticated_page):
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.additional_licensed_link).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_additional_unlicensed_link_visible(authenticated_page):
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.additional_unlicensed_link).to_be_visible()


# --- Selective section ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_selective_licensed_link_visible(authenticated_page):
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.selective_licensed_link).to_be_visible()


@pytest.mark.regression
@pytest.mark.dashboard
def test_selective_unlicensed_link_visible(authenticated_page):
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()
    expect(widget.selective_unlicensed_link).to_be_visible()


# --- Link href assertions ---

@pytest.mark.regression
@pytest.mark.dashboard
def test_mandatory_link_hrefs(authenticated_page, base_url):
    """Verify mandatory section links point to correct filtered portfolio views."""
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()

    expect(widget.mandatory_licensed_link).to_have_attribute(
        "href",
        f"{base_url}/portfolio?tableFilters%5Bcompliance_status%5D%5Bvalue%5D=1"
        f"&tableFilters%5Baction_text%5D%5Bvalues%5D%5B0%5D=none"
        f"&tableFilters%5Blicence_required%5D%5Bvalues%5D%5B0%5D=mandatory",
    )
    expect(widget.mandatory_applied_link).to_have_attribute(
        "href",
        f"{base_url}/portfolio?tableFilters%5Baction_text%5D%5Bvalues%5D%5B0%5D=licence_requested"
        f"&tableFilters%5Blicence_required%5D%5Bvalues%5D%5B0%5D=mandatory",
    )
    expect(widget.mandatory_unlicensed_link).to_have_attribute(
        "href",
        f"{base_url}/portfolio?tableFilters%5Baction_text%5D%5Bvalues%5D%5B0%5D=missing_licence"
        f"&tableFilters%5Baction_text%5D%5Bvalues%5D%5B1%5D=licence_rejected"
        f"&tableFilters%5Blicence_required%5D%5Bvalues%5D%5B0%5D=mandatory",
    )


@pytest.mark.regression
@pytest.mark.dashboard
def test_additional_link_hrefs(authenticated_page, base_url):
    """Verify additional section links point to correct filtered portfolio views."""
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()

    expect(widget.additional_licensed_link).to_have_attribute(
        "href",
        f"{base_url}/portfolio?tableFilters%5Bcompliance_status%5D%5Bvalue%5D=1"
        f"&tableFilters%5Baction_text%5D%5Bvalues%5D%5B0%5D=none"
        f"&tableFilters%5Blicence_required%5D%5Bvalues%5D%5B0%5D=additional",
    )
    expect(widget.additional_unlicensed_link).to_have_attribute(
        "href",
        f"{base_url}/portfolio?tableFilters%5Baction_text%5D%5Bvalues%5D%5B0%5D=missing_licence"
        f"&tableFilters%5Baction_text%5D%5Bvalues%5D%5B1%5D=licence_rejected"
        f"&tableFilters%5Blicence_required%5D%5Bvalues%5D%5B0%5D=additional",
    )


@pytest.mark.regression
@pytest.mark.dashboard
def test_selective_link_hrefs(authenticated_page, base_url):
    """Verify selective section links point to correct filtered portfolio views."""
    widget = LicenceNeedsWidget(authenticated_page)
    widget.navigate()

    expect(widget.selective_licensed_link).to_have_attribute(
        "href",
        f"{base_url}/portfolio?tableFilters%5Bcompliance_status%5D%5Bvalue%5D=1"
        f"&tableFilters%5Baction_text%5D%5Bvalues%5D%5B0%5D=none"
        f"&tableFilters%5Blicence_required%5D%5Bvalues%5D%5B0%5D=selective",
    )
    expect(widget.selective_unlicensed_link).to_have_attribute(
        "href",
        f"{base_url}/portfolio?tableFilters%5Baction_text%5D%5Bvalues%5D%5B0%5D=missing_licence"
        f"&tableFilters%5Baction_text%5D%5Bvalues%5D%5B1%5D=licence_rejected"
        f"&tableFilters%5Blicence_required%5D%5Bvalues%5D%5B0%5D=selective",
    )
