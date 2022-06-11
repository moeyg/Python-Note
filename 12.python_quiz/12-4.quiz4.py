# Quiz) 신조어 퀴즈 클래스를 만드세요.

# [조건]
# Word 클래스 작성
# __init__(...): 신조어, 보기1, 보기2, 정답을 받아서 멤버 변수 설정
# show_question(...): 질문 내용 표시
# check_answer(...): 입력값이 정답인지 확인하여 "정답입니다" 또는 "틀렸습니다" 출력

# [주어진 프로그램 예제]
# word = Word("얼죽아", "얼어 죽어도 아이스아메리카노", "얼어 죽어도 아이스크림", 1)
# word.show_question()
# word.check_answer(int(input(">> ")))

# 3. 출력 결과
# '얼죽아' 의 뜻은?
# 1. 얼어 죽어도 아이스아메리카노
# 2. 얼어 죽어도 아이스크림
# >>

class Word:
    def __init__(self, neologism, example1, example2, answer):
        self.neologism = neologism
        self.example1 = example1
        self.example2 = example2
        self.answer = answer

    def show_question(self):
        print(f"'{self.neologism}' 의 뜻은?\n")
        print(f"1. {self.example1}")
        print(f"2. {self.example2}\n")

    def check_answer(self, user_answer):
        if user_answer == self.answer:
            print("정답입니다 🙌")
        else:
            print("틀렸습니다 🥺")


# word = Word("얼죽아", "얼어 죽어도 아이스아메리카노", "얼어 죽어도 아이스크림", 1)
# word = Word("어쩔TV", "어쩌고 저쩌고 TV", "어쩌라고 TV나 봐", 2)
word = Word("점메추", "점심 메뉴 추가", "점심 메뉴 추천", 2)

word.show_question()
word.check_answer(int(input(">> ")))
