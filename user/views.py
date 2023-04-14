from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        gender = request.POST.get('gender', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)

            if exist_user:
                return HttpResponse('이미 존재하는 유저입니다.')
            else:
                UserModel.objects.create_user(username=username,
                                              password=password,
                                              name=name,
                                              email=email,
                                              gender=gender)
        return redirect('/user/login')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return render(request, 'main.html')
        else:
            return redirect('/user/login')
    elif request.method == 'GET':
        return render(request, 'user/login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/user/login')

# 민영

def edit(request):
    return render(request, 'user/edit.html')


def mypage(request):
        user = UserModel()
        if request.method == 'GET':
            # username = request.GET.get('username', None)
            return render(request, 'user/mypage.html')
        if request.method == 'POST':
            username = request.POST.get('username', None)
            # name = request.POST.get('name', None)
            # gender = request.POST.get('gender', None)
            # email = request.POST.get('email', None)
            if username:
                user.username = username
                # user.name = name
                # user.gender = gender
                # user.email = email
                user.save()
                return HttpResponse('성공')
            else:
                return HttpResponse('실패')




# 마이페이지 user정보 수정
# 1. 버튼을 누르는 순간 기존 사용자 정보를 가져오는데
#  입력폼에 채워진 채로 보여주는 것이 중요
# 2. 새로입력한 내용을 post요청으로 db에 보냄

# def edit(request):
#     if request.method == 'POST':
#         return
#     # username, name, email을 가지고와서 user에 저장
#     user = UserModel.objects.get(username='username', name='name', email='email')
#     user.username = 'username'
#     render(request, 'user/edit.html')



