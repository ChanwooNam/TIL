from django.shortcuts import render
import requests

# Create your views here.

# 루트 페이지 
def index(request):
    return render(request, 'index.html')

# 정보를 던져줄 페이지
def throw(request):
    return render(request, 'throw.html')

# 사용자로부터 정보를 받아서 다시 던져줄 페이지 
def catch(request):
    message = request.GET.get('message')
    context = { 'message' : message }
    return render(request, 'catch.html', context)


# [실습] 아스키 아티 ASCII ARTII
# 사용자로부터 텍스트 입력받는 페이지
def art(request):
    return render(request, 'art.html')
# 텍스트 받아서 아스키 아트로 보여주는 페이지
def result(request):
    message = request.GET.get('message')
    
    font = requests.get(f'http://artii.herokuapp.com/make?text={message}&font=trek').text
    context ={ 'font' : font }
    return render(request, 'result.html', context)
    