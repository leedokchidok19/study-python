# 리스트[], 사전 튜플, 세트, 자료구조의 변경

# 리스트[] - 내용 변경 추가 가능
print("리스트[]")
subway = [10, 20 ,30]       # 숫자
print(subway)               # [10, 20, 30]
subway = ["유재석", "조세호" ,"박명수"]    # 문자
print(subway)                

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))    # 1

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # 하하 추가
print(subway)    # ['유재석', '조세호', '박명수', '하하']

#정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")    # insert(넣을 위치, 넣을 값)
print(subway)                # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼내고 지운다.
subway.pop()     # 맨 뒤의 값을 지운다.
print(subway)    # ['유재석', '조세호', '박명수']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)    # 2
print(subway.count("유재석"))    # count(넣을 값) 리스트 안에 있는 넣은 값의 갯수

# 정렬
num_list = [5, 1, 2, 4, 3]
num_list.sort()    # 값 정렬
print(num_list)    # [1, 2, 3, 4, 5]

# 순서 거꾸로
num_list.reverse()
print(num_list)    # [5, 4, 3, 2, 1]
 
# 모두 지우기
num_list.clear()
print(num_list)    # []

# 다양한 자료형
mix_list = ["조세호", 20, True]
print(mix_list)    # ["조세호", 20, True]

#리스트확장
num_list = [6, 7, 8, 9, 10]
num_list.extend(mix_list)
print(num_list)    # [6, 7, 8, 9, 10, '조세호', 20, True]

# 사전
print("\n사전")
# 사전 선언 및 값 가져오기
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet.get(3))
# 없는 값을 가져올시 차이
#print(cabinet[5])    # 에러
print(cabinet.get(5))# None
print(cabinet.get(5, "사용가능"))# 사용가능
# 사전안에 값이 있는지 확인
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])    # 유재석
print(cabinet["B-100"])  # 김태호
# 값 추가
cabinet["A-3"]    = "김종국"
cabinet["C-20"]  = "조세호"
print(cabinet)     # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}
# 값 제거
del cabinet["A-3"] # {'A-3': '김종국'} 삭제
print(cabinet)     # {'B-100': '김태호', 'C-20': '조세호'}
# Key값만 출력
print(cabinet.keys())    # dict_keys(['B-100', 'C-20'])
# value값만 출력
print(cabinet.values())  # dict_values(['김태호', '조세호'])
# Key, value 같이 출력
print(cabinet.items())   # dict_items([('B-100', '김태호'), ('C-20', '조세호')])
# 값 모두 제거
cabinet.clear()
print(cabinet)    # {}

# 튜플 - 내용 변경, 추가 불가 단 속도가 리스트보다 빨라서 상수값을 사용할 때 이용
print("\n튜플")
menu = ("돈까스", "치즈까스")
print(menu[0])
# menu.add("생선까스")    # 에러 추가불가
# 여러개 한꺼번에 선언
# 기존 방식
# name = "김종국"
# age = 20
# hobby = "코딩"
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

#세트(set) - 집합, 중복 안됨, 순서 없음
print("\n세트")
my_set = {1, 2, 3, 3, 3}
print(my_set)        # {1, 2, 3}
java = {"유재석", "김태호", "양세형"}    # 세트 선언 방법 1
python = set(["유재석", "박명수"])      # 세트 선언 방법 2

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)                # {'유재석'}
print(java.intersection(python))    # {'유재석'}

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)         # {'김태호', '유재석', '양세형', '박명수'}
print(java.union(python))    # 순서는 보장하지 않음

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)            # {'김태호', '양세형'}
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)          # {'김태호', '유재석', '박명수'}

# java 를 잊었어요
java.remove("김태호")
print(java)            # {'유재석', '박명수'}

#자료구조의 변경
print("\n자료구조의 변경")
menu = {"커피", "우유", "주스"}    # set
print(menu, type(menu))          # <class 'set'>

menu = list(menu)                # set to list
print(menu, type(menu))          # <class 'list'>

menu = tuple(menu)               # list to tuple
print(menu, type(menu))          # <class 'tuple'>

menu = set(menu)                 # tuple to set
print(menu, type(menu))          # <class 'set'>
