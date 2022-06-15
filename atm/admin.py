from django.contrib import admin

from atm.models import Card, Account

admin.site.register([Card, Account])
