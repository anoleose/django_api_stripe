from django.urls import path
from items import views
from .views import DetailView, CheckoutView

app_name = 'items'

urlpatterns = [
	path('', views.list_item, name="list_item"),
	path('item/<int:id>/', views.detail_item, name="detail_item"),
	path('api/item/<int:id>/', DetailView.as_view(), name="detailview"),
	path('success', views.success, name="success"),
	path('cancel', views.cancel, name="cancel"),
	path('buy/<int:id>/', views.checkout, name="checkout"),
	path('api/buy/<int:id>/', CheckoutView.as_view(), name="checkoutview"),
	path('my_web_hook_view/', views.my_web_hook_view, name="my_web_hook_view")
]

