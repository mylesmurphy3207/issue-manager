











from pathlib import pathlib


BASE_DIR = Path(__file__).resolve().parent.parent






SECRET_KEY = "django-insecure-z(zawfn3qc1++5rmyd@j5oe^57m&!n5bg3&0n5lie9ri(zqc63"


DEBUG = True

ALLOWED_HOSTS = []




INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",  
    "issues",
    "pages",
]