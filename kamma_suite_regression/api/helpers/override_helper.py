from kamma_suite_regression.request_utility.request_utility import SuiteRequestUtility


class OverrideHelper:
    def __init__(self, api: SuiteRequestUtility):
        self.api = api
        self.overrides_endpoint = "/v3/overrides"
        self.override_endpoint = "/v3/overrides/{override_id}"
        self.property_overrides_endpoint = "/v3/overrides/property/{property_id}"

    def create_override(self, payload, expected_status_code=201):
        return self.api.post(self.overrides_endpoint, data=payload, expected_status_code=expected_status_code)

    def get_all_overrides(self, expected_status_code=200, **kwargs):
        params = {k: v for k, v in kwargs.items() if v not in (None, False)}
        return self.api.get(self.overrides_endpoint, params=params, expected_status_code=expected_status_code)

    def get_override(self, override_id, expected_status_code=200):
        return self.api.get(
            self.override_endpoint.format(override_id=override_id),
            expected_status_code=expected_status_code,
        )

    def update_override(self, override_id, payload, expected_status_code=200):
        return self.api.patch(
            self.override_endpoint.format(override_id=override_id),
            data=payload,
            expected_status_code=expected_status_code,
        )

    def delete_override(self, override_id, expected_status_code=200):
        return self.api.delete(
            self.override_endpoint.format(override_id=override_id),
            expected_status_code=expected_status_code,
        )

    def delete_property_overrides(self, property_id, expected_status_code=200):
        return self.api.delete(
            self.property_overrides_endpoint.format(property_id=property_id),
            expected_status_code=expected_status_code,
        )
