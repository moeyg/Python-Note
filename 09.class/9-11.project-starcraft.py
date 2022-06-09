from random import *


class Unit:  # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.\n".format(self.name))

    # 유닛 이동 메서드
    def move(self, location):
        print("[{0} 유닛 이동]".format(self.name))
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]\n"
              .format(self.name, location, self.speed))

    # 공격 받을 시 데미지 감소 메서드
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.\n".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.\n".format(self.name))


class AttackUnit(Unit):  # 지상 공격 유닛(AttackUnit)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    # 공격 메서드
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [데미지 : {2}]\n"
              .format(self.name, location, self.damage))


class FlyableUnit(Unit):  # 공중 유닛(FlyableUnit)
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    # 비행 메서드
    def fly(self, name, location):
        print("[{0} 유닛 이동]".format(name))
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]\n"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit(FlyableUnit, AttackUnit):  # 공중 공격 유닛(FlyableAttackUnit)
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        FlyableUnit.__init__(self, flying_speed)

    # 비행 방향 메서드
    def move(self, location):
        self.fly(self.name, location)


# 지상 유닛 생성

class Marine(AttackUnit):  # 마린 유닛 - AttackUnit 상속
    def __init__(self):
        AttackUnit.__init__(self, "마린(👮)", 40, 1, 5)

    # 스팀팩 메서드 : hp -10 으로 일정 시간 동안 공격력, 속도 증가
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. [HP -10]\n".format(self.name))
        else:
            print("{0} : 스팀팩을 사용할 수 없습니다. [현재 체력 : {1}]\n"
                  .format(self.name, self.hp))


class Tank(AttackUnit):  # 탱크 유닛 - AttackUnit 상속
    seize_developed = False  # 시즈 모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크(🚓)", 150, 1, 35)
        self.seize_mode = False

    # 시즈 모드 : 탱크를 지상에 고정시켜 더 높은 파워로 공격 가능, 이동 불가
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈 모드가 아닐 때 -> 시즈 모드
        if self.seize_mode == False:
            print("{0} : 시즈 모드로 전환합니다.\n".format(self.name))
            self.damage *= 2
            self.speed = 0
            self.seize_mode = True
        # 현재 시즈 모드일 때 -> 시즈 모드 해제
        else:
            print("{0} : 시즈 모드를 해제합니다.\n".format(self.name))
            self.damage /= 2
            self.seize_mode = False


# 공중 유닛 생성

class Wraith(FlyableAttackUnit):  # 레이스 유닛 - FlyalbeAttackUnit 상속
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스(🚁)", 80, 20, 5)
        self.clocked = False  # 크로킹 모드 해제 상태

    def clocking(self):
        # 현재 클로킹 모드일 때 -> 모드 해제
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.\n".format(self.name))
            self.clocked = False
        # 현재 클로킹 모드가 아닐 때 -> 클로킹 모드
        else:
            print("{0} : 클로킹 모드 설정합니다.\n".format(self.name))
            self.clocked = True


def game_start():  # 게임 시작 함수
    print("[알림] 새로운 게임을 시작합니다!\n")


def game_over():  # 게임 종료 함수
    print("Player : GG")
    print("[알림] Player 님이 게임을 떠났습니다.")


# 게임 시작
game_start()

# 마린 3기 생성
marine1 = Marine()
marine2 = Marine()
marine3 = Marine()

# 탱크 2기 생성
tank1 = Tank()
tank2 = Tank()

# 레이스 1기 생성
wraith = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(marine1)
attack_units.append(marine2)
attack_units.append(marine3)
attack_units.append(tank1)
attack_units.append(tank2)
attack_units.append(wraith)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈 모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.\n")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈 모드, 레이스 : 클로킹)
# isinstance(instance, Class) : instance가 class인지 확인
for unit in attack_units:
    # unit이 Marine 클래스의 인스턴스
    if isinstance(unit, Marine):
        unit.stimpack()
    if isinstance(unit, Tank):
        unit.set_seize_mode()
    if isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
# 랜덤 데미지 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))

# 게임 종료
game_over()
