import os

SUITE = {
    "testing": {
        "base_url": "https://liam-suite.kammadata.org",
        "username": "SUITE_USERNAME",
        "password": "SUITE_PASSWORD",
    },
    "staging": {
        "base_url": "https://suite-staging.kammadata.io",
        "username": "SUITE_USERNAME",
        "password": "SUITE_PASSWORD",
    },
}

API_V3 = {
    "testing": {
        "base_url": f"https://{os.environ.get('USER', 'liam')}-api-v3.kammadata.org",
        "api_token": "KAMMA_APIV3_TOKEN",
        "group_id": "KAMMA_PS_API_GROUP_ID",
    },
    "staging": {
        "base_url": "https://api-v3-staging.kammadata.io",
        "api_token": "KAMMA_APIV3_TOKEN",
        "group_id": "KAMMA_PS_API_GROUP_ID",
    },
}
