# #모듈 

# import theater_module
# theater_module.price(3) #3명영화
# theater_module.prince_morning(4) #4명 조조할인영화
# theater_module.price_soldier(5) #5명 군인 영화

# import theater_module as mv
# mv.price(3)
# mv.prince_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# prince_morning(4)
# price_soldier(5)


# from theater_module import price, price_soldier, prince_morning
# price(5)
# prince_morning(6)
# #price_soldier(7) #오류발생

from theater_module import price_soldier as price
price(5) #군인 영화 가격으로 