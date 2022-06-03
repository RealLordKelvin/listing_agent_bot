from django.contrib import admin

from .models import User, Listing

admin.site.register(Listing)
admin.site.register(User)
