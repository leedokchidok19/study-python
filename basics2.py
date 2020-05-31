# 숫자 함수(mathm random), 슬라이싱,
# 문자열 함수(lower, upper, isupper, replace, index, find, count),
# 문자열 포맷, 탈출문자(이스케이프)

# 숫자 함수
print("\n숫자 함수")
print(abs(-5))        # 5
print(pow(4, 2))      # 4^2 = 4*4 = 16
print(max(1, 3))      # 3
print(min(1, 3))      # 1
print(round(3.141))   # 3
print(round(5.926))   # 6

# math
from math import *
print()
print(floor(5.926))   # 5 반내림
print(ceil(5.926))    # 6 반올림
print(sqrt(9))        # 3 제곱근

# 랜덤
from random import *
print("\n랜덤")
print(random())                 # 0.0 ~ 1.0 미만 임의 값
print(random() * 10)            # 0.0 ~ 10.0 미만 임의 값
print(int(random() * 10))       # 0 ~ 10 미만 임의 값
print(int(random() * 10)+1)     # 1 ~ 10 이하 임의 값

print()
print(randrange(1, 31))         # 1 ~ 31 미만 임의 값
print(randint(1, 30))           # 1 ~ 30 이하 임의 값
print(randrange(7, 15))         # 7 ~ 15 미만 임의 값
print(randint(7, 14))           # 7 ~ 14 이하 임의 값

# 슬라이싱
print("\n슬라이싱")
socialNumber = "200522-1234567"
print("성별 : "+socialNumber[7])          # 1 시작은 1이 아닌 0부터 시작
print("연도 : "+socialNumber[0:])         # 200522-1234567 0 ~ 끝까지 0:
print("출생연도 : "+socialNumber[0:2])     # 20 0 ~ 1 자리
print("출생월 : "+socialNumber[2:4])       # 05 2 ~ 3 자리
print("출생일 : "+socialNumber[4:6])       # 22 4 ~ 5 자리
print("출생일 : "+socialNumber[:6])        # 200522 0 ~ 5 자리
print()

print("뒷자리 : "+socialNumber[-7:])        # 1234567 7 ~ 14 자리 뒤를 기준으로 7자리

# 문자열 함수
print("\n문자열 함수")
message = "EveryDay Study Python"
print(message.lower())                    # 문자열 소문자로 변환 everyday study python
print(message.upper())                    # 문자열 대문자로 변환 EVERYDAY STUDY PYTHON
print(message[0].isupper())               # 대문자 확인 True
print(len(message))                       # 문자열 길이 21
print(message.replace("Python", "Java"))  # 문자열 치환 Python -> Java

index = message.index("y")
print(index)
index = message.index("y", index + 1)    # index 사용시 찾는 문자열이 없으면 error
print(index)

print(message.find("1"))                 # index 반대 찾는 문자열이 없으면 -1 return

print(message.count("y"))                # "y"가 message안에 몇번 있는지 count

# 문자열 포맷
print("\n문자열 포맷")
print("a"+"b")                           # ab
print("a", "b")                          # a b ,사용은 공백을 붙여준다.

# 방법 1
print("오늘 날짜는 %d 입니다." % 20200522)
print("%s을 배우고 있습니다." % "Python")
print("\"학교\"의 첫글자는 %c 입니다." % "학")

print("좋아하는 색은 %s과 %s입니다." % ("빨간색", "노란색"))

# 방법 2
print("오늘 날짜는 {} 입니다.".format(20200522))
print("{}과 {}를 배우고 있습니다.".format("Python", "Java"))
print("{1}과 {0}를 배우고 있습니다.".format("Python", "Java"))

# 방법 3
print("{date}년 {lang}을 배우고 있습니다.".format(lang = "Python", date = 2020))

# 방법 4 (v3.6 이상)
lang = "Python"
date = 2020
print(f"{date}년 {lang}을 배우고 있습니다.")

# 탈출문자(이스케이프)
print("\n탈출문자(이스케이프)")
# \n : 줄바꿈
print("첫 번째 줄\n두 번째 줄 입니다.\n 줄바꿈은 \\n입니다.")
# \t : 탭
print("첫 번째 줄\t두 번째 줄 입니다. 탭은 \\t입니다.")
# \" \' : 문장 안의 따옴표
print("문장 큰 따옴표 \"따옴표\" 사용법입니다.")
print("문장 작은 따옴표 \'따옴표\' 사용법입니다.")
# \\ : 문장 안의 \
print("문장에서 \\사용법 \\을 두번 붙이면 됩니다.")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스(한 글자 삭제) 영어, 숫자만 지운다. 한글은 삭제가 안된다.
print("Pined\b Apple")