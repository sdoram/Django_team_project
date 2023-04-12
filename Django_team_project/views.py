from django.http import HttpResponse
from django.shortcuts import render


#my_test.html을 보여주는 함수
def main_view(request):
    return render(request, 'main.html')