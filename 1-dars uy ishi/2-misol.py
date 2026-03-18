"""Foydalanuvchi 3 xonali son kiritadi.Dastur sonning har bir raqamini 
ajratib olib, ularning yig‘indisini topadi.
(if ishlatilmaydi!)"""

son = int(input("3 xonali son kiriting: "))
natija = son//100+son//10%10+son%10
print(f"3 xonali sonning raqamlari yig'indisi {natija} teng")