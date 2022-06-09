# 클래스

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
# 마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5

marine2 = Unit("마린", 40, 5)
# 마린 유닛이 생성되었습니다.
# 체력 40, 공격력 5

tank = Unit("탱크", 150, 35)
# 탱크 유닛이 생성되었습니다.
# 체력 150, 공격력 35
