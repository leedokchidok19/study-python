"""
# 방법 1
import module_example    # 방법 1 : 같은 폴더, 패키지일 경우 확장자 py 없이 import 파일명

module_example.price(3)
module_example.price_morning(4)
module_example.price_soldier(5)
"""
'''
# 방법 2
import module_example as m
# 방법 2 : import한 파일명이 길 경우 as를 붙이면 간단하게 사용 할 수 있다
m.price(3)
m.price_morning(4)
m.price_soldier(5)
'''
"""
# 방법 3
from module_example import *
# 방법 3 : 함수명을 직접적으로 바로 불러서 사용 가능하다.
price(3)
price_morning(4)
price_soldier(5)
"""
'''
# 방법 4
from module_example import price, price_morning
# 방법 4 : 필요한 함수만 불러서 사용 가능하다.
price(3)
price_morning(4)
# price_soldier(5) # import에 없어서 에러 NameError: name 'price_soldier' is not defined
'''
# 방법 5
from module_example import price_soldier as price
# 방법 5 : 필요한 함수만 부르고 as로 원하는 이름으로 사용 가능하다.
price(5)    # module_example의 price와 이름은 같지만 실제로는 price_soldier이다.
