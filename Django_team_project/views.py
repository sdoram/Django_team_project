from django.http import HttpResponse
from django.shortcuts import render
from posting.models import Posting
from django.shortcuts import render, redirect, get_object_or_404


#my_test.html을 보여주는 함수
# main리스트
def main_view(request):
# posting 모델 임포트함
# 제목이랑 글쓴이만 출력

    if request.method == 'GET':
            # 모든 게시글 가져오기
            posting_list = Posting.objects.order_by('-create_at')  # 카테고리별로 시간 내림차순 정렬
            return render(request, 'main.html', {'postings': posting_list})


# def posting_list(request, category=None):
#     if category:
#         # 모델에서 choices 옵션으로 정의한 값('codereview')으로 필터링합니다.
#         posting_list = Posting.objects.filter(
#             category=category.lower()).order_by('-create_at') # 카테고리별로 시간 내림차순 정렬
    
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
