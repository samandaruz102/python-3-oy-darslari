"""Foydalanuvchi ism-familiyasini kiritsin. Dastur ismning birinchi 
harfi va familiyaning oxirgi harfini chiqarib bersin."""


ism = input("Ism familiyangizni kiriting: ")
natija1 = ism[:1]
natija2 = ism[-1:]
print(f"Birinchi harf: {natija1}")
print(f"Oxirgi harf: {natija2}")