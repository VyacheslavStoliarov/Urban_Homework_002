first, second, third = map(int, input('Введите 3 целых числа через пробел: ').split())
print('Найдено совпадений: ', end = '')
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)