# 세트, 집합 (set)
# 중복 안 됨, 순서 없음
# variable = {value}

from turtle import back

my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}

backend_engineer = {"James", "Linda"}
frontend_engineer = set(["James", "Mary", "David"])

# & / .intersection : 백엔드와 프론트엔드 개발자 교집합
# {'James'}
print(backend_engineer & frontend_engineer)
print(backend_engineer.intersection(frontend_engineer))

# | / .union : 백엔드와 프론트엔드 개발자 합집합
# {'Linda', 'Mary', 'David', 'James'}
print(backend_engineer | frontend_engineer)
print(backend_engineer.union(frontend_engineer))

# 백엔드와 프론트엔드 개발자 차집합
# 백엔드는 할 수 있지만, 프론트는 못 하는 개발자 = {'Linda'}
print(backend_engineer - frontend_engineer)
print(backend_engineer.difference(frontend_engineer))
# 프론트는 할 수 있지만, 백엔드는 할 수 없는 개발자 = {'David', 'Mary'}
print(frontend_engineer - backend_engineer)
print(frontend_engineer.difference(backend_engineer))

# frontend_engineer 추가
frontend_engineer.add("Linda")
print(frontend_engineer)  # {'Linda', 'Mary', 'James', 'David'}

# frontend_engineer 삭제
frontend_engineer.remove("James")
print(frontend_engineer)  # {'Linda', 'Mary', 'David'}
