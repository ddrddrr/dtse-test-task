import datetime
from email.policy import default
from pathlib import Path

from decouple import AutoConfig, Csv

BASE_DIR = Path(__file__).resolve().parent.parent  # django project root dir
ROOT_DIR = BASE_DIR.parent  # repo root dir

config = AutoConfig(search_path=ROOT_DIR)  # looks for env in ROOT_DIR

DJANGO_BASE_URL = config("DJANGO_BASE_URL", default="http://localhost:8000")

SECRET_KEY = config("SECRET_KEY", default="<SECRET_KEY>")

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS", default="localhost,127.0.0.1", cast=Csv()
)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party
    "rest_framework",
    "knox",
    # Local
    "users.apps.UsersConfig",
    "predictor.apps.PredictorConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "house_prices.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "house_prices.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# REST
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "knox.auth.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}


TOKEN_TTL_HOURS = config(
    "TOKEN_TTL_HOURS",
    default="1",
    cast=float,
)
REST_KNOX = {
    "TOKEN_TTL": datetime.timedelta(hours=TOKEN_TTL_HOURS),
    "AUTO_REFRESH": False,
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Users

AUTH_USER_MODEL = "users.BaseUser"


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Model
MODEL_PATH = config(
    "MODEL_PATH", default="/Users/mazda/job_stuff/dtse-test-task/model/model.joblib"
)
FEATURES_PATH = config(
    "FEATURES_PATH", default="/Users/mazda/job_stuff/dtse-test-task/model/features.json"
)
