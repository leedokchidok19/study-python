# 함수, 전달 값과 반환 값, 기본값, 키워드 값, 가변인자, 지역변수, 전역변수
print("\n함수")
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

#전달 값과 반환 값
print("\n전달 값과 반환 값")
# 입금
def deposit(balance, money):
    print("입금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance+money

#출금
def withdraw(balance, money):
    if balance >= money:    # 잔액이 출금보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

#저녁에 출금
def withdraw_night(balance, money):
    commission = 100    # 수수료 100원
    return commission, balance - money - commission


balance = 0    # 잔액
balance =deposit(balance, 1000)
print(balance)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)    # 튜플 구조
print("수수료는 {0} 원이며, 잔액은 {1} 원 입니다.".format(commission, balance))

# 기본값
print("\n기본값")
# 기본값 사용 전
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
         .format(name, age, main_lang))
    
profile("유재석", 25, "파이썬")
profile("김태호", 20, "자바")

# 기본값 사용 후
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
         .format(name, age, main_lang))
    
profile("유재석")
profile("김태호")

# 키워드 값 - 매개 변수의 순서가 달라질 떄 사용
# 순서가 바뀌어도 문제 없이 나온다.
print("\n키워드 값")
profile(main_lang="C", name="조태호", age=28)

#가변인자 - 가변적으로 변하는 매개 변수를 사용해야 할 때
print("\n가변인자")
# 가변인자 사용 전
def profile2(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")    #print에 end=" "를 넣어주면 다음 print가 같은 줄에 나온다.
    print(lang1, lang2, lang3, lang4, lang5)
    
profile2("유재석", 20, "python", "java", "C", "C++", "C#")
profile2("김태호", 25, "kotlin", "swuft", "", "", "")

# 가변인자 사용 후
def profile2(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")    #print에 end=" "를 넣어주면 다음 print가 같은 줄에 나온다.
    for lang in language:
        print(lang, end=" ")
    print()
    
profile2("유재석", 20, "python", "java", "C", "C++", "C#", "javascript")
profile2("김태호", 25, "kotlin", "swuft")

#지역변수, 전역변수
#지역변수 : 함수 내에서만 사용가능한 변수
gun = 10
def checkpoint(soldiers):
    gun =20    # 없으면 에러가 나온다.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))    # 10
checkpoint(2)                        # 18
print("전체 총 : {0}".format(gun))    # 10

#전역변수 : 프로그램 내에서 어디든 사용 가능한 변수
gun = 10
def checkpoint(soldiers):
    global gun    # 전역 공간에 있는 gun 사용.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ref(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun    # return을 안 하면 gun 값이 변하지 않는다.
    
print("전체 총 : {0}".format(gun))    # 10
# checkpoint(2)                      # 8
gun = checkpoint_ref(gun, 2)         # return 받은 값을 다시 저장해야만 gun값이 변한다.
print("전체 총 : {0}".format(gun))    # 8