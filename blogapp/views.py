from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blogapp
from drink.models import BlogDrink
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def home(request):  # 쿼리셋( 블로그 객체 목록 = 메소드 ) 전달 
    return render(request, 'home.html')

    # 쿼리셋 표현
    # 모델.쿼리셋(object)
def detail(request):
    return render(request, 'detail.html')

def new(request):
    return render(request, 'new.html')
@csrf_exempt
def create(request): # 입력받은내용을 DB에 넣어주는 함수
    blogapp = Blogapp()
    blogapp.title = request.POST['title']
    blogapp.body = request.POST['body']
    blogapp.pub_date = timezone.datetime.now()
    blogapp.kinds = request.POST['kinds']
    blogapp.kakaotalkID = request.POST['kakaoTalkID']
    blogapp.price = request.POST['price']
    blogapp.save()
    return render(request, 'finish.html')
    