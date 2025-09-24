from django.urls import path
from . import views
from .views import ItemUnitsListView

urlpatterns = [
	path('api/get/', views.ItemUnitsListView.as_view(), name='ItemUnits-list'),
	path('api/post/', views.ItemUnitsCreateView.as_view(), name='ItemUnits-create')
]