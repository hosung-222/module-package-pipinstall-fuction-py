# # 패키지 
# # 하나의 파일에 여러 모듈 집합
# import travel
# import tarvel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import * 
# from travel import *  #__init__.py 파일에 all사용필요
# # trip_to = vietnam.VietnamPackage()
# # trip_to.detail()

# trip_to =  thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
from travel import thailand
print(inspect.getfile(random))
print(inspect.getfile(thailand))