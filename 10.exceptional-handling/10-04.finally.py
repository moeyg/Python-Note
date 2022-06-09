# finally
# 예외 처리 구문에서 정상적 / 오류 상관 없이 무조건 실행되는 구문
# try 문 내에서 마지막에 사용

class BigNumberError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)  # 입력값 : num1, num2
finally:
    print("copyright : @moeyg")
