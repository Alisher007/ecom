from django.urls import path
from . import views
from cart.views import ProductListView

app_name = 'main'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('profile/', views.ProfileView.as_view(), name='profile')
]
