# alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = ('\'"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n"'
    '—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')

print(alice_in_wonderland)
                       
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for char in alice_in_wonderland:
    if char == "'":
        print(char)
         
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
Black_sea_area = 436402                               
Azov_sea_area  = 37800                                
Sea_areas = Black_sea_area + Azov_sea_area            
print(Sea_areas)                                      

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_inv_wh = 375291
first_second_wh = 250449
second_third_wh = 222950
# 3-й склад
third_wh = total_inv_wh - first_second_wh
# 2-й склад
second_wh = second_third_wh - third_wh
# 1-й склад
first_wh = first_second_wh - second_wh

print("На першому складі:", first_wh, "товарів.")
print("На другому складі:", second_wh, "товарів.")
print("На третьому складі:", third_wh, "товарів.")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
Payment_period = 18                                              
Monthly_payment = 1179                                           
total_cost_PC = Payment_period * Monthly_payment

print(total_cost_PC)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(8019%8)
print(9907%9)
print(2789%5)
print(7248%6)    
print(7128%5)    
print(19224%9)   

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_piz_qty = 4
big_piz_price = 274

middle_piz_qty = 2
middle_piz_price = 218

juice_qty = 4
juice_price = 35

cake_qty = 1
cake_price = 350

water_qty = 3
water_price = 21

total_cost = (
        big_piz_qty * big_piz_price +
        middle_piz_qty * middle_piz_price +
        juice_qty * juice_price +
        cake_qty * cake_price +
        water_qty * water_price
)

final_string = f"Для замовлення на день народження знадобиться {total_cost} грн."
print(final_string)

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
photos_per_page = 8

pages = photos // photos_per_page
remainder = photos % photos_per_page

if remainder > 0:
    pages = pages + 1

final_string = f"Щоб вклеїти всі фото Ігорю знадобиться {pages} сторінок."
print(final_string)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
dist = 1600
tank_capacity = 48
fuel_per_100 = 9

fuel_required = dist * fuel_per_100 // 100

refuels = fuel_required // tank_capacity
remainder = fuel_required % tank_capacity

if remainder > 0:
    refuels = refuels + 1

final_string = f"Для подорожі потрібно {fuel_required} літрів бензину."
print(final_string)
final_string = f"Мінімально потрібно заїхати на заправку {refuels} рази."
print(final_string)



