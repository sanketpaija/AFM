from django.contrib import admin
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=('item','qty','user')
    list_filter=('user','created_at')
    search_fields=('item__name',)
    icon_name = 'shopping_cart'

admin.site.register(Cart,CartAdmin)