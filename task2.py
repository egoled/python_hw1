# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# x = int (input('Введите x: '))
# y = int (input('Введите y: '))
# z = int (input('Введите z: '))

# statement_one = not(x or y or z)
# statement_two = not x and not y and not z 
# print(statement_one == statement_two)

for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            print(f'Для x={x}, y={y}, z={z} утверждение {(not (x or y or z)) == (not x and not y and not z)}')