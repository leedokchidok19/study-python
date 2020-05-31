# 메소드, 상속, 다중 상속, 메소드 오버라이딩, pass, supper
# 메소드
print("메소드")
class Unit:
    def __init__(self, name, hp, damage):    # __init__ : 생성자
        self.name = name     # 멤버 변수
        self.hp = hp         # 멤버 변수
        self.damage = damage # 멤버 변수
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

#공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name     # 멤버 변수
        self.hp = hp         # 멤버 변수
        self.damage = damage # 멤버 변수
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [ 공격력 {2}]"\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다."\
              .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다."\
              .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염 방사기
firebat1 = AttackUnit("파이엇뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 상속
print("\n상속")
class Unit:    # 부모 클래스
    def __init__(self, name, hp, speed):    # __init__ : 생성자
        self.name = name     # 멤버 변수
        self.hp = hp         # 멤버 변수
        self.speed = speed	 # 멤버 변수


    def move(self, location):
        print("지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
              .format(self.name, location, self.speed))

#공격 유닛
class AttackUnit(Unit):    # 자식 클래스
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage # 멤버 변수
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [ 공격력 {2}]"\
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다."\
              .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다."\
              .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#상속후 동일한 결과 출력
# 파이어뱃 : 공격 유닛, 화염 방사기
firebat1 = AttackUnit("파이엇뱃", 50, 5, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 다중 상속
print("\n다중 상속")
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
# 다중 상속 , 를 붙이면 된다.
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)	# 지상 스피드는 0
        Flyable.__init__(self, flying_speed)
	#오버라이딩
    def move(self, location):	# 상속받은 fly 함수를 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

#발키리 : 공중 공격 유닛
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

#벌쳐 : 지상 유닛
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀 크루져 : 공중 유닛
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시") 오버라이딩 전
battlecruiser.move("9시")

# pass
print("\npass")
# 건물
class BuildingUnit(Unit):
	def __init__(self, name, hp, location):
		pass	# 미구현이지만 넘어간다.

# 서플라이 디폿 : 건물
supply_depot = BuildingUnit("서플라이 디폿", 500, "7")

def game_start():
	print("[알림] 새로운 게임을 시작합니다.")

def game_over():
	pass

game_start()
game_over()

# super
print("\nsuper")
class BuildingUnit(Unit):	# supper 사용 전
	def __init__(self, name, hp, location):
		Unit.__init__(self, name, hp, 0)
		self.location = location

class BuildingUnit(Unit):	# supper 사용 후
	def __init__(self, name, hp, location):
		supper.__init__(self, name, hp, 0)	# 단일 상속에만 사용을 권장, 다음 생성자가 상속이 안 된다.
		self.location = location