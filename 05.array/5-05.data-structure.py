# 자료구조의 변경
cafe_menu = {"Americano", "Tea", "Smoothie"}
print(cafe_menu, type(cafe_menu))
# {'Smoothie', 'Americano', 'Tea'} <class 'set'>

cafe_menu = list(cafe_menu)
print(cafe_menu, type(cafe_menu))
# ['Smoothie', 'Americano', 'Tea'] <class 'list'>

cafe_menu = tuple(cafe_menu)
print(cafe_menu, type(cafe_menu))
# ('Americano', 'Smoothie', 'Tea') <class 'tuple'>

cafe_menu = set(cafe_menu)
print(cafe_menu, type(cafe_menu))
# {'Americano', 'Tea', 'Smoothie'} <class 'set'>
