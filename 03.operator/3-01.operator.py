# 연산자 (Operators)

# + 더하기
print(10 + 10)  # 20
# - 빼기
print(11 - 10)  # 1
# * 곱하기
print(10 * 10)  # 100
# / 나누기
print(10 / 2)  # 5.0
# // 몫
print(10 // 3)  # 3
# % 나머지
print(10 % 3)  # 1
# ** 거듭제곱
print(10 ** 2)  # 100 = 10^2

# 비교 연산
print(10 > 1)  # True
print(10 >= 1)  # True
print(1 > 10)  # False
print(10 >= 10)  # True
print(10 == 10)  # True
print(10 + 10 == 20)  # True
print(10 != 1)  # True
print(not(10 != 1))  # False

# and(&) : 조건이 모두 맞아야 참
print((10 > 0) and (10 > 1))  # True
print((10 < 0) & (10 > 1))  # False
# or(|) : 조건 중 하나라도 맞으면 참
print((10 > 0) or (10 < 1))  # True
print((10 < 0) | (10 < 1))  # False

print(10 > 5 > 1)  # True
print(10 > 5 > 8)  # False
