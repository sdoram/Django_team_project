from django.urls import path
from user import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('mypage/{username}', views.mypage, name='mypage'),
    path('mypage/', views.mypage, name='mypage'),
]
