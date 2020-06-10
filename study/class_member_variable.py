# 클래스, 멤버변수
print("클래스")

print("클래스 사용전")
# 마린 : 공격 유닛, 군인. 총을 쓸 수 있음
name = "마린"    # 유닛의 이름
hp = 40         # 유닛의 체력
damage = 5      # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크 포를 쏠 수 있는데, 일반 모드 / 시즈모드
tank_name = "탱크"    # 유닛의 이름
tank_hp = 150         # 유닛의 체력
tank_damage = 35      # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

print("클래스 사용후")
class Unit:
    def __init__(self, name, hp, damage):    # __init__ : 생성자
        self.name = name     # 멤버 변수
        self.hp = hp         # 멤버 변수
        self.damage = damage # 멤버 변수
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

# 사용시 self를 제외한 인자만 넣어주면 된다.
marine1 = Unit("마린", 40, 5)    # Unit class의 인스턴스인 marine1 객체
marine2 = Unit("마린", 40, 5)    # Unit class의 인스턴스인 marine2 객체
tank = Unit("탱크", 150, 35)     # Unit class의 인스턴스인 tank 객체

#멤버변수
print("\n멤버변수")
# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True    # 새로운 변수를 넣을 수 있다.

if wraith2.clocking == True:    # wraith2는 clocking을 만들어줬지만 wraith1 없다.
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
#if wraith1.clocking == True:    # 에러
 #   print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
