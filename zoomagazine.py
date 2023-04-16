# Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и котки. 
# Храната се пазарува от зоомагазин,
# като една опаковка храна за кучета е на цена 2.50 лв,
# а опаковка храна за котки струва 4 лв.

# От конзолата се четат 2 реда:
# 1.	Броят на опаковките храна за кучета – цяло число в интервала [0… 100]
# 2.	Броят на опаковките храна за котки –  цяло число в интервала [0… 100]
# Изход
# На конзолата се отпечатва: 


dog_food_packages = int(input("How many packages of dog food"))
dog_food_price = dog_food_packages * 2.50
cat_food_packages = int(input("How many packages of cat food"))
cat_food_price = cat_food_packages * 4
total = dog_food_price + cat_food_price
print(total)

