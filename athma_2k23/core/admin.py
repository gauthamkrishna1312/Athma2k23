from django.contrib import admin
from .models import Profiles, Events, SpecialEvents

# Register your models here.

admin.site.register(Profiles)
admin.site.register(Events)
admin.site.register(SpecialEvents)