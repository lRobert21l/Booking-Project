from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('home/',views.home, name='home'),
    path('login/',views.log_in, name='login'),
    path('logout/',views.log_out, name='logout'),
    path('sign-up/',views.sign_up, name='sign-up'),
    path('blog/', views.destinations, name='destinations'),
    path('search/', views.search, name='search'),
    path('results/', views.search, name='results'),
    path('details/', views.details, name='details'),
    path('user/', views.user, name='user'),
]