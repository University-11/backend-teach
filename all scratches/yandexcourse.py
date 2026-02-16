

# Задача на форматирование print
name = input()
price = int(input())
weight = int(input())
paper = int(input())
item = price * weight
itog = paper - item
print('=' * 16 + 'Чек' + '=' * 16)
print(f'Товар:{name:>29}')
s = str(weight) + 'кг' + ' * ' + str(price) + 'руб/кг'
print('Цена:' + ' ' * (35 - 5 - len(s)) + s)
print(f'Итого:{item:>26}руб')
print(f'Внесено:{paper:>24}руб')
print(f'Сдача:{itog:>26}руб')
print('=' * 35)