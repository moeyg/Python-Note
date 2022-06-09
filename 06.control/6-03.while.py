# 반복문 (while)
# while (조건):

customer = "James"
index = 1
while index <= 5:
    print("{0} 님, 주문하신 음료 나왔습니다. - {1} 번째 호출".format(customer, index))
    index += 1
    if index == 6:
        print("주문하신 음료는 폐기하였습니다.")

# 무한 루프
# customer = "Mary"
# index = 1
# while True:
#     print("{0} 님, 주문하신 음료 나왔습니다. - {1} 번째 호출".format(customer, index))
#     index += 1

customer = "Paul"
person = "Unknown"

while person != customer:
    print("{0} 님, 주문하신 음료 나왔습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
    if person != customer:
        print("음료가 아직 나오지 않았어요 🥲")
    else:
        print("음료 여기 있습니다! 😊")
