"""Foydalanuvchi kitob nomini kiritsin. Dastur uni .title() yordamida 
bosh harflar bilan chiqarib, markazga 30 belgilik joyda joylashtirsin."""


ism = input("Ismingizni kiriting: ")
natija = ism.title()
natija_oxirgi = natija.center(30)
print(natija_oxirgi)