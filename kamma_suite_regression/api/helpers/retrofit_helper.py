from kamma_suite_regression.request_utility.request_utility import SuiteRequestUtility


class RetrofitHelper:
    def __init__(self, api: SuiteRequestUtility):
        self.api = api
        self.epc_cost_endpoint = "/v3/retrofit/epc-cost"

    def cost_to_epc(self, payload, expected_status_code=200):
        return self.api.post(self.epc_cost_endpoint, data=payload, expected_status_code=expected_status_code)
