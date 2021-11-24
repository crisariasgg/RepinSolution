# app/admin.py

from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin


from apps.import_excel.models import PartsAuthority,Shopify

class PartsAuthorityResource(resources.ModelResource):
	
	class Meta:
		model = PartsAuthority

class ShopifyResource(resources.ModelResource):
	handle = Field(attribute='handle', column_name='Handle')
	bodyHTML = Field(attribute='bodyHTML', column_name='Body (HTML)')
	title = Field(attribute='title', column_name='Title')
	vendor = Field(attribute='vendor',column_name="Vendor")
	standard_product_type = Field(attribute='standard_product_type',column_name="Standard Product Type")
	custom_product_type = Field(attribute='custom_product_type',column_name="Custom Product Type")
	tags = Field(attribute='tags',column_name="Tags")
	published = Field(attribute='published',column_name="Published")
	option1_name = Field(attribute='option1_name',column_name="Option 1 Name")
	option1_value = Field(attribute='option1_value',column_name="Option 1 Value")
	option2_name = Field(attribute='option2_name',column_name="Option 2 Name")
	option2_value = Field(attribute='option2_value',column_name="Option 2 Value")
	option3_name = Field(attribute='option3_name',column_name="Option 3 Name")
	option3_value = Field(attribute='option3_value',column_name="Option 3 Value")
	variant_sku = Field(attribute='variant_sku',column_name="Variant SKU")
	variant_grams = Field(attribute='variant_grams',column_name="Variant Grams")
	variant_inventory_tracker = Field(attribute='variant_inventory_tracker',column_name="Variant Inventory Tracker")
	variant_inventory_qty = Field(attribute='variant_inventory_qty',column_name="Variant Inventory Qty")
	variant_inventory_policy = Field(attribute='variant_inventory_policy',column_name="Variant Inventory Policy")
	variant_fulfillment_service = Field(attribute='variant_fulfillment_service',column_name="Variant Fulfillment Service")
	variant_price = Field(attribute='variant_price',column_name="Variant Price")
	variant_compare_at_price = Field(attribute='variant_compare_at_price',column_name="Variant Compare At Price")
	variant_requires_shipping = Field(attribute='variant_requires_shipping',column_name="Variant Requires Shipping")
	variant_taxable = Field(attribute='variant_taxable',column_name="Variant Taxable")
	variant_barcode = Field(attribute='variant_barcode',column_name="Variant Barcode")
	image_src = Field(attribute='image_src',column_name="Image Src")
	image_position = Field(attribute='image_position',column_name="Image Position")
	image_alt_text = Field(attribute='image_alt_text',column_name="Image Alt Text")
	gift_card = Field(attribute='gift_card',column_name="Gift Card")
	seo_title = Field(attribute='seo_title',column_name="SEO Title")
	seo_description = Field(attribute='seo_description',column_name="SEO Description")
	google_shopping_google_product_category = Field(attribute='google_shopping_google_product_category',column_name="Google Shopping / Google Product Category")
	google_shopping_gender = Field(attribute='google_shopping_gender',column_name="Google Shopping / Gender")
	google_shopping_age_group = Field(attribute='google_shopping_age_group',column_name="Google Shopping Age Group")
	google_shopping_MPN = Field(attribute='google_shopping_MPN',column_name="Google Shopping MPN")
	google_shopping_adWords_grouping = Field(attribute='google_shopping_adWords_grouping',column_name="Google Shopping AdWords Grouping")
	google_shopping_adWords_labels = Field(attribute='google_shopping_adWords_labels',column_name="Google Shopping AdWords Labels")
	google_shopping_condition = Field(attribute='google_shopping_condition',column_name="Google Shopping Condition")
	google_shopping_custom_product = Field(attribute='google_shopping_custom_product',column_name="Google Shopping Custom Product")
	google_shopping_custom_label_0 = Field(attribute='google_shopping_custom_label_0',column_name="Google Shopping Custom Label 0")
	google_shopping_custom_label_1 = Field(attribute='google_shopping_custom_label_1',column_name="Google Shopping Custom Label 1")
	google_shopping_custom_label_2 = Field(attribute='google_shopping_custom_label_2',column_name="Google Shopping Custom Label 2")
	google_shopping_custom_label_3 = Field(attribute='google_shopping_custom_label_3',column_name="Google Shopping Custom Label 3")
	google_shopping_custom_label_4 = Field(attribute='google_shopping_custom_label_4',column_name="Google Shopping Custom Label 4")
	variant_image = Field(attribute='variant_image',column_name="Variant Image")
	variant_weight_unit = Field(attribute='variant_weight_unit',column_name="Variant Weight Unit")
	variant_tax_code = Field(attribute='variant_tax_code',column_name="Variant Tax Code")
	cost_per_item = Field(attribute='cost_per_item',column_name="Cost per item")
	status = Field(attribute='status',column_name="Status")
	class Meta:
		model = Shopify
		export_order = (
		'handle', 
		)
		exclude=('id','date')
	
	

