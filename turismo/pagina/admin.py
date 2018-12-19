from django.contrib import admin
from core.admin import admin_general
from . import models


@admin.register(models.FeedBack, site=admin_general)
class FeedBackAdmin(admin.ModelAdmin):
    pass