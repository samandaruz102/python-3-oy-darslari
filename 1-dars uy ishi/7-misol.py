"""Foydalanuvchi ismini kiritsin. Parol ismning birinchi 2 harfi va 
oxirgi 2 harfidan tashkil topib, 3 marta takrorlansin."""


ism = input("Isim kiriting: ")
natija = (ism[:2] + ism[-2:]) * 3
print(natija)