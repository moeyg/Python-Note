# 외장 함수
# 직접 import를 해서 사용
# Google : list of python modules

# glob
import glob

# os
import os

# time
import time
import datetime


# glob : 경로 내의 폴더 / 파일 목록 조회 (dir과 유사)

print(glob.glob("*.py"))  # 확장자가 py인 모든 파일


# os : 운영체제에서 제공하는 기본 기능

print(os.getcwd())  # 현재 디렉토리 표시 /Users/moeyg/Desktop/Python-Basic
print(os.listdir())  # glob 과 비슷하게 사용
# ['01.hello-world', '07.function', '.DS_Store', '04.string', '03.operator', '10.exceptional-handling', '11.module', '05.array', '02.datatype', '09.class', '06.control', '08.makefile']

folder = "sample_dir"
if os.path.exists(folder):  # 만약 folder가 존재한다면
    print("이미 존재하는 폴더 입니다.")
    os.rmdir(folder)  # 폴더 삭제
    print("폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)  # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")


# time : 시간 관련 함수 제공

print(time.localtime())
# time.struct_time(tm_year=2022, tm_mon=6, tm_mday=10, tm_hour=23, tm_min=33, tm_sec=46, tm_wday=4, tm_yday=161, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# %Y(년)-%m(월)-%d(일) %H(시):%M(분):%S(초)
# 2022-06-10 Jun:35:39


# datetime : 날짜, 시간 함수 제공

print("오늘 날짜는 " + str(datetime.date.today()) + " 입니다.")
# 오늘 날짜는 2022-06-11 입니다.

# timedelta : 두 날짜 사이의 간격을 알려줌
today = datetime.date.today()  # 오늘 날짜 저장
days_later = datetime.timedelta(days=100)  # 100일 저장
print("우리가 만난 지 100일 뒤는? "+str(today + days_later)+"")
# 우리가 만난 지 100일 뒤는? 2022-09-19
