from kamma_suite_regression.request_utility.request_utility import SuiteRequestUtility


class DeterminationHelper:
    def __init__(self, api: SuiteRequestUtility):
        self.api = api
        self.determination_endpoint = "/v3/determinations/check"
        self.determination_by_prop_id_endpoint = "/v3/determinations/check/{property_id}"
        self.determination_by_id_endpoint = "/v3/determinations/savedchecks/{kamma_id}"
        self.determination_saved_checks_endpoint = "/v3/determinations/savedchecks"
        self.determination_registry_endpoint = "/v3/determinations/registry-check"

    def spot_check(self, payload, expected_status_code=200):
        return self.api.post(self.determination_endpoint, data=payload, expected_status_code=expected_status_code)

    def spot_check_by_property_id(self, property_id, payload=None, expected_status_code=200):
        return self.api.post(
            self.determination_by_prop_id_endpoint.format(property_id=property_id),
            data=payload,
            expected_status_code=expected_status_code,
        )

    def get_saved_check(self, kamma_id, expected_status_code=200):
        return self.api.get(
            self.determination_by_id_endpoint.format(kamma_id=kamma_id),
            expected_status_code=expected_status_code,
        )

    def get_all_saved_checks(self, expected_status_code=200, **kwargs):
        params = {k: v for k, v in kwargs.items() if v not in (None, False)}
        return self.api.get(
            self.determination_saved_checks_endpoint,
            params=params,
            expected_status_code=expected_status_code,
        )

    def registry_check(self, payload, expected_status_code=200):
        return self.api.post(
            self.determination_registry_endpoint, data=payload, expected_status_code=expected_status_code
        )
