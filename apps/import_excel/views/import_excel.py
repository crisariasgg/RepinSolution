""" User's Views """

# Django
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from django.shortcuts import render


#Third party
from tablib import Dataset


# local Django
User = get_user_model()
from apps.import_excel.resources import PartsAuthorityResource,ShopifyResource


class ImportExcelView(TemplateView):
	template_name = 'import_excel.html'
	paginate_by = 5
				
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = User.objects.get(pk=self.request.user.pk)
		context.update({
			'user': user,
		})
		return context
	
	def post(self, request):
		
		excel_resource = ExcelResource()
		dataset = Dataset()
		new_persons = request.FILES['myfile']

		imported_data = dataset.load(new_persons.read())
		result = excel_resource.import_data(dataset, dry_run=True)  # Test the data import

		if not result.has_errors():
			excel_resource.import_data(dataset, dry_run=False)  # Actually import now

		return render(request, 'core/simple_upload.html')