from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from apps.import_excel.models import PartsAuthority,Shopify
from apps.import_excel.resources import ShopifyResource




class PartsAuthorityAdmin(ImportExportModelAdmin):
	pass

class ShopifyAdmin(ImportExportModelAdmin):
	resource_class = ShopifyResource

admin.site.register(Shopify,ShopifyAdmin)
	
		

