# super
# 상속 받을 때 사용
# 상속 받는 부분에 self 를 작성하지 않는다.
# class Child(Parent):
#       super().__init__(value)

class Unit:  # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # 상속 방법 1. 상속 초기화
        # Parent.__init__(self, value)
        # Unit.__init__(self, name, hp, 0)

        # 상속 방법 2. super
        # super().__init__(value)
        super().__init__(name, hp, 0)
        self.location = location
        print("{0} : {1} 방향에 생성되었습니다. [HP : {2}]"
              .format(name, self.location, hp))


supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
print()
# 서플라이 디폿 : 7시 방향에 생성되었습니다. [HP : 500]


#####

# 다중 상속 시 super 주의!

class Unit2:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyalbeUnit(Unit2, Flyable):
    def __init__(self):
        super().__init__()


# 두 개 이상의 부모 클래스를 다중 상속 받을 경우, 맨 처음 상속 받는 부모 클래스만 init 호출
# 따라서 다중 상속 시, 모든 부모 클래스를 init 초기화하는 과정이 필요하다.
# class FlyalbeUnit(Unit2, Flyable):
#   def __init__(self):
#       Unit2.__init__(self)
#       Flyalbe.__init__(self)

dropship = FlyalbeUnit()  # Unit 생성자
