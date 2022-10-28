# Для задания 1:
coord_1 = "96 95 6"     # Координаты
radius_1 = 17           # Радиус

# Для задания 2:
coord_2 = "33 71 71"    # Координаты
radius_2 = 36           # Радиус
height_2 = 15           # Высота
color_2 = "#3b05e3"     # Цвет

# Для задания 3:
width = 56              # Ширина
height = 46             # Высота
depth = 11              # Глубина
indent = 5              # Отступ (... ближайшего ребра параллелепипеда составлял ...)
ledge = 1.6             # Выступ (...  грани параллелепипеда и выступало на ...)

# Решение
print('Упражнение 1:')
print(f'<a-sphere position="{coord_1}" radius="{radius_1}"></a-sphere>', '\n')

print('Упражнение 2:')
print(f'<a-cylinder position="{coord_2}" radius="{radius_2}" height="{height_2}" color="{color_2}"></a-cylinder>', '\n')

print('Упражнение 3:')
task3_1_1 = (width - 4 * indent) / 4
task3_1_2 = (height - 2 * indent) / 2
task3_1 = task3_1_1 if task3_1_2 > task3_1_1 else task3_1_2
task3_2 = depth + ledge
task3_3_1 = width / 4
task3_3_2 = ledge / 2

task3_1 = int(task3_1) if task3_1.is_integer() else task3_1
task3_2 = int(task3_2) if task3_2.is_integer() else task3_2
task3_3_1 = int(task3_3_1) if task3_3_1.is_integer() else task3_3_1
task3_3_2 = int(task3_3_2) if task3_3_2.is_integer() else task3_3_2

print(task3_1)
print(task3_2)
print(f'<a-cylinder position="{task3_3_1} 0 {task3_3_2}" radius="{task3_1}" height="{task3_2}" color="#FFC65D" rotation="90 0 0"></a-cylinder>')
