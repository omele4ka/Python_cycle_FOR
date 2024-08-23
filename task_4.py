print('Задача 4. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

from random import randint

excellent_marks = 0
good_marks = 0
satisfactory_marks = 0
student_list = int(input('Введите количество учеников в классе: '))
marks_list = []

for mark in range(1, student_list + 1):
  mark = randint(3, 5)
  marks_list.append(mark)
  if mark == 5:
    excellent_marks += 1
  elif mark == 4:
    good_marks += 1
  else:
    satisfactory_marks += 1

print(f'Список оценок: {marks_list}')
if (excellent_marks > good_marks) and (excellent_marks > satisfactory_marks):
  print(f'Сегодня больше отличников: {excellent_marks} человек.')
elif (good_marks > excellent_marks) and (good_marks > satisfactory_marks):
  print(f'Сегодня больше хорошистов: {good_marks} человек.')
elif (satisfactory_marks > excellent_marks) and (satisfactory_marks
                                                 > good_marks):
  print(f'Сегодня больше троечников: {satisfactory_marks} человек.')
else:
  print('Сегодня нет явных лидеров.')