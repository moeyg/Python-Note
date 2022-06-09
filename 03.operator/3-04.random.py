# 난수(random) : 무작위로 수를 뽑아주는 함수
# 난수 사용 라이브러리
from random import *

print(random())  # 0.0 ~ 1.0 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성
print(int((random() * 10) + 1))  # 1 ~ 10 이하의 임의의 값 생성

# 로또 값 생성
print(int((random() * 45) + 1))  # 1 ~ 45 이하의 임의의 값 생성

# randrage(a, b) : a 이상 b 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성

# randint(a, b) : a 이상 b 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
