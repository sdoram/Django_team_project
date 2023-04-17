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
    
    #     if # 카테고리별로 게시글 리스트 보이게
    # codereview_posts = Posting.objects.filter(category='codereview')
    # course_posts = Posting.objects.filter(category='course')
    # coding_study_posts = Posting.objects.filter(category='coding_study')
    # study_posts = Posting.objects.filter(category='study')
    # free_board_posts = Posting.objects.filter(category='free_board')

    # context = {
    #     'codereview_posts':codereview_posts,
    #     'course_posts':course_posts,
    #     'coding_study_posts':coding_study_posts,
    #     'study_posts':study_posts,
    #     'free_board_posts':free_board_posts,
    # }

    # return render(request, 'main.html', context)
