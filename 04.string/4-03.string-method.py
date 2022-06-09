# 문자열 처리 함수

text = "Hello World!"

# lower : 소문자로 변환
print(text.lower())  # hello world!
# upper : 대문자로 변환
print(text.upper())  # HELLO WORLD!

# []번째 문자열이 대문자인가?
print(text[0].isupper())  # True
# []번째 문자열이 소문자인가?
print(text[4].isupper())  # False

# 문자열의 길이 반환
print(len(text))  # 12

# 문자 변환
# .replace("World", "Python") : "World"를 찾아 "Python"로 변환
print(text.replace("World", "Python"))

# 문자 위치 - 1
# .index("o") : "o" 라는 글자가 몇 번째에 위치하고 있는지 반환
index = text.index("o")  # 첫 번째 "o" 위치
print(index)  # 4
index = text.index("o", index + 1)  # 두 번째 "o" 위치
print(index)  # 7
# 만약 문자열에 원하는 문자가 없다면, error
# print(text.index("Java"))

# 문자 위치 - 2
# .find("o") : "o" 라는 글자가 몇 번째에 위치하고 있는지 반환
print(text.find("o"))
# 만약 문자열에 원하는 문자가 없다면, -1 반환
print(text.find("C++"))  # -1

# 문자 개수
# .count("o") : 문자열에 "o" 라는 글자가 몇 개 있는지 반황
print(text.count("o"))  # 2
