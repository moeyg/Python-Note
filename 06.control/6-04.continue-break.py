# contine : 반복문에서 제외할 대상을 건너뛰고 반복문 실행
# break : break를 만나면 반복문 조건이 달성되지 않아도 탈출

absent = [2, 5]  # 결석
no_book = [10]  # 교과서를 안 가져온 학생
for student in range(1, 21):  # 출석번호 1 ~ 20
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}번은 교무실로 따라와!! 😡".format(student))
        break
    print("{0}번, 책을 읽어봐".format(student))
