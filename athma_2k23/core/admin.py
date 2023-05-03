from django.contrib import admin
from .models import Profiles, Events, SpecialEvents, About, Teams

# Register your models here.

admin.site.register(Profiles)
admin.site.register(Events)
admin.site.register(SpecialEvents)
admin.site.register(About)
admin.site.register(Teams)