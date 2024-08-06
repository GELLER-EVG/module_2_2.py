first = input('Введите  целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третье целое число: ')

if first == second and second == third:
    matches = 3
elif first == second or second == third or first == third:
    matches = 2
else:
    matches = 0
print('Введено одинаковых чисел:', matches)


