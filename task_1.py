# В базе банка хранятся данные и должников, и законопослушных граждан. 
# Каждому человеку система присваивает свой номер. У нас есть случайная выборка из десяти номеров. 
# Правда, иногда база глючит и выдаёт номер с отрицательным значением. А ещё по статистике, 
# которую собрал наш «МирПрогБанк», каждый второй пользователь брал кредит и не выплатил его вовремя, то есть является должником.
# Напишите программу, которая при вводе десяти чисел определяет, сколько из них являются одновременно чётными и положительными.

print("Введите 10 пользователей! ")

even_positive = 0

for i in range(1, 11):
    print("Введите номер пользователя", i)
    user_number = int(input())
    if user_number % 2 == 0 and user_number > 0:
        even_positive += 1
print("Из 10 введенных пользователей четных и положительных: ", even_positive)
    

