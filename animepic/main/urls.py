from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', MainView.as_view(), name='MainView'),
    path('character/<slug:post_slug>/', PostView.as_view(), name='PostView'),
    path('character/category/<slug:cat_slug>/', CatView.as_view(), name='CatView'),
    path('character/new/add/', AddPost.as_view(), name='AddPost'),
    path('contact/', Contact.as_view(), name='Contact'),
    path('search/', SearchView.as_view(), name='Search'),
]