# 사전 (Dictionary)
# dict_variable = {key: value}

cabinet = {1: "James", 100: "Paul"}

print(cabinet[1])  # James
print(cabinet[100])  # Paul

print(cabinet.get(1))  # James
print(cabinet.get(100))  # Paul

# 존재하지 않는 key를 호출하면 오류 발생
# print(cabinet[10])

# 반면에 .get() 을 사용하면 None 출력
print(cabinet.get(10))  # None
# 값이 존재하지 않으면 뒤의 값 출력
print(cabinet.get(10, "⭕️"))  # ⭕️
# 값이 존재하면 원래의 값 출력
print(cabinet.get(1, "⭕️"))  # James

# 사전의 key 에 value 가 존재하는지 확인
print(1 in cabinet)  # True
print(10 in cabinet)  # False

# 정수형 key도 가능
cabinet = {"A-1": "James", "A-100": "Paul"}

print(cabinet["A-1"])  # James
print(cabinet["A-100"])  # Paul
print(cabinet.get("A-1"))  # James
print(cabinet.get("A-100"))  # Paul

print(cabinet.get("B-10", "⭕️"))  # ⭕️
print(cabinet.get("A-1", "⭕️"))  # James

print("A-1" in cabinet)  # True
print("B-10" in cabinet)  # False

# 새로운 key: value
print(cabinet)  # {'A-1': 'James', 'A-100': 'Paul'}
cabinet["B-20"] = "Mary"
cabinet["A-1"] = "John"
print(cabinet)  # {'A-1': 'John', 'A-100': 'Paul', 'B-20': 'Mary'}

# key: value 삭제
del cabinet["A-100"]
print(cabinet)  # {'A-1': 'John', 'B-20': 'Mary'}

# 총 사용 중인 key 출력
print(cabinet.keys())  # dict_keys(['A-1', 'B-20'])
print(cabinet.values())  # dict_values(['John', 'Mary'])

# key, value 함께 출력
print(cabinet.items())  # dict_items([('A-1', 'John'), ('B-20', 'Mary')])

# key: value 모두 삭제
cabinet.clear()
print(cabinet)  # {}
