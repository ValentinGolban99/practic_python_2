# Напишите программу, которая считывает с клавиатуры два числа: 
# a и b, — считает и выводит в консоль среднее арифметическое 
# всех чисел из отрезка [a; b], кратных числу 3.

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

result = 0
count = 0
for i in range(first_number, second_number + 1):
    if i % 3 == 0:
        result += i
        count += 1
print("Результат вычеслений будет равен: ", (result / count))


