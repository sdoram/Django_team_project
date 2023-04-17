from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Posting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # 페이지 페이징 처리 모듈
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


# 게시글 상세보기 
def posting_detail_view(request, posting_id):
    posting = get_object_or_404(Posting, posting_id=posting_id)
    comment_list = posting.comment_set.order_by('-create_at') # 댓글 리스트 시간역순으로 모아보기
    

    context = {
        'posting': posting,
        'comment_list': comment_list,
    }

    # 댓글 수정, 삭제 버튼 보여주기
    if request.user.is_authenticated: # 유저 판별코드 
        for comment in comment_list:
            if request.user == comment.username:
                comment.can_modify = True #can_modify 활용 유저 판별해서 보여주기
            else:
                comment.can_modify = False

    return render(request, 'posting/posting_detail.html', context)




#게시글 리스트
def posting_list(request, category=None):
    if category:
        # 모델에서 choices 옵션으로 정의한 값('codereview')으로 필터링합니다.
        posting_list = Posting.objects.filter(
            category=category.lower()).order_by('-create_at') # 카테고리별로 시간 내림차순 정렬
    else:
        posting_list = Posting.objects.all().order_by('-create_at') # 전체보기 시간 내림차순 정렬

    paginator = Paginator(posting_list, 6)  #게시글 6개가 1페이지
    page = request.GET.get('page')
    page_obj = paginator.get_page(page) 
    try: # try except 문 사용해서 오류코드가 나왔을때도 작동되게 함
        posting_list = paginator.page(page)
    except PageNotAnInteger: #페이지가 범위를 넘어가면 1번 페이지
        posting_list = paginator.page(1)
    except EmptyPage: # 없는페이지를 보일때 마지막 페이지를 보임
        posting_list = paginator.page(paginator.num_pages)

    context = {
        'title': 'LIST',
        'posting_list': posting_list,
        'category': category,
        'page_obj' : page_obj
    }

    return render(request, 'posting/posting_list.html', context)




# 게시글 작성
# @login_required(login_url='login')
def create_post(request):
    if not request.user.is_authenticated:
        return redirect("/main")
    if request.method == 'POST':
        user_id = request.user.id  # 로그인한 사용자의 id 값을 가져옴
        title = request.POST.get('title')
        main_content = request.POST.get('main_content')
        category = request.POST.get('category')

        posting = Posting.objects.create(username_id=user_id,  # username 필드에 로그인한 사용자의 id 값을 입력
                                         title=title,
                                         main_content=main_content,
                                         category=category)

        return redirect('posting_detail', posting_id=posting.posting_id)
    else:
        return render(request, 'posting/posting_admin.html')






# 게시글 수정
@login_required(login_url='login')
def update_post(request, posting_id):
    posting = get_object_or_404(Posting, posting_id=posting_id, username=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        main_content = request.POST.get('main_content')
        category = request.POST.get('category')

        posting.title = title
        posting.main_content = main_content
        posting.category = category
        posting.save()

        return redirect(reverse('posting_detail', kwargs={'posting_id': posting_id}))
    else:
        context = {'posting': posting}
        return render(request, 'posting/posting_admin.html', context)


# 게시글 삭제
@login_required(login_url='login')
def delete_post(request, pk):
    posting = get_object_or_404(Posting, posting_id=pk, username=request.user)
    if request.method == 'POST':
        posting.delete()
        return redirect('posting_list')
    else:
        context = {'posting': posting}
        return render(request, 'posting/posting_confirm_delete.html', context)


def posting_admin(request):
    return render(request, 'posting/posting_admin.html')

# return 값 수정 
@csrf_exempt
def api_create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        main_content = request.POST.get('main_content')
        category = request.POST.get('category')
        post = Posting(title=title, main_content=main_content, category=category)
        post.save()
        response_data = {'success': True, 'posting_id': post.posting_id}
        return JsonResponse(response_data)
    elif request.method == 'GET':
        response_data = {'success': True, 'message': 'API is working.'}
        return JsonResponse(response_data)
    else:
        response_data = {'success': False, 'message': 'Invalid request method'}
        return JsonResponse(response_data, status=400)

    

@csrf_exempt
def api_update_post(request, posting_id):
    if request.method == 'PUT':
        title = request.POST.get('title')
        main_content = request.POST.get('main_content')
        category = request.POST.get('category')

        post = get_object_or_404(Posting, posting_id=posting_id, user_id=request.user)
        post.title = title
        post.main_content = main_content
        post.category = category
        post.save()

        data = {
            'posting_id': post.posting_id,
            'title': post.title,
            'main_content': post.main_content,
            'category': post.category
        }
        return JsonResponse(data)




