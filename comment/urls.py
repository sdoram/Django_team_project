from django.urls import path
from . import views

urlpatterns = [
    # path('', views.add_comment, name='add_comment'),
    path('add/<int:posting_id>/', views.add_comment, name='add_comment'),
    path('update/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
