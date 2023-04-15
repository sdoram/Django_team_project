from django.shortcuts import render, redirect, get_object_or_404
from .models import UserModel
from posting.models import Posting
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from posting.models import Posting


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

def edit(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        gender = request.POST.get('gender', None)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        # 기존 사용자 정보를 가져옴
        # me = get_object_or_404(UserModel, pk=username)
        me = get_object_or_404(UserModel, username=username)
        # 하나도 변경된 사항이 없는 경우 -> alert창
        if me.username == username and me.gender == gender and me.name == name and email == email:
            return HttpResponse("<script>alert('변경사항이 없습니다!');location.href='/user/edit';</script>")
        # 변경된 사항이 있는 경우 -> 저장
        else:
            me.username = username
            me.gender = gender
            me.name = name
            me.email = email
            me.save()

            return HttpResponse("<script>alert('수정완료!');location.href='/user/mypage';</script>")
    elif request.method == "GET":
        return render(request, 'user/edit.html')


def mypage(request):
        user = request.user
        if request.method == 'GET':
            # .order_by('-create_at')은 정렬하기
            postings = Posting.objects.filter(username=user).order_by('-create_at')
            return render(request, 'user/mypage.html', {'user': user, 'postings': postings})
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
            



def myposting(request):
        user = request.user
        if request.method == 'GET':
            postings = Posting.objects.filter(username=user)
            return render(request, 'user/myposting.html', {'user': user, 'postings': postings})
            

def user_info(request, username):

    if request.method == 'GET':
        user_info = get_object_or_404(UserModel, username=username)
        postings = Posting.objects.filter(username=username)
    return render(request, 'user/user_info.html', {'user_info': user_info, 'postings': postings})
