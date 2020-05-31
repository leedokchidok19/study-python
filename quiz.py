"""
5Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1 : 승객별 운행 소요 시간은 5분~ 50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[0] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2 분
"""
from random import *

cnt = 0    # 총 탑승 승객 수
for customer in range(1, 51):    # 1-50번째 승객
    minute = int(random()*50)+5
    check = " "
    if 5 <= minute <= 15:
        check = "0"
        cnt += 1
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(check, customer, minute, cnt))
    if customer == 50:
        print("총 탑승 승객 : %d 분" % cnt)
        
# 답
from random import *

cnt = 0    # 총 탑승 승객 수
for i in range(1, 51):    # 1-50이라는 수(승객)
    time = randrange(5,51)    #5-50분의 소요 시간
    if 5 <= time <= 15:    #5-15분 사이의 손님(매칭 성공), 탑승 승객 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:    # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

    print("총 탑승 승객 : %d 분" % cnt)


"""
6Quiz) 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) X 키(m) X 22
여자 : 키(m) X 키(m) X 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
조건 2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175 남자의 표준 체중은 67.38kg 입니다.
"""
height = 175
gender = "남자"

def std_weight(height, gender):
    value = 21
    if gender == "남자":
        value += 1
#    if gender == "여자":
        
        weight = round((height/100) * (height/100) * value, 2)
    print("키 {0} {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

std_weight(gender = "남자", height = 175)

# 답
def std_weight2(height, gender):    # 키 m 단위(실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

weight = round(std_weight2(height/100, gender), 2)
print("키 {0} {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

"""
7Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 "1주차.txt", "2주차.txt", "3주차.txt", ... 와 같이 만드시오.
"""
"""

for i in range(1, 51):
    with open(str(i)+"주차.txt", "w", encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
"""

"""
8Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 준공년도 2010년
마포 오피스텔 전세 5억 준공년도 2007년
송파 빌라 월세 500/50 2000년

[코드]
"""
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    #메물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
              , self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "매월세매", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 %d대의 매물이 있습니다." % len(houses))

for house in houses:
    house.show_detail()
    
"""
9Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
출력 메시지 : "잘못된 값을 입력하였습니다."
조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

[코드]

chicken = 10
waiting = 1    # 홀 안에는 현재 만석. 대기번호1부터 시작
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:    # 남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                  .format(waiting, order))
            waiting += 1
            chicken -= order
"""

class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1    # 홀 안에는 현재 만석. 대기번호1부터 시작
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:    # 남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                  .format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break    # while문 종료

"""
10Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오.

조건 : 모듈 파일명은 byme.py로 작성

(모듈 사용 예제)
import byme
byme.sign()

(출력 예제)
이 프로그램은 나도코딩에 의해 만들어졌습니다.
유튜브 : http://youtube.com
이메일 : nadocoding@gmail.com
"""
import byme
byme.sign()









