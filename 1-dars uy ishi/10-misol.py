"""Foydalanuvchi bitta harf kiritsin. Dastur ord() orqali uning ASCII 
kodini topib, 3 ga oshirib chr() yordamida “shifrlangan” 
harfni chiqarsin."""


harf = input("Bitta harf kiriting: ")
natija1 = ord(harf) + 3
natija2 = chr(natija1)
print(f"Kod: {ord(harf)} -> {natija1} -> {natija2} ")