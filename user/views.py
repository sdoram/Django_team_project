from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.user.is_authenticated:
        return redirect("/main")
    elif request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        gender = request.POST.get('gender', None)
        
        # 빈값 체크 조건문 alert으로 모달창 출력
        if username == '':
            return HttpResponse("<script>alert('아이디를 입력해주세요!');location.href='/user/signup';</script>")
        if name == '':
            return HttpResponse("<script>alert('이름을 입력해주세요!');location.href='/user/signup';</script>")
        if password == '':
            return HttpResponse("<script>alert('비밀번호를 입력해주세요!');location.href='/user/signup';</script>")
        elif password != password2:
            return HttpResponse("<script>alert('비밀번호가 일치하지 않습니다!');location.href='/user/signup';</script>")

        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return HttpResponse("<script>alert('이미 존재하는 유저입니다.');location.href='/user/signup';</script>")
            else:
                UserModel.objects.create_user(username=username,
                                              password=password,
                                              name=name,
                                              email=email,
                                              gender=gender)
                # 회원가입 후 자동 로그인
                me = auth.authenticate(request, username=username, password=password)
                if me is not None:
                    auth.login(request, me)
                    return redirect('/main')
        return redirect('/user/login')


def login(request):
    if request.user.is_authenticated:
        return redirect("/main")
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 이전 페이지 url or main
        next_url = request.GET.get('next') or '/main'

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect(next_url)
        else:
            return redirect('/user/login')
    elif request.method == 'GET':
        return render(request, 'user/login.html')


@login_required
def logout(request):
    auth.logout(request)
    next_url = request.GET.get('next') or '/main'
    return redirect(next_url)


# 민영
def mypage(request):
    return render(request, 'user/mypage.html')
