from django.urls import path
from . import views

urlpatterns = [
    path('/posting_detail', views.posting_detail_view, name='posting_detail'),
    path('/posting_list', views.posting_list, name='posting_list'),
]