"""Foydalanuvchi N sonini kiritsin. 1 dan N gacha bo‘lgan toq 
sonlar yig‘indisini toping."""


N = int(input("Son kiriting: "))
jam = 1
for i in range(1, N + 1):
    jam *= i
print(f"N gacha faktorial: {jam}")