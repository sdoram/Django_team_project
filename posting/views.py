from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Posting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # 페이지 페이징 처리 모듈
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def posting_detail_view(request, post_id):
    posting = get_object_or_404(Posting, post_id=post_id)
    context = {
        'posting': posting
    }
    return render(request, 'posting/posting_detail.html', context)


# def posting_detail_view(request):
#     return render(request, 'posting/posting_detail.html')




from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import Posting


def posting_list(request, category=None):
    if category:
        posting_list = Posting.objects.filter(category=category).order_by('-create_at')
    else:
        posting_list = Posting.objects.all().order_by('-create_at')

    paginator = Paginator(posting_list, 6)  # 한 페이지당 6개의 게시글만 보여주도록 설정
    page_number = request.GET.get('page')  # 현재 페이지 번호 가져오기

    # 현재 페이지 번호가 유효하지 않으면 1페이지로 보여줌
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'title': 'LIST',
        'posting_list': page_obj,
        'category': category,
    }

    return render(request, 'posting/posting_list.html', context)



# 게시글 작성
@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        user_id = request.user
        title = request.POST.get('title')
        main_content = request.POST.get('main_content')
        category = request.POST.get('category')

        posting = Posting.objects.create(user_id=user_id,
                                         title=title,
                                         main_content=main_content,
                                         category=category)

        return redirect('post_detail', post_id=posting.post_id)
    else:
        return render(request, 'posting/posting_admin.html')

# 게시글 수정
@login_required(login_url='login')
def update_post(request, post_id):
    posting = get_object_or_404(Posting, post_id=post_id, user_id=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        main_content = request.POST.get('main_content')
        category = request.POST.get('category')

        posting.title = title
        posting.main_content = main_content
        posting.category = category
        posting.save()

        return redirect('post_detail', post_id=post_id)
    else:
        return render(request, 'posting/posting_admin.html', {'posting': posting})

# 게시글 삭제
@login_required(login_url='login')
def delete_post(request, post_id):
    posting = get_object_or_404(Posting, post_id=post_id, user_id=request.user)
    posting.delete()

    return redirect('home')


def posting_admin(request):
    return render(request, 'posting/posting_admin.html')


@csrf_exempt
def api_create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        main_content = request.POST.get('main_content')
        category = request.POST.get('category')
        post = Posting(title=title, main_content=main_content, category=category)
        post.save()
        response_data = {'success': True, 'post_id': post.id}
        return JsonResponse(response_data)
    else:
        response_data = {'success': False, 'message': 'Invalid request method'}
        return JsonResponse(response_data, status=400)