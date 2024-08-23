# В базе банка хранятся данные и должников, и законопослушных граждан. Каждому человеку система присваивает свой номер. У нас есть случайная выборка из десяти номеров. Правда, иногда база глючит и выдаёт номер с отрицательным значением. А ещё по статистике, которую собрал наш «МирПрогБанк», каждый второй пользователь брал кредит и не выплатил его вовремя, то есть является должником.

# Напишите программу, которая при вводе десяти чисел определяет, сколько из них являются одновременно чётными и положительными.

num_list = []

for i in range(10):
    number = int(input(f'Введите {i + 1} число: '))
    num_list.append(number)

even_num_counter = 0

for num in num_list:
    if (num > 0) and (num % 2 == 0):
        even_num_counter += 1
print(f'В списке {even_num_counter} положительных четных чисел/числа.')