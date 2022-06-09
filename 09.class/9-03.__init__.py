# __init__
# 생성자
# 객체가 만들어질 때 자동으로 호출되는 부분
# 인스턴스 : 클래스로부터 만들어진 객체

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


# 인스턴스
marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린") -> init에 맞게 값을 전달해 주어야 함
