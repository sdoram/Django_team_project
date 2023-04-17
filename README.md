# 프로젝트 이름 : 임금님 귀는 당나귀 귀
### 마음속에 묵혀두고있던 하고싶은 말을 털어놓는 개발자 전용 커뮤니티입니다.
---
# 팀명 : 장고와 함께하는 야생 생활
***

## 팀원 :
***
### 김세만 (팀장): 회원가입,로그인,로그아웃 기능구현 이후 팀원 케어
### 구병진 : 게시글 작성 , 수정 , 삭제기능 
### 공민영 : 메인페이지 , 마이페이지 , 마이페이지 수정기능 
### 임재훈 : 게시글 리스트 , 게시글 카테고리 , 게시글 상세페이지 기능
### 장한울 : 댓글작성 , 수정 , 삭제기능

---
---
# 설명
## 메인페이지 :
### 게시글의 리스트를 한 눈에 볼 수 있다 사용자 검색에서 회원을 검색해 볼 수 있다 , 카테고리별 리스트로 바로가기 기능 추가

## 마이페이지 :
### 회원정보가 보이고 로그인 되어있는 회원정보를 수정할 수 있다 , 해당 회원이 작성한 게시글 , 댓글을 볼 수 있음

## 게시글 작성 : 
### 게사글을 작성, 수정할 수 있음

## 게시글 상세 페이지 :
### 게시글과 댓글을 볼 수 있고 로그인된 사용자가 게시글 작성자와 일치한다면 수정, 삭제버튼이 보이고 댓글을 작성한 사용자와 사용자가 일치하면 댓글을 수정, 삭제를 할 수 있게했다

## 게시글 리스트 : 
### 최신 게시글이 위로 보일수 있게 정렬해뒀고 카테고리별로 게시글을 모아서 볼 수 있음 개시글이 많으면 페이지를 넘길수 있는 기능추가

## 로그인 , 회원가입 :
### 사용자에게 정보를 입력받아 회원가입을 할 수 있고 중복된 유저 id를 사용하지 못히게 만듦 email, 성별은 선택사항으로 입력값이 없어도 가입이 가능

## 가장 마음에 드는 코드
### 김세만 : 
```python
def search_info(request):
    try:
        # html 검색 입력값 가져 오기
        search_user = request.GET.get('search_user')
        user_info = get_object_or_404(UserModel, username=search_user)
        postings = Posting.objects.filter(username=user_info).order_by('-create_at')
        comments = Comment.objects.filter(username=user_info).order_by('-create_at')
        return render(request, 'user/user_info.html', {'user_info': user_info, 'postings': postings, 'comments':comments})
    except Http404:
        return HttpResponse(f"<script>alert('{search_user}은 존재하지 않는 유저입니다! or next로 돌아오면서 search_user값이 없어서 에러 발생');location.href='/main';</script>")
```
이해 가능한 코드로  유저 검색이라는 새로운 기능을 만들어서 마음에 듭니다.

### 구병진 :
```python
# 게시글 수정 
@login_required(login_url='login')
def update_post(request, post_id):
    posting = get_object_or_404(Posting, post_id=post_id, username=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        main_content = request.POST.get('main_content')
        category = request.POST.get('category')

        posting.title = title
        posting.main_content = main_content
        posting.category = category
        posting.save()

        return redirect(reverse('posting_detail', kwargs={'post_id': post_id}))
    else:
        context = {'posting': posting}
        return render(request, 'posting/posting_admin.html', context)
```
데코레이터 ```python@login_required(login_url='login')```을 사용하여 해당 view 함수가 실행되기 전에 사용자가 로그인했는지 확인합니다. 만약 로그인하지 않았다면 'login' URL로 리디렉션합니다.
### 공민영 :
```python
<!--님이 작성한 글 전체보기 >-->
            <div class="mypage_write">
                <!--<a href="/user/mypage/{user_id}">내가 작성한 글 > </a>-->
                <a href="/user/myposting">{{ user.username }}님이 작성한 글 전체보기 > </a>
                {% if postings %}
                <ul>
                    {% for posting in postings|slice:'3' %}
                    <li><b><a style="color: black" href="{% url 'posting_detail' posting.posting_id %}">{{ posting.title }}</a></b></li>
                    {% endfor %}
                </ul>
                {% else %}
                <p>작성한 글이 없습니다.</p>
                {% endif %}
            </div>
            
            
def myposting(request):
    user = request.user
    if request.method == 'GET':
        postings = Posting.objects.filter(username=user)
        return render(request, 'user/myposting.html', {'user': user, 'postings': postings})
```
로그인한 사용자가 작성한 글을 모아 볼 수 있는 기능입니다.
### 임재훈 :
```python
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
```
pagonator 모듈을 사용해서 페이징처리를 할 수 있던게 제일 마음 들었습니다
### 장한울 :










