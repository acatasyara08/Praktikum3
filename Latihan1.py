from random import random

n = int(input("Masukkan nilai n: "))

for i in range(n):
    num = random()
    while num >= 0.5:
        num = random()
    print(f"{i + 1}. {num}")
