"""Soch olish narxi 25 000 so‘m, soqol olish 10 000 so‘m. 
Foydalanuvchi ikkala xizmatni oldimi yoki bittasinimi — shunga qarab 
umumiy summani hisoblang.
(*Bu yerda `input()` satrlarni `int()` ga o‘girish kerak bo‘ladi.*)"""


soch = int(input("Soch olasizmi?\n1.Ha\n0.Yo'q\n"))
soqol = int(input("\nSoqol olasizmi?\n1.Ha\n0.Yo'q\n"))

jami = 0

if soch == 1:
    jami += 25000

if soqol == 1:
    jami += 10000

print(f"Jami to‘lov: {jami} so‘m")