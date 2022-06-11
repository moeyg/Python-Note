# * : 모든 요소를 사용하겠다는 뜻이지만, 실제로는 개발자가 문법 상에서 공개 범위를 설정해야 사용할 수 있다.
# 즉, __init__.py 파일 에서 공개/비공개를 설정할 수 있다.
# __init__.py 에서 __all__ = ["사용하려는 모듈"] 을 작성 후 사용할 수 있다.

from travel import *

trip_to_america = america.AmericaPackage()
trip_to_america.detail()  # [미국 패키지 10박 12일] LA, 디즈니랜드 300만원

trip_to_japan = japan.JapanPackage()
trip_to_japan.detail()  # [일본 패키지 여행 10박 12일] 오키나와 150만원
