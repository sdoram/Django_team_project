from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comment
from posting.models import Posting


@login_required(login_url='/user/login')
def add_comment(request, post_id):
    if request.method == 'POST':
        user = request.user
        content = request.POST.get('content')
        post = get_object_or_404(Posting, post_id=post_id)
        comment = Comment(author=user, post_id=post_id, content=content)
        comment.save()
        return redirect('posting_detail', post_id=post_id)
    else:
        return HttpResponse('Invalid Access')


@login_required(login_url='/user/login')
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('posting_detail', post_id=comment.post.post_id)
    else:
        context = {'comment': comment}
        return render(request, 'comment/edit_comment.html', context)


@login_required(login_url='/user/login')
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, username=request.user)
    post_id = comment.posting.post_id
    comment.delete()
    return redirect('posting_detail', post_id=post_id)


@csrf_exempt
@login_required(login_url='/user/login')
def api_delete_comment(request):
    if request.method == 'DELETE':
        user = request.user
        comment_id = request.POST.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id, author=user)
        comment.delete()
        response_data = {'success': True,
                         'message': 'Comment deleted successfully'}
        return JsonResponse(response_data)
    else:
        response_data = {'success': False, 'message': 'Invalid request method'}
        return JsonResponse(response_data, status=400)


@csrf_exempt
@login_required(login_url='/user/login')
def api_add_comment(request):
    if request.method == 'POST':
        user = request.user
        content = request.POST.get('content')
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Posting, post_id=post_id)
        comment = Comment(author=user, post=post, content=content)
        comment.save()
        data = {
            'success': True,
            'comment_id': comment.id,
            'author': comment.author.username,
            'content': comment.content,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': comment.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        return JsonResponse(data)
    else:
        response_data = {'success': False, 'message': 'Invalid request method'}
        return JsonResponse(response_data, status=400)


@csrf_exempt
@login_required(login_url='/user/login')
def api_update_comment(request):
    if request.method == 'PUT':
        user = request.user
        comment_id = request.POST.get('comment_id')
        content = request.POST.get('content')
        comment = get_object_or_404(Comment, id=comment_id, author=user)
        comment.content = content
        comment.save()
        data = {
            'success': True,
            'comment_id': comment.id,
            'author': comment.author.username,
            'content': comment.content,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': comment.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        return JsonResponse(data)
    else:
        response_data = {'success': False, 'message': 'Invalid request method'}
        return JsonResponse(response_data, status=400)


@csrf_exempt
@login_required(login_url='/user/login')
def api_delete_comment(request):
    if request.method == 'DELETE':
        user = request.user
        comment_id = request.POST.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id, author=user)
        comment
