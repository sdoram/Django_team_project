from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # 페이지 페이징 처리 모듈

# def posting_detail_view(request, post_id):
#     if request.method == "GET":
#         posting = get_object_or_404(Posting, id=post_id)
#         context = {
#             'posting': posting
#         }
#         return render(request, 'posting/posting_detail.html', context)

def posting_detail_view(request):
    return render(request, 'posting/posting_detail.html')
    


def posting_list(request, category=None):
    if category:
        posting_list = Posting.objects.filter(
            category=category).order_by('-create_at')
    else:
        posting_list = Posting.objects.all().order_by('-create_at')

    paginator = Paginator(posting_list, 6)  # 한 페이지당 6개의 게시글만 보여주도록 설정
    page = request.GET.get('page')  # 현재 페이지 번호 가져오기

    # 현재 페이지 번호가 유효하지 않으면 1페이지로 보여줌
    try:
        posting_list = paginator.page(page)
    except PageNotAnInteger:
        posting_list = paginator.page(1)
    except EmptyPage:
        posting_list = paginator.page(paginator.num_pages)

    context = {
        'title': 'LIST',
        'posting_list': posting_list,
        'category': category,
    }

    return render(request, 'posting/posting_list.html', context)


# 게시글 작성


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

        # posting_list = postingList.objects.create(posting=posting,
        #                                           category=category)

        return redirect('post_detail', post_id=posting.post_id)
    else:
        return render(request, 'create_post.html')

# 게시글 수정


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
        return render(request, 'update_post.html', {'posting': posting})

# 게시글 삭제


def delete_post(request, post_id):
    posting = get_object_or_404(Posting, post_id=post_id, user_id=request.user)
    posting.delete()

    return redirect('home')
