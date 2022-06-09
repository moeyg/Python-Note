# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하세요.

# 출력 예제
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 (준공 시기 : 2018년)
# 마포 빌라 전세 5억 (준공 시기 : 2020년)
# 송파 오피스텔 월세 1000/80 (준공 시기 : 2021년)

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} (준공 시기 : {4}년)"
              .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))


houses = []
gangnam = House("강남", "아파트", "매매", "10억", 2018)
mapo = House("마포", "빌라", "전세", "5억", 2020)
songpa = House("송파", "오피스텔", "월세", "1000/80", 2021)

# 배열 추가
houses.append(gangnam)
houses.append(mapo)
houses.append(songpa)

print("총 {}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
