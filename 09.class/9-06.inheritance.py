# 상속
# class 상속 받을 클래스(상속 클래스)
# class Child(Parent):
#       Parent.__init__(self, value)

class Unit:  # 일반 유닛
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class AttackUnit(Unit):  # 공격 유닛
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염 방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
# 파이어뱃 : 5시 방향으로 적군을 공격합니다. [공격력 : 16]

# 공격 2번 받는다고 가정
firebat1.damaged(25)
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 25 입니다.
firebat1.damaged(25)
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 0 입니다.
# 파이어뱃 : 파괴되었습니다.
