from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/<str:username>', views.user_info, name='user_info'),
    path('mypage/', views.mypage, name='mypage'),
    path('edit/', views.edit, name='edit'),
]
