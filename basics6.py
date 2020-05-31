# 입출력, 입출력 포맷
print("입출력")
# sep ","에 들어가는 값을 변경 할 수 있다. 기본은 " " 공백
print("java", "python", "javascript", sep=" vs ")
# end 문장에 들어가는 끝부분을 변경할 수 있다. 기본은 \n 줄바꿈
print("java", "python", "javascript", sep=" vs ", end="? ")
print("어떤 언어를 배우는 중 입니까?")

import sys
# 출력화면은 같다
print("java", "python", file = sys.stdout)    # 표준 출력
print("java", "python", file = sys.stderr)    # 표준 에러

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # just => justify 정렬 ljust(8) : 8칸의 여백 확보 후 왼쪽 정렬
    # rjust(4) : 4칸의 여백 확부 후 오른쪽 정렬
"""
수학      :   0
영어      :  50
코딩      : 100    
"""
# 은행 대기순번표
# 001 002 003...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))    # 대기번호 : 002, 대기번호 : 002
    #zfill(int) : int 숫자만큼의 크기를 만들고 빈공간은 0으로 채운다.

# input은 입력 값을 String으로 변환한다.
answer = input("아무 값이나 입력하세요. ")
print(type(answer))
print("입력하신 값은 "+ answer + "입니다.")

# 입출력 포맷
print("\n입출력 포맷")
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리의 공간을 확보
print("{0: >10}".format(500))     # "       500" 0:" " : 빈공간 > 오른쪽 정렬 10 : 10칸

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))    # "      +500"
print("{0: >+10}".format(-500))   # "      -500"

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))    # "+500______"
print("{0:_<10}".format(500))     # "500_______"

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))      # 100,000,000,000
# 3자리 마다 콤마를 찍어주고, +-부호 찍어주기
print("{0:+,}".format(100000000000))     # +100,000,000,000
print("{0:-,}".format(-100000000000))    # -100,000,000,000
# 3자리 마다 콤마를 찍어주고, +-부호 찍어주고, 자릿수 확보하기
# 빈 자리는 ^로 채우기
print("{0:^<+30,}".format(100000000000)) # +100,000,000,000^^^^^^^^^^^^^^

# 소수점 출력
print("{0}".format(5/3))      # 1.6666666666666667
print("{0:f}".format(5/3))    # 1.666667
# 소수점 특정 자리수까지만 표시(소수점 3자리에서 반올림)
print("{0:.2f}".format(5/3))  # 1.67






