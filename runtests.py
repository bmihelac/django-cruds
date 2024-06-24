import sys

from django.conf import settings
from django.test.runner import DiscoverRunner


settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
        }
    },
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sites",
        "cruds",
        "tests.testapp",
    ],
    SITE_ID=1,
    ROOT_URLCONF="tests.testapp.urls",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {},
        },
    ],
    SECRET_KEY="secret-key",
)

try:
    import django

    setup = django.setup
except AttributeError:
    pass
else:
    setup()


def run_tests(*test_args):
    if not test_args:
        test_args = ["tests"]

    # Run tests
    test_runner = DiscoverRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == "__main__":
    run_tests(*sys.argv[1:])
