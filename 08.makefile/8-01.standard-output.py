import sys
# stdout : 표준 출력
print("Python", "C++", "Java", file=sys.stdout)  # Python C++ Java
# stderr : 표준 에러 처리 - 필요 시 따로 에러 처리
print("Python", "C++", "Java", file=sys.stderr)  # Python C++ Java

# sep : 단어 사이에 sep=" " 따옴표 안의 문자를 넣어줄 수 있다.
print("Python", "C++", "Java", sep=", ")  # Python, C++, Java
print("Python", "C++", "Java", sep=" vs ")  # Python vs C++ vs Java

# end : 문장의 끝 부분을 end=" " 따옴표 안의 문자를 넣어주고, 문장이 줄바꿈 되지 않은 채 다음 문장이 한 문장으로 출력된다.
print("Python", "C++", sep=", ", end="? ")
print("무엇이 더 재미있을까요?")
# Python, C++? 무엇이 더 재미있을까요?


# 시험 성적
scores = {"수학": 0, "영어": 50, "국어": 100}
for subject, score in scores.items():
    # ljust(n) : n칸 공간을 확보하고 왼쪽 정렬
    # rjust(n) : n칸 공간을 확보하고 오른쪽 정렬
    print(subject.ljust(4), str(score).rjust(4), sep=":")
    # 수학  :   0
    # 영어  :  50
    # 국어  : 100


# 은행 대기 순번 표
# 001, 002, 003, ...
for num in range(1, 5):
    # .zfill(n) : n칸 공간을 확보하고 남은 공간에 0을 넣기
    print("대기 번호 : " + str(num).zfill(3))
    # 대기 번호 : 001
    # 대기 번호 : 002
    # 대기 번호 : 003
    # 대기 번호 : 004
