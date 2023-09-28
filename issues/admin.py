from django.contrib import admin
from .models import Issue


class IssueAdmin(admin.ModelAdmin):
    model = Issue

    list_display = [
        "summary",
        "description",
        "reporter",
        "status"
    ]


admin.site.register(Issue, IssueAdmin)
