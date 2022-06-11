# Quiz) 행맨 게임 프로그램

# [조건]
# 1. 리스트에 3개 이상의 단어를 추가
# 예) apple, banana, orange

# 2. 위 리스트에서 랜덤으로 1개의 단어를 선택

# 3. 단어의 길이에 맞게 밑줄 출력
# 예) apple의 경우 _ _ _ _ _

# 4. 사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct' 출력, 아니면 'Wrong' 출력

# 5. 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시 (맞히지 못 한 글자는 밑줄 출력)
# 예) a 입력 시 : a _ _ _ _
#     p 입력 시 : a p p _ _
#     c 입력 시 : a p p _ _

# 6. 정답을 맞히면 Succeed 출력 후 프로그램 종료 (단, 횟수 제한은 없음)

from random import *

words = ["apple", "watermelon", "strawberry", "grape", "pear", "peach"]
word = choice(words)

letters = ""

while True:
    succeed = True

    print()

    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False

    print()

    if succeed:
        print("\n🎊 Succeed!! 🎊\n")
        break

    letter = input("Input letter >> ")

    if letter not in letters:
        letters += letter

    if letter in word:
        print("\n⭕️ Correct! ⭕️")
    else:
        print("\n❌ Wrong! ❌")
