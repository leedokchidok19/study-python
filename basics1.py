# 자료형(int, String, boolean, 주석, 변수, 연산자)

# 자료형
# 숫자
print(5)       # 5
print(-10)     # -10
print(10.5)    # 10.5
print(15+20)   # 35

# 문자열
print('작은따옴표')          # 작은따옴표
print("큰따옴표")            # 큰따옴표
print('문자열곱하기'*2)      # 문자열곱하기문자열곱하기
print("문자열곱하기"*3)      # 문자열곱하기문자열곱하기문자열곱하기
sentencs = """
여러 문장을 큰 따옴표를
사용하면 담고
쓸 수 있습니다.
"""
print(sentencs)          # 여러 문장을 큰 따옴표를
                         # 사용하면 담고
                         # 쓸 수 있습니다.

# boolean 참/거짓
print(5 < 10)            # True
print(5 > 10)            # False
print(True)              # True
print(False)             # False
print(not (5 < 10))      # False
print(not True)          # False
print(not False)         # True

# 주석
'''
작은 따옴표 3개를 쓰면
 여러문장을 주석 처리 할 수 있다.
'''
"""
큰 따옴표 3개를 쓰면
 여러문장을 주석 처리 할 수 있다.
"""

# 변수선언
date = 20200522
day = "금요일"
isDay = day == "금요일"
print("오늘 날짜는 "+str(date)+" 입니다.")    # int str()을 사용해서 String으로 변환해야 한다.
print("오늘은 "+day+"입니다.")               #
print("금요일이 맞나요? "+str(isDay))         # boolean str()을 사용해서 String으로 변환해야 한다.

# 연산자
# 사칙연산
print(1 + 1)        # 2
print(2 - 1)        # 1
print(2 * 3)        # 6
print(4 / 2)        # 2.0
# 제곱근 나머지
print(2 ** 3)       # 8
print(4 % 2)        # 0
print(4 // 2)       # 2
# 비교연산자
print(3 > 2)         # True
print(2 >= 2)        # True
print(2 < 3)         # True
print(2 <= 2)        # True

print(4 == 2)        # False
print(4 == 2+2)      # True
print(4 != 2)        # True
print(not(1 != 2))    # False

print(3>0 and 3<2)    # 
print(3>0 & 3<2)      # 
print(3>0 or 3<2)    # 
print(3>0 | 3<2)     # 

# 수식
print(1 + 2 * 3)        # 7
print((1 + 2) * 3)      # 9
number = 1 + 2 * 3      # 7
print(number)

# number = 7 = 1 + 2 * 3
number += 2
print(number)          # 9
number -= 2
print(number)          # 7
number *= 2
print(number)          # 14
number /= 2
print(number)          # 7.0
number %= 2
print(number)          # 1.0
