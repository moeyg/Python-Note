# 조건문 (if)
# if 조건:
#     실행 명령문

wheater = input("오늘 날씨는 어때요? ")
if wheater == "비" or wheater == "눈":
    print("우산을 챙기세요! 😉")
elif wheater == "미세먼지":
    print("마스크를 챙기세요! 😷")
else:
    print("오늘의 날씨는 맑아요! 😆")

temp = int(input("오늘 기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요! 나가지 마세요 🥵")
elif 10 <= temp < 30:
    print("괜찮은 날씨예요. 😁")
elif 0 <= temp < 10:
    print("외투를 챙기세요. 🤧")
else:
    print("너무 추워요! 나가지 마세요. 🥶")
