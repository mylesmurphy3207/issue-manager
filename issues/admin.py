from django.contrib import admin
from .models import Status, Issue


admin.site.register([Status, Issue])

# Register your models here.
