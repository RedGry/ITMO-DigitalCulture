# Вставляешь числа из заданий по порядку:
# Задании 1:
a = 339
b = 2712
c = 2712
d = 339
e = 2712000

# Задании 2:
f = 993

# Задании 3: g - это размер, h - это скорость
g = 19.6
h = 38

# Задании 4: i - это раз в секунду, j - это замер
i = 40688
j = 39

# Задании 5:
k = 337

# Задании 6: l - это секунд, m - это кол-во уровней
l = 0.06
m = 722

# Задании 7: n - это байт (размер пакета), o - это байт (заголовок) , p - это байт (размер файла)
n = 3142
o = 60
p = 186000




#Код (да, да, я знаю ...) :
def upwards(y):
    if int(y * 10 % 10) == 0:
        if (y * 100 % 10) < 5:
            return print(int(y))
        else:
            return print(int(y) + 0.1)
    else:
        y *= 100
        if y % 10 <= 5:
            y /= 100
            y = round(y + 0.1, 1)
            return print(y)
        else:
            return print(round(y / 100, 1))

def pow2(gg):
    count = 1
    while gg != 0:
        if gg == 1:
            break
        else:
            gg //= 2
            count += 1
    return count

print("Задание 1:")
print("1:", a * 1024 * 8)
print("2:", b / 1000)
print("3:", c / 1000)
print("4:", d * 1000)
print("5:", e / 1000 / 8)
print("\nЗадание 2:")
z = f * (10 ** 9)
print("1:", z)
print("2:", int(round(z / (2 ** 30), 2) * 10) / 10)
print("\nЗадание 3 (Если число например: 15.0, то в ответ пишешь 15):")
upwards(y = int((g * (2 ** 30)) / (h * 1000 * 125) / 60 * 100) / 100)
print("\nЗадание 4:")
print(round(j/i*1000, 3))
print("\nЗадание 5:")
print(pow2(k))
print("\nЗадание 6:")
print(round(pow2(m) / l, 2))
print("\nЗадание 7:")
print(int(p / (n - o)) + 1)




