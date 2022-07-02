from .views import index_page
from django.urls import path

urlpatterns = [
    path('', index_page),
]
