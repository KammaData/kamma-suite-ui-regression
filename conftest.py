import os
import re
from datetime import datetime
from dotenv import load_dotenv
import pytest
from playwright.sync_api import expect

from hosts import SUITE_HOSTS

expect.set_options(timeout=15_000)


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="testing",
        help="Target environment: testing, staging",
    )
    parser.addoption(
        "--report-name",
        action="store",
        default=None,
        help="Generate an HTML report with the specified name (e.g., --report-name=my_report)",
    )
    parser.addoption(
        "--redact-credentials",
        action="store_true",
        default=False,
        help="Redact credentials from test output",
    )


def pytest_configure(config):
    env = config.getoption("--env")
    envfile = f".env.{env}"

    if os.path.exists(envfile):
        load_dotenv(envfile, override=True)

    os.environ.setdefault("ENV", env)

    report_name = config.getoption("--report-name")
    html_path = config.getoption("--html", default=None)

    if html_path or report_name:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        user = os.environ.get("USER", "unknown")
        os.makedirs("reports", exist_ok=True)

        if report_name:
            html_report_path = f"reports/{report_name}_{env}_{user}_{timestamp}.html"
            config.option.htmlpath = html_report_path

        if html_path:
            config._additional_html_path = html_path
            if not report_name:
                config.option.htmlpath = html_path

        config.option.self_contained_html = True


def pytest_sessionfinish(session, exitstatus):
    config = session.config
    if hasattr(config, "_additional_html_path") and config.option.htmlpath != config._additional_html_path:
        source_path = config.option.htmlpath
        target_path = config._additional_html_path

        if os.path.exists(source_path):
            import shutil

            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.copy2(source_path, target_path)
            print(f"\nReport also copied to: {target_path}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.longrepr and item.config.getoption("--redact-credentials"):
        report_text = str(report.longrepr)
        report_text = re.sub(r"'Authorization': '[^']*'", "'Authorization': '[REDACTED]'", report_text)
        report_text = re.sub(r"'Cookie': '[^']*'", "'Cookie': '[REDACTED]'", report_text)
        report.longrepr = report_text


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    env = pytestconfig.getoption("--env")
    url = SUITE_HOSTS.get(env, {}).get("kamma-suite")
    if not url:
        raise ValueError(f"No base URL configured for environment: '{env}'")
    return url
