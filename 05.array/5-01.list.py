# 리스트 [ ]

subway = [10, 20, 30]
print(subway)  # [10, 20, 30]

subway = ["James", "Mary", "David"]
print(subway)  # ['Kim', 'Lee', 'Park']

# .index("Mary") : Mary 가 몇 번째 칸에 타고 있는지?
print(subway.index("Mary"))  # 1
# .index("David") : David 가 몇 번째 칸에 타고 있는지?
print(subway.index("David"))  # 2

# .append("Linda") : 다음 정거장에서 Linda 가 탄다면?
subway.append("Linda")
print(subway)  # ['James', 'Mary', 'David', 'Linda']

# .append("Paul") : 다음 정거장에서 Paul 이 Mary 와 David 사이에 탄다면?
subway.insert(2, "Paul")
print(subway)  # ['James', 'Mary', 'Paul', 'David', 'Linda']

# .pop() : 지하철에 있는 사람을 뒤에서 한 명씩 뒤에서 꺼냄
print(subway.pop())  # Linda
print(subway)  # ['James', 'Mary', 'Paul', 'David'] -> 마지막에 있던 Linda 빠짐
print(subway.pop())  # David
print(subway)  # ['James', 'Mary', 'Paul'] -> 마지막에 있던 David 빠짐

# .count("name") : 같은 이름의 사람이 몇 명 있는지 확인
subway.append("James")
print(subway)  # ['James', 'Mary', 'Paul', 'James']
print(subway.count("James"))  # 2

# .sort() : 정렬
num_list = [1, 9, 3, 5, 7, 6]
num_list.sort()
print(num_list)  # [1, 3, 5, 6, 7, 9]

# .reverse() : 뒤집어 정렬
num_list.reverse()
print(num_list)  # [9, 7, 6, 5, 3, 1]

# clear() : 모두 지우기
num_list.clear()
print(num_list)  # []

# 다양한 자료헝에 함께 사용
mix_list = ["James", 20, True]
print(mix_list)  # ['James', 20, True]

# 리스트 확장
num_list = [1, 9, 3, 5, 7, 6]
mix_list = ["James", 20, True]

num_list.extend(mix_list)
print(num_list)  # [1, 9, 3, 5, 7, 6, 'James', 20, True]

mix_list.extend(num_list)
print(mix_list)  # ['James', 20, True, 1, 9, 3, 5, 7, 6, 'James', 20, True]
