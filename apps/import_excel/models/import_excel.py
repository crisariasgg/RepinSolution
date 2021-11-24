"""PartsAuthority models."""


# Django
from django.db import models

class PartsAuthority(models.Model):
	id = models.BigAutoField('Id', primary_key=True)
	line = models.CharField('Line', max_length=100, blank=True, null=True)
	part = models.CharField('Part', max_length=100, blank=True, null=True)
	cost = models.CharField('Cost',max_length=100, blank=True,null=True)
	coreprice = models.CharField('Coreprice',max_length=100, blank=True,null=True)
	qtyonhand = models.CharField('Qtyonhand',max_length=100, blank=True, null=True)
	packs = models.CharField('Packs',max_length=100, null=True, blank=True)
	sku = models.CharField('SKU', max_length=100, blank=True, null=True)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.part
	

class Shopify(models.Model):
	id = models.BigAutoField('Id', primary_key=True)
	handle = models.CharField(max_length=200,blank=True,null=True)
	title = models.CharField(max_length=200,blank=True,null=True)
	bodyHTML = models.TextField('Body (HTML)',blank=True,null=True)
	vendor = models.CharField(max_length=200,blank=True,null=True)
	standard_product_type = models.CharField('Standard Product Type',max_length=200,blank=True,null=True)
	custom_product_type = models.CharField(max_length=200,blank=True,null=True)
	tags = models.CharField(max_length=200,blank=True,null=True)
	published = models.CharField(max_length=200,blank=True,null=True)
	option1_name = models.CharField(max_length=200,blank=True,null=True)
	option1_value = models.CharField(max_length=200,blank=True,null=True)
	option2_name = models.CharField(max_length=200,blank=True,null=True)
	option2_value = models.CharField(max_length=200,blank=True,null=True)
	option3_name = models.CharField(max_length=200,blank=True,null=True)
	option3_value = models.CharField(max_length=200,blank=True,null=True)
	variant_sku = models.CharField(max_length=200,blank=True,null=True)
	variant_grams = models.CharField(max_length=200,blank=True,null=True)
	variant_inventory_tracker = models.CharField(max_length=200,blank=True,null=True)
	variant_inventory_qty = models.CharField(max_length=200,blank=True,null=True)
	variant_inventory_policy = models.CharField(max_length=200,blank=True,null=True)
	variant_fulfillment_service = models.CharField(max_length=200,blank=True,null=True)
	variant_price = models.CharField(max_length=200,blank=True,null=True)
	variant_compare_at_price = models.CharField(max_length=200,blank=True,null=True)
	variant_requires_shipping = models.CharField(max_length=200,blank=True,null=True)
	variant_taxable = models.CharField(max_length=200,blank=True,null=True)
	variant_barcode = models.CharField(max_length=200,blank=True,null=True)
	image_src = models.CharField(max_length=500,blank=True,null=True)
	image_position = models.CharField(max_length=200,blank=True,null=True)
	image_alt_text = models.CharField(max_length=200,blank=True,null=True)
	gift_card = models.CharField(max_length=200,blank=True,null=True)
	seo_title = models.CharField(max_length=200,blank=True,null=True)
	seo_description = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_google_product_category = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_gender = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_age_group = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_MPN = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_adWords_grouping = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_adWords_labels = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_condition = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_custom_product = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_custom_label_0 = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_custom_label_1 = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_custom_label_2 = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_custom_label_3 = models.CharField(max_length=200,blank=True,null=True)
	google_shopping_custom_label_4 = models.CharField(max_length=200,blank=True,null=True)
	variant_image = models.CharField(max_length=200,blank=True,null=True)
	variant_weight_unit = models.CharField(max_length=200,blank=True,null=True)
	variant_tax_code = models.CharField(max_length=200,blank=True,null=True)
	cost_per_item = models.CharField(max_length=200,blank=True,null=True)
	status = models.CharField(max_length=200,blank=True,null=True)
	date = models.DateField(auto_now_add=True)
	record_status = models.CharField(max_length=200,blank=True,null=True)

	def __str__(self):
		return str(self.variant_sku)