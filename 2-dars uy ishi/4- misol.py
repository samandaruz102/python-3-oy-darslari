"""Foydalanuvchi kiritgan sonni teskari tartibda chiqaring."""


son = int(input("Son kiriting: "))
teskari = 0
while son != 0:
    raqam = son % 10
    teskari = teskari * 10 + raqam
    son = son // 10
print("Teskari tartibda:", teskari)