"""Foydalanuvchi telefon raqamini “+998-90-123-45-67” ko‘rinishida 
kiritsin. Dastur replace() yordamida “+”, “-” belgilarini 
olib tashlasin."""


raqam = input("Telifon raqam kiriting: Misol(+998-88-585-77-21)")
natija1 = raqam.replace("+","")
natija2 = natija1.replace("-","")

print(natija2)