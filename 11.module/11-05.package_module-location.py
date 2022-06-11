# 패키지 / 모듈 위치 확인
# import inspect
# inspect.getfile(찾는 패키지 / 모듈)

import inspect
import random
from travel import *

# random 모듈의 위치를 알려줌
# /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/random.py
print(inspect.getfile(random))

# america 모듈의 위치를 알려줌
# /Users/moeyg/Desktop/Python-Basic/11.module/travel/america.py
print(inspect.getfile(america))
