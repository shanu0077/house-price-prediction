from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "accounts"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'), 
    path('logout/', views.logout_user, name='logout'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    path('admin/', views.admin,name='admin'),
    path('appartment/', views.appartment,name='appartment'),
    path('register/', views.register_type, name='register_type'),
    path('register/normal_user/', views.register_normal_user, name='register_normal_user'),
    path('register/hotel_owner/', views.register_hotel_owner, name='register_hotel'),
    path('normal_user_home/', views.normal_user_home, name='normal_user_home'),
    path('hotel_owner_home/', views.hotel_owner_home, name='hotel_owner_home'),
    path('cab_driver_home/', views.cab_driver_home, name='cab_driver_home'),
    path('appartments/', views.appartments, name='appartments'),
    path('appartment_user_view/', views.appartment_user_view, name='appartment_user_view'),
    path('all_users/', views.all_users, name='all_users'),
    path('booking/<str:name>', views.booking, name='booking'),
    path('edit/<str:name>', views.edit, name='edit'),
    path('editbtn/<str:name>', views.editbtn, name='editbtn'),
    path('payment/', views.payment, name='payment'),
    path('search/', views.search, name='search'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
