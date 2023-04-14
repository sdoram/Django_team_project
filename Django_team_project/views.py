from django.http import HttpResponse
from django.shortcuts import render
from posting.models import Posting


#my_test.html을 보여주는 함수
# main리스트
def main_view(request): 
# posting 모델 임포트함
# 제목이랑 글쓴이만 출력
    if not request.user.is_authenticated:
          return render(request,'main.html')
    elif request.method == 'GET':
            # 모든 게시글 가져오기
            # postings = get_object_or_404(Posting, username=request.username)
            user = request.user
            postings = Posting.objects.filter(username=user).order_by('-create_at')
            return render(request, 'main.html', {'user': user, 'postings': postings})
