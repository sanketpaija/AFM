from django.contrib import admin
from category.models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','status','image')
    list_filter=('status','created_at')
    search_fields=('name',)
    icon_name="call_split"

admin.site.register(Category,CategoryAdmin)