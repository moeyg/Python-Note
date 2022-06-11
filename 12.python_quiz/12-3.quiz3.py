# Quiz) 사회적 거리두기" 에 따른 영화관 좌석 예매 시스템을 만드세요.

# [조건]
# 1. 각 열은 1 ~ 20번까지 총 20개의 좌석으로 구성되어 있습니다.
# 예) A1 A2 A3 A4 ... A20
#     B1 B2 B3 B4 ... B20
#     C1 C2 C3 C4 ... C20

# 2. 이 때 A열에 대해서 홀수로 끝나는 좌석에 대해서만 출력하세요. (각 좌석은 "" 로 구분)
# 예) A1 A3 A5 A7 ... A19

rows = ["A", "B", "C", "D", "E", "F"]

# 해결 1
for row in rows:
    for seat in range(1, 21):
        if seat % 2 == 1:
            print("{0}{1}".format(row, seat), end=" ")
    print()

print()

# 해결 2
for row in rows:
    for seat in range(1, 21)[::2]:
        print("{0}{1}".format(row, seat), end=" ")
    print()
