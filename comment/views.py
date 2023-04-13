from .models import Comment
from django.shortcuts import render,redirect
from django.http import HttpResponse
def comment(request):
    if request.method == 'GET': #요청하는 방식이 GET 방식인지 확인하기  
        user = request.user.is_authenticated
        if user: #로그인 한 사용자라면
         return render(request, 'posting_detail.html')
        else:
            return redirect('/user/login')
    elif request.method == 'POST':
        user = request.user
        my_tweet = Comment()
        my_tweet = user
        my_tweet
        

