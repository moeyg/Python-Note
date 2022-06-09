# 지역 변수(Local Variable)
# 함수 내에서만 사용이 가능한 변수
# 함수가 호출될 때 생성되다가 함수가 호출이 끝나면 사라짐

# 전역 변수(Global Variable)
# 모든 공간에서 부를 수 있는 변수

book = 10  # 전역 변수


def library(students):
    global book  # 전역 공간에 있는 book 사용
    book = book - students
    print("[도서관] 대여 불가 책 : {0}".format(book))


print("도서관 전체 책 : {0}".format(book))
library(2)
print("대여 가능한 책 : {0}".format(book))
print()

# --------------------------------------------- #

book = 10  # 전역 변수


def library_return(book, students):  # book : 지역변수
    book = book - students
    print("[도서관] 대여 불가 책 : {0}".format(book))
    return book


print("도서관 전체 책 : {0}".format(book))  # 전역 변수 book의 개수 20
book = library_return(book, 2)  # (전역 변수 book의 개수 20, 2)
print("대여 가능한 책 : {0}".format(book))  # return 받은 book
