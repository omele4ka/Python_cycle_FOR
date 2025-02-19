print('Задача 3. Факториал')

# Мы всё ближе и ближе подбираемся к серьёзной математике.
# Одна из классических задач - задача на нахождение факториала числа.
# И в будущем мы с ней ещё встретимся.
# 
# Дано натуральное число N. Напишите программу, которая находит N! (N факториал)
# 
# Запись N! означает следующее:
# 
# N! = 1 * 2 * 3 * 4 * 5 * … * N
# 
# Пример:
# 
# Введите число: 5
# Факториал числа 5 равен 120

factorial_num = int(input('Введите число: '))
for num in range(1, factorial_num):
    factorial_num *= num
print(f'Факториал вашего числа равен {factorial_num}')