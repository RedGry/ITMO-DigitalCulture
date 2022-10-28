# 1 Упражнение
# Вставляешь из задания p, q, c, text (k - это количество знаков "... коды стали длиной k знаков" из 1 упражнения)
p = 149
q = 179
c = 15121
text = "Кунсткамера"
k = 5

# 2 Упражнение
# (kk - это количество знаков "... коды стали длиной k знаков" из 2 упражнения)
C = "0149121202143331626926006211943006612721"
kk = 5

# Числа из закрытого ключа
private_key = [30473, 34393]


# Решение
# Задание 1
a = []
b = ""
d = 0
op = ""
p1 = p - 1
q1 = q - 1
N = p * q

[a.append(ord(i) - 848) for i in text]

for gg in range(N + 1):
    if (c * gg % (p1 * q1)) == 1:
        d = gg
for i in a:
    num = str(int(i) ** int(c) % N)
    b += "0" * (k - len(num)) + num

# Задание 2
C = [C[i:i + kk] for i in range(0, len(C), kk)]

for i, j in zip(C, range(len(C))):
    count = 0
    for t in i:
        if t == "0":
            count += 1
            continue
        break
    C[j] = C[j][count:]

for i in C:
    temp_in = int(i) ** private_key[0] % private_key[1]
    temp_out = chr(temp_in + 848)
    op += temp_out

print("Упражнение 1")
print(f"d = {d}")
print(f"N = {N}")
print(f'Полученная последовательность ASCII символов: {"".join(str(i) for i in a)}')
print(f"Зашифрованное значение: {b}", "\n")

print("Упражнение 2")
print(f"Просто вставь это слово в ответ: {op}")
