from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def signup(request):
    # 이미 로그인한 유저 메인페이지로 돌려보내기
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        gender = request.POST.get('gender', None)
        # password 불일치를 나타낼 수 있도록 변경
        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            # HttpResponse 이외의 방법으로 변경
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
    # 이미 로그인한 유저 메인페이지로 돌려보내기
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/main')
        else:
            return redirect('/user/login')
    elif request.method == 'GET':
        return render(request, 'user/login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/user/login')

# 민영
def mypage(request):
    return render(request, 'user/mypage.html')
