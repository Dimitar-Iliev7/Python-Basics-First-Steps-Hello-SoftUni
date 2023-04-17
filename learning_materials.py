# Учебната година вече е започнала и отговорничката на 10Б клас - 
# Ани трябва да купи определен брой пакетчета с химикали, пакетчета с маркери, 
# както и препарат за почистване на дъска. Тя е редовна клиентка на една книжарница,
# затова има намаление за нея, което представлява някакъв процент от общата сума. 
# Напишете програма, която изчислява колко пари ще трябва да събере Ани, за да плати сметката,
# като имате предвид следния ценоразпис: 
# •	Пакет химикали - 5.80 лв. 
# •	Пакет маркери - 7.20 лв. 
# •	Препарат - 1.20 лв (за литър)
# Вход
# От конзолата се четат 4 числа:
# •	Брой пакети химикали - цяло число в интервала [0...100]
# •	Брой пакети маркери - цяло число в интервала [0...100]
# •	Литри препарат за почистване на дъска - цяло число в интервала [0…50]

from math import floor


num_of_pen_packages = int(input())
num_of_marker_packages = int(input())
litters_of_washer = int(input())
percent_of_discount = int(input())

price_of_pens = num_of_pen_packages * 5.80
price_of_markers = num_of_marker_packages * 7.20
price_of_washer = litters_of_washer * 1.20

price_of_all_materials = price_of_pens + price_of_markers + price_of_washer

price_with_discount = price_of_all_materials - (price_of_all_materials * percent_of_discount)

print(floor(price_with_discount))

