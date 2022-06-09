# 방법 1

# 정수 포맷 (%d)
print("나는 %d살 입니다." % 10)

# 문자열 포맷 (%s)
print("나는 %s을 좋아합니다." % "Phython")
print("나는 %s와 %s 언어를 좋아합니다." % ("Phython", "C++"))

# 문자(1개) 포맷 (%c)
print("Python의 첫 글자는 %c 입니다." % "P")

print("%s %d %c!" % ("방법", 1, "끝"))
print()


# 방법 2
# .format : {} 안에 .format() 안의 값을 넣음
print("나는 {}살 입니다." .format(10))
print("나는 {}와 {} 언어를 좋아합니다." .format("Phython", "C++"))
print("나는 {1}와 {0} 언어를 좋아합니다." .format("Phython", "C++"))
print("나는 {0}와 {1} 언어를 좋아합니다." .format("Phython", "C++"))

print("{0} {2} {1}!" .format("방법", "끝", 2))
print()


# 방법 3
print("나는 {age}살이고, {language}를 좋아합니다." .format(age=10, language="Python"))
print("나는 {age}살이고, {language}를 좋아합니다." .format(language="Python", age=10))

print("{method} {number} {end}!" .format(method="방법", number=3, end="끝"))
print()


# 방법 4 (v3.6 이상~)
# 출력할 문자열 앞에 f 를 붙인다.
age = 10
language = "Python"
print(f"나는 {age}살이고, {language}를 좋아합니다.")

method = "방법"
number = 4
end = "끝"
print(f"{method} {number} {end}!")
