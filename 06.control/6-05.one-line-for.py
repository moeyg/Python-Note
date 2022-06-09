# 출석번호가 1, 2, 3, 4 -> 앞에 100을 붙이기로 함 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [index+100 for index in students]
print(students)

# 학생 이름을 길이로 변환
students = ["James", "Mary", "David", "Linda", "Paul"]
students = [len(index) for index in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["James", "Mary", "David", "Linda", "Paul"]
students = [index.upper() for index in students]
print(students)

# 학생 이름을 소문자로 변환
students = [index.lower() for index in students]
print(students)
