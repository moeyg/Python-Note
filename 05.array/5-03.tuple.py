# 튜플 (Tuple)
# variable = (value)
# variable[0] = value
# (key) = (value)
# 튜플은 항목을 추가할 수 없다.

menu = ("pizza", "burger")
print(menu[0])  # pizza
print(menu[1])  # burger


# 튜플 사용 예제
name = "James"
age = 10
hobby = "coding"
print(name, age, hobby)  # James 10 coding
# 튜플을 사용하여 아래와 같이 변환할 수 있다.
(name, age, hobby) = ("James", 10, "coding")
print(name, age, hobby)  # James 10 coding
