# Мы всё ближе и ближе подбираемся к серьёзной математике. 
# Одна из классических задач — задача на нахождение факториала числа. И в будущем мы с ней ещё встретимся.
# Дано натуральное число n. Напишите программу, которая находит n! (n-факториал).
# Запись n! означает следующее:
# n! = 1 * 2 * 3 * 4 * 5 * … * n

number = int(input("Введите число для нахождения его факториала: "))
result = 1

for i in range(1, number + 1):
    result *= i
print("Факториал числа", number, "равно", result)
    


