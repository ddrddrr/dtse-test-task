from house_prices.settings.base import *


REST_FRAMEWORK = REST_FRAMEWORK | {
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "50/day", "user": "100/min"},
}

SPECTACULAR_SETTINGS = SPECTACULAR_SETTINGS | {
    "ENABLE_DJANGO_DEPLOY_CHECK": True,
}
