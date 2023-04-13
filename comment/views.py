from .models import Comment
from django.shortcuts import render,redirect
from django.http import HttpResponse
def comment(request):
    # if request.method == 'GET': #요청하는 방식이 GET 방식인지 확인하기  
    #     user = request.user.is_authenticated
    #     if user: #로그인 한 사용자라면
    #      return render(request, 'posting_detail.html')
    #     else:
            #return redirect('/user/login')
    if request.method == 'GET':
        return render(request, 'comment/borad.html')
    elif request.method == 'POST':
        user = request.user
        my_comment = Comment()
        my_comment.username = user
        my_comment.comment_content = request.POST.get('comment_content',None)#댓글 내용
        my_comment.save()
        
        return redirect('/main')
        