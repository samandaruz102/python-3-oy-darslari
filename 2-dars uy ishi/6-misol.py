"""Foydalanuvchi N sonini kiritsin. 1 dan N gacha bo‘lgan tub sonlarni chiqarilsin."""


N = int(input("Son kiriting: "))
for i in range(1, N + 1):
    tub = True
    for j in range(2, i):
        if i % j == 0:
            tub = False
            break
    if tub:
        print(i)