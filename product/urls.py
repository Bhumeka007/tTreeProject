from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='Home'),
    path('seller/',views.sellerpage, name='Seller'),
    path('about/',views.aboutpage, name='About'),
    path('bs1/',views.bestsellerpage, name='BestSeller'),
]