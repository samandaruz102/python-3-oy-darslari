"""Foydalanuvchi 3ta harfli ism kiritsin. Har bir harfning ord() 
qiymatini chiqaring va ularning yig‘indisini toping."""


ism = input("3 ta harfli ism kiriting: ")
natija1 = ord(ism[0])
natija2 = ord(ism[1])
natija3 = ord(ism[2])
yigindi = natija1 + natija2 + natija3 
print(f"{ism[0]} -> {natija1}")
print(f"{ism[1]} -> {natija2}")
print(f"{ism[2]} -> {natija3}")
print(f"Jami: {yigindi}")