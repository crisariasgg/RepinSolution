# Local imports
import datetime


# Third party 
import pandas as pd
import pymysql
from sqlalchemy import create_engine

class ShopifyImport():
	
	def __init__(self,name,user,host,port,password):
	
		self.user = user
		self.password = password
		self.host = host
		self.port = port 
		self.name = name
		self.connection_results = self.connection_to_db(self.name,self.user,self.host,self.port,self.password)


	def connection_to_db(self,name,user,host,port,password):
		connection_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(user, password, host, port, name)
		try:
			print('establishing connection...')
			connection = create_engine(connection_string)
			connection.connect()
		except Exception:
			raise("Error, can't establishing connection...")
		else:
			print ('No exception occurred')
		return connection


	def clean_csv_titles(self,data):
		new_data = data.rename(columns = {
			'Body (HTML)': 'BodyHTML',
			'Standard Product Type': 'standard_product_type',
			'Custom Product Type': 'custom_product_type',
			'Option1 Name': 'option1_name',
			'Option1 Value': 'option1_value',
			'Option2 Name': 'option2_name',
			'Option2 Value': 'option2_value',
			'Option3 Name': 'option3_name',
			'Option3 Value': 'option3_value',
			'Variant SKU': 'variant_sku',
			'Variant Grams': 'variant_grams',
			'Variant Inventory Tracker': 'variant_inventory_tracker',
			'Variant Inventory Qty': 'variant_inventory_qty',
			'Variant Inventory Policy': 'variant_inventory_policy',
			'Variant Fulfillment Service': 'variant_fulfillment_service',
			'Variant Price': 'variant_price',
			'Variant Compare At Price': 'variant_compare_at_price',
			'Variant Requires Shipping':'variant_requires_shipping',
			'Variant Taxable':'variant_taxable',
			'Variant Barcode':'variant_barcode',
			'Image Src':'image_src',
			'Image Position':'image_position',
			'Image Alt Text':'image_alt_text',
			'Gift Card':'gift_card',
			'SEO Title':'seo_title',
			'SEO Description':'seo_description',
			'Google Shopping / Google Product Category':'google_shopping_google_product_category',
			'Google Shopping / Gender':'google_shopping_gender',
			'Google Shopping / Age Group':'google_shopping_age_group',
			'Google Shopping / MPN':'google_shopping_MPN',
			'Google Shopping / AdWords Grouping':'google_shopping_adWords_grouping',
			'Google Shopping / AdWords Labels':'google_shopping_adWords_labels',
			
			
			'Google Shopping / Condition':'google_shopping_condition',
			'Google Shopping / Custom Product':'google_shopping_custom_product',
			'Google Shopping / Custom Label 0':'google_shopping_custom_label_0',
			'Google Shopping / Custom Label 1':'google_shopping_custom_label_1',
			'Google Shopping / Custom Label 2':'google_shopping_custom_label_2',
			'Google Shopping / Custom Label 3':'google_shopping_custom_label_3',
			'Google Shopping / Custom Label 4':'google_shopping_custom_label_4',

			'Variant Image': 'variant_image',
			'Variant Weight Unit': 'variant_weight_unit',
			'Variant Tax Code': 'variant_tax_code',
			'Cost per item':'cost_per_item'
			}, 
		inplace = False
		)
		return new_data

   
	def read_input_file(self,file_name):
		data=pd.read_csv(file_name)
		return data


	def import_to_sql(self,data,connection):
		data.to_sql(name='import_excel_shopify', con=connection, if_exists = 'append', index=False)
