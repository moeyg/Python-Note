class AmericaPackage:
    def detail(self):
        print("[미국 패키지 10박 12일] LA, 디즈니랜드 300만원")


if __name__ == "__main__":
    print("America 모듈을 직접 실행")
    trip_to_america = AmericaPackage()
    trip_to_america.detail()
else:
    print("America 외부에서 모듈 호출")

# America 모듈을 직접 실행
# [미국 패키지 10박 12일] LA, 디즈니랜드 300만원


# 만약 외부에서 모듈을 사용할 경우,

# America 외부에서 모듈 호출
# [미국 패키지 10박 12일] LA, 디즈니랜드 300만원
