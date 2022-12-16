from django.contrib import admin
from .models import Redirect

# Register your models here.


@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    list_display = ('_key', '_url',
                    '_created_date', '_modified_date', '_active',)
    list_filter = ('_created_date', '_modified_date', '_active',)

    readonly_fields = ('_created_date', '_modified_date')
    pass
