# 멤버 변수
# 클래스 내에 선언된 변수
# 클래스 Unit의 멤버 변수는 name, hp, damage

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


# 레이스 : 공중 유닛, 비행기, 클로킹
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 추가로 변수를 외부에서 만들어 객체에 쓸 수 있다.
# 하지만, 확장된 변수는 확장한 객체에 대해서만 적용이 되고 기존 객체는 적용 불가
# 적군 - 프로토스 : 마인드 컨트롤(상대방 유닛을 내 것으로 빼앗는 기술)
wraith2 = Unit("[clocking] 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태 입니다.".format(wraith2.name))
