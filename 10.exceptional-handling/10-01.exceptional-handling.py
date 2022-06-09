# 예외 처리
try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:  # int 값이 아닌 경우 에러 처리
    print("[ERROR] 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:  # 0을 입력할 경우 에러 처리
    print(err)  # 에러에 대한 내용 출력
except Exception as err:  # 위의 상황이 아닌 에러 상황
    print("[ERROR] 알 수 없는 에러가 발생하였습니다!")
    print(err)  # 에러에 대한 내용 출력
