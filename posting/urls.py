from django.urls import path
from . import views


urlpatterns = [
    path('posting_detail/', views.posting_detail_view, name='posting_detail'),
    path('posting/<int:post_id>/', views.posting_detail_view, name='post_detail'),
    path('posting_list/<str:category>/',views.posting_list, name='posting_list'),
    path('posting_list/', views.posting_list, name='posting_list'),
    path('create/', views.create_post, name='create_post'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('posting_admin/', views.posting_admin, name='posting_admin'),
    path('api/create-post/', views.api_create_post, name='api_create_post'),
    path('api/update-post/<int:post_id>/',
         views.api_update_post, name='api_update_post'),

]
