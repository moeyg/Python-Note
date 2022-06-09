# 패스
# 에러가 발생하지 않고, 일단은 완성된 것처럼 넘어가는 의미

class Unit:  # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass


# 서플라이 디폿 : 건물, 1개 = 8 유닛
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass


game_start()  # [알림] 새로운 게임을 시작합니다.
game_over()
