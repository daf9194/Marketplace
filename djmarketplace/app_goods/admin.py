from django.contrib import admin
from app_goods.models import Good, Store

class GoodAdmin(admin.ModelAdmin):
    list_display = ['good_name','price', 'amount']

class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_name']


admin.site.register(Good, GoodAdmin)
admin.site.register(Store, StoreAdmin)