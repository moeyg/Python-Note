# open("file_name", "w(write : 쓰기)", encoding="utf8")
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 100", file=score_file)
score_file.close()

# open("file_name", "a(append : 이어서 쓰기)", encoding="utf8")
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n국어 : 50")
score_file.close()

# open("file_name", "r(read)", encoding="utf8")
score_file = open("score.txt", "r", encoding="utf8")
# 파일의 모든 내용 읽기
print(score_file.read())
# 수학 : 0
# 영어 : 100
# 과학 : 80
# 국어 : 50


# 한 줄씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
# 한 줄  읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline(), end="")
score_file.close()
# 수학 : 0

# 영어 : 100


# 내용이 어느 정도인 지 모를 때
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()
# 수학 : 0

# 영어 : 100

# 과학 : 80

# 국어 : 50


# list에 값을 넣어 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line)
score_file.close()
# 수학 : 0

# 영어 : 100

# 과학 : 80

# 국어 : 50
