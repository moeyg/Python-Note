# 모듈화
# 필요한 것끼리 부품처럼 만들어진 파일
# 함수 정의, 클래스 등의 파이썬 문장을 담고 있는 파일로 확장자는 .py

# 모듈 사용 방법 1 : theater_module로 사용할 수 있음
import theater_module

# 모듈 사용 방법 2 : theater_module을 as 뒤의 단어로 단축어로 사용할 수 있음
import theater_module as theater

# 모듈 사용 방법 3 : theater_module을 모두 사용할 수 있음
from theater_module import *

# 모듈 사용 방법 4 : theater_module에서 사용하고 싶은 함수만 사용할 수 있음
from theater_module import price, price_morning

# 모듈 사용 방법 5 : theater_module에서 사용하고 싶은 함수를 가져와 as 뒤의 단축어로 사용할 수 있음
from theater_module import price_soldier as soldier


# theater_module 파일에서 3명이 영화를 보러 갔을 때 일반 가격
# 3명 가격은 30000원 입니다.
theater_module.price(3)  # 방법 1
theater.price(3)  # 방법 2
price(3)  # 방법 3

# theater_module 파일에서 4명이 조조 영화를 보러 갔을 때 조조 가격
# 4명 가격은 240000원 입니다.
theater_module.price_morning(4)  # 방법 1
theater.price_morning(4)  # 방법 2
price_morning(4)  # 방법 3

# theater_module 파일에서 5명의 군인이 영화를 보러 갔을 때 군인 가격
# 5명 가격은 200000원 입니다.
theater_module.price_soldier(5)  # 방법 1
theater.price_soldier(5)  # 방법 2
price_soldier(5)  # 방법 3
