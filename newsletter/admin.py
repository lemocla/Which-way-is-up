from django.contrib import admin
from .models import Mailing


class MailingAdmin(admin.ModelAdmin):
    """
    Admin model to display mailing list
    Display field email
    """
    model = Mailing
    list_display = (
        "email",
    )

admin.site.register(Mailing, MailingAdmin)