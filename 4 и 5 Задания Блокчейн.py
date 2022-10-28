# Задание 4
a = 281
c = 624
d = 970

# Задание 5
one = "0077a3bacbb13bf0ffaf9d5fb1fc8f02cc4d166916b506793c8274cedd930efd"    # вставляем hash, который уже дан по заданию
two = 681                                                                   # пишем число, которое дано по заданию


# Решение
import hashlib
task1 = str(hashlib.sha256(str(a).encode()).hexdigest())
h = task1 + str(hashlib.sha256(str(c).encode()).hexdigest())
task2 = str(hashlib.sha256(str(h).encode()).hexdigest())
j = task2 + str(hashlib.sha256(str(d).encode()).hexdigest())
task3 = str(hashlib.sha256(str(j).encode()).hexdigest())

print("Задание 4:")
print(f"1: {task1}")
print(f"2: {task2}")
print(f"3: {task3}", "\n")


two_hash = hashlib.sha256(str(two).encode()).hexdigest()
string = one + two_hash
answer = ""
x = 1
b = 1

while x < 10000:
    s = hashlib.sha256(str(b).encode()).hexdigest()
    gg = string
    gg += s
    gg = hashlib.sha256(str(gg).encode()).hexdigest()
    if gg[:2] == "00":
        answer = gg
        break
    x += 1
    b += 1

print("Задание 5:")
print(f"Пишешь в ответ: {answer}")
