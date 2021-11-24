"""Circles URLs."""

# Django
from django.urls import path


# Views
from .views.import_excel import *

urlpatterns = [
    path('import/',ImportExcelView.as_view(),name="import_excel"),    
]