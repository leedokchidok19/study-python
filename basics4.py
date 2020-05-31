#분기문(if, for, while, continue, break, 한 줄 for)
#if
print("if문")
# weather = "맑아"
weather = input("오늘 날씨는 어때요? ")    # input 사용자 입력을 받아준다. 한 칸 공백을 준 이유는 끝을 기준으로 입력 커서가 생긴다.
if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")
    
temp = int(input("기온은 어때요? "))   # input 사용자 입력을 받아준다. 한 칸 공백을 준 이유는 끝을 기준으로 입력 커서가 생긴다.
if 30 <= temp :
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp  < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")

#for - 반복문
print("\n반복문 for")
# for waiting_no in [0, 1, 2, 3, 4]:
# for waiting_no in range(5):    # 0, 1, 2, 3, 4
for waiting_no in range(1, 6):   # 1-5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

#while - 반복문
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")
        
# customer = "아이언맨"
# index = 1
# while True:    #무한루프
#    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
#    index += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
    
#continue, break
print("\ncontinue, break")
asent = [2, 5]    # 결석
no_book = [8]     # 책이 없음
for student in range(1, 11):    # 1-10
    if student in asent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지 {0}는 교무실로".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# 한 줄 for문
print("\n한 줄 for문")
# 출석 번호가 1 2 3 4 5 앞에 100을 붙이기로 함 -> 101 102 103 104 105
student = [1, 2, 3, 4, 5]
print(student)
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
student = ["Iron man", "Thor", "I am groot"]
print(student)
student = [len(i) for i in student]
print(student)

# 학생 이름을 대문자로 변환
student = ["Iron man", "Thor", "I am groot"]
print(student)
student = [i.upper() for i in student]
print(student)
