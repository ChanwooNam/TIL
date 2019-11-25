from django.shortcuts import render
import random 
from datetime import datetime

# Create your views here.
# view 함수 -> 중간 관리자
# 사용자가 접속해서 볼 페이지를 작성한다. 즉, 하나하나의 페이지를 'view'라고 부른다. 
# 'view' 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다. 


def index(request):    # 첫번째 인자 반드시 request!
    return render(request, 'index.html')

'''
def introduce(request):

    name = '찬우'

    # render 메서드의 세번째 인자로 변수를 딕셔너리 형태로 넘길 수 있다. 
    return render(request, 'introduce.html', { 'name': name })
'''

def dinner(request):
    menu = ['초밥', '삽겹살', '돈까스', '회', '곱창']
    pick = random.choice(menu)

    # 넘겨줄 인자가 여러개인 경우
    context = {
        'pick' : pick  
    }

    return render(request, 'dinner.html', context)
    
# Lorem Picsum 사용해서 랜덤 이미지 보여주는 페이지 만들기!
'''
def image(request):
    image = 'https://picsum.photos/200/300'
    context = {
        'image' : image
    }
    return render(request, 'image.html', context)
'''
# 동적 라우팅
def hello(request, name):
    menu = ['초밥', '삽겹살', '돈까스', '회', '곱창']
    pick = random.choice(menu)

    # 넘겨줄 인자가 여러개인 경우
    context = {
        'name' : name,
        'pick' : pick, 
    }
    return render(request, 'hello.html', context)

# 실습 1 : 템플릿 변수 2개 이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해 보자!
def introduce(request, name,age,hobby,talent):
    context = {
        'name' : name,
        'age' : age,
        'hobby' : hobby,
        'talent' : talent,
    }
    return render(request, 'introduce.html', context)


# 실습 2 : 숫자 2개를 동적 라우팅으로 전달 받아서, 두 개의 숫자를 곱해주는 페이지를 만들자!
def times(request, num1, num2):
    square = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'square' : square,
    }
    return render(request, 'times.html', context)

# 실습 3 : 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자!
def area(request, radius):
    circle = (radius ** 2) * 3.14
    context = {
        'radius' : radius,
        'circle' : circle,
    }
    return render(request, 'area.html', context)

# 실습 4 : 동적 라우팅으로 이미지 너비, 높이를 받아서 이미지 출력하는 페이지! 
def image(request, width, height ):
    image = 'https://picsum.photos'
    context = {
        'image' : image,
        'width' : width,
        'height' : height,
    }
    return render(request, 'image.html', context)


# DTL ( Django Template Langauge )
def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

# [실습1] ISIT YOUR BIRTH?
# 오늘 날짜와 본인 실제 생일 비교해서, 맞으면 예! 아니면 아니오!
def isbirth(request):
    my_birth = '10월 28일'
    datetimenow = datetime.now()
    monthnow = datetimenow.month
    daynow = datetimenow.day

    if datetimenow.month == 10 and datetimenow.day == 28 :
        result = True
    else :
        result = False 

    context = {
        'my_birth' : my_birth,
        'datetimenow ' : datetimenow,
        'monthnow' : monthnow,
        'daynow' : daynow,
        'result' : result,
    }

    return render(request, 'isbirth.html', context)

# [실습2] 회문 판별 (팰린드롬)
# ex) 오디오는 거꾸로 해도 오디오 -> 회문!
def ispal(request, word):
    # 검색 키워드 : python 문자열 슬라이스 
    if word == word[::-1]:
        result = True
    else :
        result = False 
    context = {
        'result' : result, 
        'word' : word,
        }
    return render(request, 'ispal.html', context)

# [실습3] 로또 번호 추첨 (리스트 + a 활용)
# 임의로 출력한 로또 번호와 가장 최근에 추첨한 로또 번호 비교해서 당첨여부 확인
def lotto(request):

    lottos = sorted(list(random.sample(range(1,46),6)))
    real_lottos = [18, 34, 39, 43, 44, 45]    # 882회차 

    context ={
        'lottos' : lottos,
        'real_lottos' : real_lottos,
    }

    return render(request, 'lotto.html', context )






