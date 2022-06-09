# 마린 : 공격 유닛, 총
marine_name = "마린"  # 유닛의 이름
marine_hp = 40  # 유닛의 체력
marine_damage = 5  # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(marine_name))  # 마린 유닛이 생성되었습니다.
print("체력 {0}, 공격력 {1}\n".format(marine_hp, marine_damage))  # 체력 40, 공격력 5

# 탱크 : 공격 유닛, 포
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))  # 탱크 유닛이 생성되었습니다.
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))  # 체력 150, 공격력 35


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))


attack(marine_name, "1시", marine_damage)  # 마린 : 1시 방향으로 적군을 공격합니다. [공격력 5]
attack(tank_name, "1시", tank_damage)  # 탱크 : 1시 방향으로 적군을 공격합니다. [공격력 35]
