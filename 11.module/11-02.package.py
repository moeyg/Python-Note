# 패키지
# 여러 모듈 파일을 모아둔 집합

# 패키지(travel) 속 모듈(america, france, japan) 사용하는 방법

# import 맨 뒤에는 모듈이나 패키지만 가능하다.
# 클래스나 함수를 작성할 수 없다.
import travel.america

# from 패키지 import 모듈로 사용 가능하다.
from travel import france

# from 패키지.모듈 import 클래스는 가능하다.
from travel.japan import JapanPackage

# import 패키지.모듈 로 가져올 경우
# variable = 패키지.모듈.클래스()
# variable.함수()
trip_to_america = travel.america.AmericaPackage()
trip_to_america.detail()  # [미국 패키지 10박 12일] LA, 디즈니랜드 300만원

# from 패키지 import 모듈 로 가져올 경우
# variable = 모듈.클래스()
# variable.함수()
trip_to_france = france.FrancePackage()
trip_to_france.detail()  # [프랑스 패키지 9박 11일] 파리 200만원

# from 패키지.모듈 import 클래스 로 가져올 경우
# variable = 패키지()
# variable.함수()
trip_to_japan = JapanPackage()
trip_to_japan.detail()  # [일본 패키지 여행 10박 12일] 오키나와 150만원
