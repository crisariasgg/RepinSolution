"""This module shows a menu with 4 options"""

from apps.utils.shopify_upload_product_utility.main import *
from apps.utils.shopify_upload_product_utility.FTPutil import FTPConnection,DownloadFromFTP
from apps.utils.shopify_upload_product_utility.import_partspal import PartsPalImport

from django.db.models import Q

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

def test_menu():
	answer=True
	while answer:
		print("""

			1.Clean database ⬆️
			2.Import partsauthority.csv file to database. ⬆️
			3.Search parts/costs and deleted data 🔍
			4.Add new part +
			5.Update record with new cost 📝 
			6.Export to shopify.csv. 📝 
			7.Export all today data. 📝 
			8.Exit 😊
			"""
		)
		option=str(input("What would you like to do?: "))

		if option == "1":
	
			test_clean_database_tables()

		if option == "2":

			test_import_partspal_data()

		elif option == "3":

			test_search_differences_in_parts()
			test_search_differences_in_cost()
			test_search_deleted_parts()


		elif option =="4":
			
			test_add_new_part()	


		elif option =="5":
	
			test_update_one_record_cost()

		elif option =="6":
				
			test_export_new_data_to_csv()

		elif option =="7":
				
			test_export_all()

		elif option =="8":
			print("Goodbye!")
			break

		else:
			pass


def test_show_menu():
	menu()

def test_clean_duplicated_data():
    pass

def test_clean_database_tables():
	PartsAuthority.objects.filter().delete()
	Shopify.objects.filter().delete()
	

def test_import_partspal_data():
	print('Inserting test data...')
	TODAY_DATE=datetime.date.today()
	data = PartsAuthority.objects.filter(date=TODAY_DATE).exists()
	if not data:
		# Add data

		# Yesterday data
		connection = PartsPalImport(NAME,USER,HOST,PORT,PASSWORD)
		yesterday_data = connection.read_input_file('partsauthority_test_data.csv')
		yesterday_data = connection.insert_date_to_column(yesterday_data,day=-1)
		connection.import_to_sql(yesterday_data,connection.connection_results)

		# Today data
		today_data = connection.read_input_file('partsauthority_test_data.csv')
		today_data = connection.insert_date_to_column(today_data,day=0)
		connection.import_to_sql(today_data,connection.connection_results)

	else:
		print('ya existe data con fecha de hoy')


def test_search_differences_in_parts():
	TODAY_DATE=datetime.date.today()
			
	yesterday_data = PartsAuthority.objects.filter(date=TODAY_DATE+datetime.timedelta(days=-1))
	today_data = PartsAuthority.objects.filter(date=TODAY_DATE) 


	all_parts=[]
	for x in yesterday_data:
		all_parts.append(x.part)
	differences = today_data.exclude(part__in=all_parts)
	
	if differences:
		print('data is ready!, differences: ')
		for x in differences:
			print('SKU ',x,' ✅')

	else:
		print("There's no new part")
	return differences


def test_search_differences_in_cost():

	TODAY_DATE=datetime.date.today()
			
	yesterday_data = PartsAuthority.objects.filter(date=TODAY_DATE+datetime.timedelta(days=-1))
	today_data = PartsAuthority.objects.filter(date=TODAY_DATE)

	# verificar si el sku existe en la data de ayer
	
	today_sku = []
	today_cost = []
	for x in today_data:
		today_sku.append(x.part)
		today_cost.append(x.cost)

	new_cost = yesterday_data.exclude(part__in=today_sku,cost__in=today_cost)


	ultimate_sku = []
	for x in new_cost:
		ultimate_sku.append(x.part)
		
	new_cost = today_data.filter(part__in=ultimate_sku)

	# all_cost=[]

	# for x in yesterday_data:
	# 	if x.cost == 
	# 	all_cost.append(x.cost)
	# differences = today_data.exclude(cost__in=all_cost)


	if new_cost:
		print('data is ready!, differences: ')
		for x in new_cost:
			print('SKU ',x,'NEW COST',x.cost, '✅')

	else:
		print("There's no new costs")
	return new_cost


def test_search_deleted_parts():			
	yesterday_data = PartsAuthority.objects.filter(date=TODAY_DATE+datetime.timedelta(days=-1))
	today_data = PartsAuthority.objects.filter(date=TODAY_DATE)

	all_parts=[]

	for x in today_data:
		all_parts.append(x.part)
	deleted_data = yesterday_data.exclude(part__in=all_parts)
		
	if deleted_data:
		print('New deleted parts found!: ')
		for x in deleted_data:
			print('SKU ',x,'✅')
	else:
		print("There's no deleted data")
	return deleted_data


def test_add_new_part():
	sku = str(input('Add part SKU: '))
	cost = str(input('Add part Cost: '))
	PartsAuthority.objects.create(line = 'A1', part = sku,cost = cost,coreprice= '0',qtyonhand = '5',packs = '1')


def test_update_one_record_cost():
	
	q=PartsAuthority.objects.filter(date = datetime.date.today()).first()
	q.cost=5000
	q.save()


def test_export_new_data_to_csv():
	# EXPORTAR LAS PARTES NUEVAS
	partspal_parts = test_search_differences_in_parts()
	shopify_parts = Shopify.objects.filter()

	shopify_parts_array=[]
	for x in shopify_parts:
		shopify_parts_array.append(x.variant_sku)

	existing_parts = partspal_parts.exclude(part__in=shopify_parts_array)

	if existing_parts:
		for record in existing_parts:	
			p = Shopify.objects.create(variant_price=record.cost,variant_sku=record.part,status="active",record_status='new_part')
			p.save()

		queryset = Shopify.objects.filter(status='active',date=TODAY_DATE,record_status='new_part')
		data_export = ShopifyResource().export(queryset)
		np.savetxt("new_parts.csv", data_export, delimiter=",", comments='',fmt='%s',header=HEADERS)
		
	else:
		print('no se crearan nuevas partes')

	# EXPORTAR LOS COSTOS NUEVOS	
	partspal_costs = test_search_differences_in_cost()
	shopify_parts = Shopify.objects.filter(record_status='new_cost')

	shopify_costs_array=[]
	for x in shopify_parts:
		shopify_costs_array.append(x.variant_sku)

	existing_costs = partspal_costs.exclude(part__in=shopify_costs_array)

	if existing_costs:
		for record in existing_costs:	
			Shopify.objects.create(variant_price=record.cost,variant_sku=record.part,status="active",record_status='new_cost')

		queryset = Shopify.objects.filter(status='active',date=TODAY_DATE,record_status='new_cost')
		data_export = ShopifyResource().export(queryset)
		np.savetxt("new_costs.csv", data_export, delimiter=",", comments='',fmt='%s',header=HEADERS)
		
	else:
		print('no se crearan nuevos costos')

	# EXPORTAR PARTES ELIMINADAS

	partspal_deleted = test_search_deleted_parts()


	partspal_deleted_array=[]
	for x in partspal_deleted:
		partspal_deleted_array.append(x.part)


	# BUSCAR SI EXISTE EN SHOPIFY
	verify_if_exist_in_shopify = Shopify.objects.filter(variant_sku__in=partspal_deleted_array,record_status='deleted')

	if not verify_if_exist_in_shopify:
		for record in partspal_deleted:	
			Shopify.objects.create(variant_sku=record.part,status="draft",record_status='deleted')

	else:
		print('no se han borrado partes')
	

def test_export_all():
		
	queryset = Shopify.objects.filter(Q(status='active')|Q(status='draft'),date=TODAY_DATE)
	data_export = ShopifyResource().export(queryset)
	np.savetxt("all_export.csv", data_export, delimiter=",", comments='',fmt='%s',header=HEADERS)

	
	

if __name__ == "__main__":
	test_show_menu()
	
		