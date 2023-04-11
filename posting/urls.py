from django.urls import path
from . import views

urlpatterns = [
    path('posting_detail/', views.posting_detail_view, name='posting_detail'),
    path('posting_list/<str:category>/', views.posting_list, name='posting_list'),
    path('posting_list/', views.posting_list, name='posting_list'),
]


#### 지피티 #### 
# from django.urls import path
# from .views import posting_list, posting_detail_view, create_post, update_post, delete_post

# urlpatterns = [
#     path('', posting_list, name='home'),
#     path('posting/<int:post_id>/', posting_detail_view, name='post_detail'),
#     path('posting/create/', create_post, name='create_post'),
#     path('posting/update/<int:post_id>/', update_post, name='update_post'),
#     path('posting/delete/<int:post_id>/', delete_post, name='delete_post'),
# ]
