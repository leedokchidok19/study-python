# 사용자 정의 예외처리 - python exception/exception_custom.py
class BigNumberError(Exception):
    # pass
    # 에러 발생시 메시지 생성
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

print("사용자 정의 예외처리") 
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요. : "))
    num2 = int(input("두 번째 숫자를 입력하세요. : "))
    if num1 >= 10 or num2 >= 10:
        #raise BigNumberError # 사용자 정의 예외처리
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))# 에러 발생 메시지 추가
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("ValueError : 잘못된 값을 입력하였습니다.\n한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다.\n한 자리 숫자만 입력하세요.")
    print(err)