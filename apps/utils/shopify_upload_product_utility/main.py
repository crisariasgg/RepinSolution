"""This module shows a menu with 4 options"""

from typing import Dict
from apps.utils.shopify_upload_product_utility.test.testing import *
from apps.utils.shopify_upload_product_utility.main import *
from apps.utils.shopify_upload_product_utility.FTPutil import FTPConnection,DownloadFromFTP
from apps.utils.shopify_upload_product_utility.import_partspal import PartsPalImport

from django.db.models import F,Q,Count
import datetime
from apps.import_excel.models import *


from apps.import_excel.resources import ShopifyResource
from apps.import_excel.models import Shopify

import numpy as np
import pandas as pd


__author__ = "Cris Arias"
__copyright__ = "Copyright 2020"
__credits__ = ["Cris Arias"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Cris Arias"
__email__ = "ariasover@gmail.com"
__status__ = "Production"

# FTP credentials
FTP_HOST = "ftp.panetny.com"
FTP_USER = "repuestospf"
FTP_PASS = "RN2xh5mb"

# Database credentials
NAME='ShopifyImport'
USER = 'root'
PASSWORD = 'Minimalista1'
HOST = 'localhost'
PORT = 3306

headers = [
"Handle",
"Title",
"Body (HTML)",
"Vendor",
"Standard Product Type",
"Custom Product Type",
"Tags",
"Published",
"Option1 Name",
"Option1 Value",
"Option2 Name",
"Option2 Value",
"Option3 Name",
"Option3 Value",
"Variant SKU",
"Variant Grams",
"Variant Inventory Tracker",
"Variant Inventory Qty",
"Variant Inventory Policy",
"Variant Fulfillment Service",
"Variant Price",
"Variant Compare At Price",
"Variant Requires Shipping",
"Variant Taxable",
"Variant Barcode",
"Image Src",
"Image Position",
"Image Alt Text",
"Gift Card",
"SEO Title",
"SEO Description",
"Google Shopping / Google Product Category",
"Google Shopping / Gender",
"Google Shopping / Age Group",
"Google Shopping / MPN",
"Google Shopping / AdWords Grouping",
"Google Shopping / AdWords Labels",
"Google Shopping / Condition",
"Google Shopping / Custom Product",
"Google Shopping / Custom Label 0",
"Google Shopping / Custom Label 1",
"Google Shopping / Custom Label 2",
"Google Shopping / Custom Label 3",
"Google Shopping / Custom Label 4",
"Variant Image",
"Variant Weight Unit",
"Variant Tax Code",
"Cost per item",
"Status"]

HEADERS = ','.join(headers)
TODAY_DATE=datetime.date.today()

def menu():
	answer=True
	while answer:
		print("""
			1.Download file from server and unzip. 📁
			2.Import partsauthority.csv file to database. ⬆️
			3.Export shopify csv. 📝 
			4.Exit/Quit 😊
			"""
		)
		option=str(input("What would you like to do?: "))

		if option == "1":

			connection = FTPConnection(FTP_HOST,FTP_USER,FTP_PASS)
			DownloadFromFTP('partsauthority.zip',connection.connection_results)


		elif option == "2":
			import time
			start_time = time.time()
			import_partspal_data()
			print("--- %s seconds ---" % (time.time() - start_time))

		elif option =="3":
			
			import time
			start_time = time.time()
			export()
			print("--- %s seconds ---" % (time.time() - start_time))

		elif option =="4":
				
			print("Goodbye!")
			break


		else:
			pass


def show_menu():
	menu()

# Clean 
def clean_duplicated_data(date):
		
	duplicates = PartsAuthority.objects.values(
	'part'
	).annotate(part_count=Count('part')).filter(date=TODAY_DATE+datetime.timedelta(days=date),part_count__gt=1)

	records = PartsAuthority.objects.filter(part__in=[item['part'] for item in duplicates])


	# [item.part for item in records]
	return records

# IMPORT DATA
def yesterday_shopify_first_import():
	data = PartsAuthority.objects.filter(date=TODAY_DATE).exists()
	if not data:

		connection = PartsPalImport(NAME,USER,HOST,PORT,PASSWORD)
		csv_data = connection.read_input_file('BD_02.csv')
		csv_data = connection.insert_date_to_column(csv_data,day=-1)
		connection.import_to_sql(csv_data,connection.connection_results)

	else:
		print('ya existe data con fecha de hoy')	
		
def import_today_partsauthority_data():
	data = PartsAuthority.objects.filter(date=TODAY_DATE).exists()
	if not data:

		# Yesterday data
		connection = PartsPalImport(NAME,USER,HOST,PORT,PASSWORD)
		yesterday_data = connection.read_input_file('partsauthority.csv')
		yesterday_data = connection.insert_date_to_column(yesterday_data,day=0)
		connection.import_to_sql(yesterday_data,connection.connection_results)

	else:
		print('ya existe data con fecha de hoy')


# SEARCHING
def search_new_parts():
	
	yesterday_data = PartsAuthority.objects.filter(date=TODAY_DATE+datetime.timedelta(days=-1)).values_list('part',flat=True)
	today_data = PartsAuthority.objects.filter(date=TODAY_DATE).values_list('part',flat=True) 
	differences  = list(set(today_data) - set(yesterday_data))
	new_parts = PartsAuthority.objects.filter(date=TODAY_DATE,part__in=differences)

	# TODO VERIFICAR SI EXISTEN ESTAS PARTES EN SHOPIFY
	return new_parts

def search_differences_in_cost():
	# MATCH
	# yesterday_data = PartsAuthority.objects.filter(date=TODAY_DATE+datetime.timedelta(days=-1)).values_list('part',flat=True)
	# today_data = PartsAuthority.objects.filter(date=TODAY_DATE).values_list('part',flat=True) 
	# yesterday_data = list(PartsAuthority.objects.filter(date=TODAY_DATE+datetime.timedelta(days=-1)).values_list('part','cost'))
	# today_data = PartsAuthority.objects.filter(date=TODAY_DATE).values_list('part',flat=True) 
	# matches  = list(set(today_data) & set(yesterday_data))
	# new_cost = PartsAuthority.objects.filter(part__in=matches).exclude(date = TODAY_DATE+datetime.timedelta(days=-1))


	queryset = PartsAuthority.objects.values(
	'part'
	).annotate(part_count=Count('part'),cost_count=Count('cost')).filter(date__in=[TODAY_DATE+datetime.timedelta(days=-1),TODAY_DATE],part_count__gt=1)

	duplicated=[item['part'] for item in queryset]

	new_cost = PartsAuthority.objects.filter(part__in=duplicated).exclude(date=TODAY_DATE+datetime.timedelta(days=-1))

	return new_cost

def search_differences_in_qty():
	yesterday_data = PartsAuthority.objects.filter(date=TODAY_DATE+datetime.timedelta(days=-1))
	today_data = PartsAuthority.objects.filter(date=TODAY_DATE)

	today_sku = []
	today_qty = []
	for x in today_data:
		today_sku.append(x.part)
		today_qty.append(x.qtyonhand)

	new_qty = yesterday_data.exclude(part__in=today_sku,qtyonhand__in=today_qty)

	ultimate_sku = []
	for x in new_qty:
		ultimate_sku.append(x.part)
		
	new_qty = today_data.filter(part__in=ultimate_sku)

	return new_qty

def search_deleted_parts():
	# yesterday_data = PartsAuthority.objects.filter(date=TODAY_DATE+datetime.timedelta(days=-1)).values_list('part')
	# today_data = PartsAuthority.objects.filter(date=TODAY_DATE).values_list('part')

	# all_parts=[]

	# for x in today_data:
	# 	all_parts.append(x.part)
	# deleted_data = yesterday_data.exclude(part__in=all_parts)

	# return deleted_data

	yesterday_data = PartsAuthority.objects.filter(date=TODAY_DATE+datetime.timedelta(days=-1)).values_list('part',flat=True)
	today_data = PartsAuthority.objects.filter(date=TODAY_DATE).values_list('part',flat=True) 
	differences  = list(set(yesterday_data) & set(today_data))
	deleted_parts = PartsAuthority.objects.exclude(part__in=differences)
	return deleted_parts

# ADD TO SHOPIFY


def add_parts_to_shopify():
	# VERIFICAR SI LA DATA OBTENIDA ESTÁ EN SHOPIFY
	import time
	start_time = time.time()
	new_parts = search_new_parts()

	Shopify.objects.filter(variant_sku__in=new_parts)
	if new_parts.exists():
		for record in new_parts:	
			p = Shopify.objects.create(variant_price=record.cost,variant_sku=record.part,status="active",record_status='new_part')
			p.save()
		for x in new_parts:
			print('New part added: SKU ',x,' ✅')

	print("--- %s seconds ---" % (time.time() - start_time))		

def add_new_costs_to_shopify():
	partspal_costs = search_differences_in_cost()
	# shopify_parts = Shopify.objects.filter(record_status='new_cost')

	# shopify_costs_array=[]
	# for x in shopify_parts:
	# 	shopify_costs_array.append(x.variant_sku)

	# existing_costs = partspal_costs.exclude(part__in=shopify_costs_array)

	if partspal_costs:
		for record in partspal_costs[:100]:	
			Shopify.objects.create(variant_price=record.cost,variant_sku=record.part,status="active",record_status='new_cost')
		for x in partspal_costs:
			print('New cost added: SKU ',x,' ✅')
	else:
		print('no se crearan nuevos costos')

def add_new_qty_to_shopify():
	partspal_qty = search_differences_in_qty()
	shopify_parts = Shopify.objects.filter(record_status='new_qty')

	shopify_qty_array=[]
	for x in shopify_parts:
		shopify_qty_array.append(x.variant_sku)

	existing_qty = partspal_qty.exclude(part__in=shopify_qty_array)

	if existing_qty:
		for record in existing_qty:	
			Shopify.objects.create(variant_price=record.cost,variant_sku=record.part,status="active",record_status='new_qty')
		for x in existing_qty:
			print('New QTY added: SKU ',x,' ✅')
	else:
		print('no se crearan nuevos costos')

def add_deleted_parts_to_shopify():
	partspal_deleted = search_deleted_parts()


	partspal_deleted_array=[]
	for x in partspal_deleted:
		partspal_deleted_array.append(x.part)


	# BUSCAR SI EXISTE EN SHOPIFY
	verify_if_exist_in_shopify = Shopify.objects.filter(variant_sku__in=partspal_deleted_array,record_status='deleted')

	if not verify_if_exist_in_shopify:
		for record in partspal_deleted:	
			Shopify.objects.create(variant_sku=record.part,status="draft",record_status='deleted')
		
		print('New deleted parts added!: ')
		for x in partspal_deleted:
			print('SKU ',x,'✅')
	else:
		print('no se han borrado partes')


# EXPORT
def export_today_all():
    	
	queryset = Shopify.objects.filter(date=TODAY_DATE)
	data_export = ShopifyResource().export(queryset)
	np.savetxt("all_data.csv", data_export, delimiter=",", comments='',fmt='%s',header=HEADERS)

def export_new_parts():
	queryset = Shopify.objects.filter(status='active',date=TODAY_DATE,record_status='new_part')
	data_export = ShopifyResource().export(queryset)
	np.savetxt("new_parts.csv", data_export, delimiter=",", comments='',fmt='%s',header=HEADERS)

def export_new_qty():
	queryset = Shopify.objects.filter(status='active',date=TODAY_DATE,record_status='new_qty')
	data_export = ShopifyResource().export(queryset)
	np.savetxt("new_qty.csv", data_export, delimiter=",", comments='',fmt='%s',header=HEADERS)

def export_new_costs():
	queryset = Shopify.objects.filter(status='active',date=TODAY_DATE,record_status='new_cost')
	data_export = ShopifyResource().export(queryset)
	np.savetxt("new_costs.csv", data_export, delimiter=",", comments='',fmt='%s',header=HEADERS)

def export_deleted_parts():
	queryset = Shopify.objects.filter(status='draft',date=TODAY_DATE,record_status='deleted')
	data_export = ShopifyResource().export(queryset)
	np.savetxt("new_costs.csv", data_export, delimiter=",", comments='',fmt='%s',header=HEADERS)

# METODOS de control
def add_new_part():
	sku = str(input('Add part SKU: '))
	cost = str(input('Add part Cost: '))
	PartsAuthority.objects.create(line = 'A1', part = sku,cost = cost,coreprice= '0',qtyonhand = '5',packs = '1')


if __name__ == "__main__":
	show_menu()
	
		