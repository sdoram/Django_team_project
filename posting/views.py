from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting


def posting_detail_view(request):
    request.method == "GET"
    return render(request, '/posting_detail')


def posting_list(request, category=None):
    if category:
        posting_list = Posting.objects.filter(
            category=category).order_by('-created_date')
    else:
        posting_list = Posting.objects.all().order_by('-created_date')

    context = {
        'title': 'LIST',
        'posting_list': posting_list,
        'category': category,
    }

    return render(request, 'posting_list.html', context)

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
