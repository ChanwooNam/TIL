'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

total_score = 0
for subject_score in score.values():
  total_score += subject_score
  
result = total_score / len(score.keys())
print(result)

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    '민승': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    '건희': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

## 나 

total_score = 0
persons = len(scores.keys())  # 사람 수 

for person in scores.keys():
  for subject_score in scores[person].values():
    total_score += subject_score
  result = total_score / len(scores[person].values())
  print(total_score)
  print(result)
  result = 0
  total_score = 0

## 강사님


# 3. 도시별 최근 3일의 온도입니다.
cities = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
'''
출력 예시)
서울 : 평균온도
대전 : 평균온도
광주 : 평균온도
부산 : 평균온도
'''

tt = 0
for city, temp in cities.items():
  print(f'{city} :  {sum(temp) / len(temp)}')
  
# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
temp_min= []
for city, temp in cities.items():
  temp_min = min(temp)
  temp_max = max(temp)

  city = {'city' : city, 'min' : temp_min, 'max' : temp_max}
  


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')