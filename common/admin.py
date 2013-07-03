from django.contrib import admin
from common.models import Navigation

class NavigationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Navigation, NavigationAdmin)