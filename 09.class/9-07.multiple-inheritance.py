# 다중 상속
# 부모가 둘 이상의 상속
# 여러 곳에서 상속 받는 것

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


class Flyable:  # 비행 유닛 클래스
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):  # 공중 공격 유닛 클래스
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


#  발키리 : 공중 공격 유닛, 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 60, 5)
valkyrie.fly(valkyrie.name, "3시")  # 발키리 : 3시 방향으로 날아갑니다. [속도 5]
valkyrie.attack("3시")  # 발키리 : 3시 방향으로 적군을 공격합니다. [공격력 : 60]


# 드랍쉽 : 공중 유닛, 수송기, 공격 불가
dropship = Flyable(3)
dropship.fly("드랍쉽", "2시")  # 드랍쉽 : 2시 방향으로 날아갑니다. [속도 3]
