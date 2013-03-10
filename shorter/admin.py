# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'short_version', 'pub_date']
    list_filter = ['pub_date']
    ordering = ['url', 'short_version', 'pub_date']
    readonly_fields = ['short_version']
    search_fields = ['url', 'short_version', 'pub_date']
    date_hierarchy = 'pub_date'
    fieldsets = [
        (None,
        {'fields': ['url', 'short_version']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]


admin.site.register(Url, UrlAdmin)
