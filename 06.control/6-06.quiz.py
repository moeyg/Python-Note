# Quiz) 당신은 CocoaTaxi 서비스를 이용하는 택시 기사님 입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하세요.

# 조건1 : 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5 ~ 15분 사이의 승객만 매칭해야 합니다.

# 출력문 예제
# [✅] 1 번째 손님 (소요 시간 : 15 분)
# [ ] 2 번째 손님 (소요 시간 : 50 분)
# [✅] 3 번째 손님 (소요 시간 : 5 분)
# ...
# [ ] 50 번째 손님 (소요 시간 : 16 분)
# 총 탑승 승객 : 2 분

from random import *

count = 0  # 총 탑승 승객
customer = 1  # 첫 번째 승객부터 시작

while customer <= 50:
    time = randrange(1, 51)
    if 1 <= time <= 15:
        print("[✅] {0} 번째 손님 (소요 시간 : {1} 분".format(customer, time))
        count += 1
    else:
        print("[  ] {0} 번째 손님 (소요 시간 : {1} 분".format(customer, time))
    customer += 1

print("총 탑승 승객 : {} 분".format(count))


# 답

count = 0  # 총 탑승 승객

for customer in range(1, 51):  # 1 ~ 50 명의 승객
    time = randrange(5, 51)  # 5 ~ 50분 소요 시간
    if 5 <= time <= 15:  # 5 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 처리
        print("[✅] {0} 번째 손님 (소요 시간 : {1} 분".format(customer, time))
        count += 1
    else:  # 매칭 실패
        print("[  ] {0} 번째 손님 (소요 시간 : {1} 분".format(customer, time))

print("총 탐승 승객 : {0} 분".format(count))
