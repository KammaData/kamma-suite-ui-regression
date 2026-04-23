from kamma_suite_regression.request_utility.request_utility import SuiteRequestUtility


class PortfolioHelper:
    def __init__(self, api: SuiteRequestUtility):
        self.api = api
        self.portfolio_endpoint = "/v3/portfolio"
        self.portfolio_stats_endpoint = "/v3/portfolio/stats"
        self.portfolio_overview_stats_endpoint = "/v3/portfolio/stats/overview"
        self.portfolio_determination_stats_endpoint = "/v3/portfolio/stats/determinations"
        self.portfolio_future_determination_stats_endpoint = "/v3/portfolio/stats/future-determinations"

    def get_portfolio(self, expected_status_code=200, **kwargs):
        params = {k: v for k, v in kwargs.items() if v not in (None, False)}
        return self.api.get(self.portfolio_endpoint, params=params, expected_status_code=expected_status_code)

    def create_portfolio(self, payload, expected_status_code=201):
        return self.api.post(self.portfolio_endpoint, data=payload, expected_status_code=expected_status_code)

    def get_portfolio_stats(self, expected_status_code=200):
        return self.api.get(self.portfolio_stats_endpoint, expected_status_code=expected_status_code)

    def get_portfolio_overview_stats(self, expected_status_code=200):
        return self.api.get(self.portfolio_overview_stats_endpoint, expected_status_code=expected_status_code)

    def get_portfolio_determination_stats(self, expected_status_code=200):
        return self.api.get(self.portfolio_determination_stats_endpoint, expected_status_code=expected_status_code)

    def get_portfolio_future_determination_stats(self, expected_status_code=200):
        return self.api.get(self.portfolio_future_determination_stats_endpoint, expected_status_code=expected_status_code)
