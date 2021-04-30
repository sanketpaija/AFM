from django.contrib import admin
from .models import Restaurent
# Register your models here.


class RestaurentAdmin(admin.ModelAdmin):
    list_display=('name','image','city','zip','status','created_at','updated_at')
    list_filter=('zip','city','created_at')
    search_fields=('name','city','zip')
    icon_name="restaurant"

admin.site.register(Restaurent,RestaurentAdmin)
