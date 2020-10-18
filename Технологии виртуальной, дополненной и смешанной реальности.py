#Для задания 1:
coord_1  = "97 2 74"  # Координаты
radius_1 = 24         # Радиус

#Для задания 2:
coord_2  = "33 71 71" # Координаты
radius_2 = 36         # Радиус
height_2 = 15         # Высота
color_2  = "#3b05e3"  # Цвет

#Для задания 3:
width  = 116  # Ширина
height = 22   # Высота
depth  = 10   # Глубина
indent = 7    # Отступ (... ближайшего ребра параллелепипеда составлял ...)
ledge  = 3.8  # Выступ (...  грани параллелепипеда и выступало на ...)




#Ничего не трогай ниже!!!
print('Упражнение 1:')
print('<a-sphere position="'+ coord_1 + '" radius="' + str(radius_1) + '"></a-sphere>' + '\n')
print('Упражнение 2:')
print('<a-cylinder position="' + coord_2 + '" radius="' + str(radius_2) + '" height="' + str(height_2) + '" color="' + color_2 + '"></a-cylinder>' + '\n')
print('Упражнение 3:')
task3_1_1 = (width - 4 * indent) / 4
task3_1_2 = (height - 2 * indent) / 2
if (task3_1_1 > task3_1_2):
    task3_1 = task3_1_2
else:
    task3_1 = task3_1_1
task3_2 = depth + ledge
task3_3_1 = width / 4
task3_3_2 = ledge / 2
if (task3_1 % 1 == 0):
    task3_1 = int(task3_1)
if (task3_2 % 1 == 0):
    task3_2 = int(task3_2)
if (task3_3_1 % 1 == 0):
    task3_3_1 = int(task3_3_1)
if (task3_3_2 % 1 == 0):
    task3_3_2 = int(task3_3_2)
print(task3_1)
print(task3_2)
print('<a-cylinder position="' + str(task3_3_1) + ' 0 ' + str(task3_3_2) + '" radius="' + str(task3_1) + '" height="' + str(task3_2) + '" color="#FFC65D" rotation="90 0 0"></a-cylinder>')

