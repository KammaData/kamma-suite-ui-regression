import random
import string
import time
from typing import Callable, Any


def generate_random_string(length: int = 10) -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


def generate_random_email() -> str:
    return f"test.{generate_random_string(8)}@kamma-test.com"


def wait_for_condition(
    fn: Callable,
    condition: Callable[[Any], bool] = None,
    retries: int = 5,
    delay: int = 2,
    error_msg: str = "Condition not met within the retry limit.",
) -> Any:
    """
    Polls fn() up to `retries` times with `delay` seconds between attempts.
    If `condition` is provided, retries until condition(result) is truthy.
    Raises TimeoutError if the condition is never met.

    Mirrors the poll_until() pattern from kamma-api-regression.
    """
    for attempt in range(retries):
        result = fn()
        if condition is None or condition(result):
            return result
        if attempt < retries - 1:
            time.sleep(delay)

    raise TimeoutError(error_msg)


def compare_ui_with_api(ui_values: dict, api_values: dict) -> tuple[bool, list[str]]:
    """
    Compare a flat dict of values extracted from the UI against the corresponding
    API response fields.

    Returns (is_match, mismatches) where mismatches is a list of human-readable
    difference strings.

    Usage:
        ui = {"property_count": "42", "status": "Active"}
        api = {"total_properties": 42, "status": "active"}
        # field name mapping and type coercion are the caller's responsibility
        ok, diffs = compare_ui_with_api({"count": "42"}, {"count": "42"})
    """
    mismatches = []
    all_keys = set(ui_values) | set(api_values)

    for key in sorted(all_keys):
        ui_val = ui_values.get(key)
        api_val = api_values.get(key)

        if str(ui_val) != str(api_val):
            mismatches.append(f"  {key}: UI={ui_val!r} | API={api_val!r}")

    return (len(mismatches) == 0, mismatches)
