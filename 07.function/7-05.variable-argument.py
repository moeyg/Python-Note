def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # end = " " : 다음으로 출력될 문장이 줄바꿈 되지 않고 출력 된다.
    print(lang1, lang2, lang3, lang4, lang5)


profile("James", 20, "C", "C++", "Java", "Python", "Go")
profile("Paul", 21, "C", "C#", "", "", "")


# 가변 인자 (Variable Argument)
# 서로 다른 개수의 값을 같은 인자를 넣어줄 때는 가변 인자를 사용한다. *argument


def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()  # 줄바꿈


profile("James", 20, "C", "C++", "Java", "Python", "Go", "JavaScript")
profile("Paul", 21, "C", "C#")
