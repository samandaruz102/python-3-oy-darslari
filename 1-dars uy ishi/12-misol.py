"""Foydalanuvchi parol kiritsin. Dastur len() yordamida uzunligini 
aniqlasin. Agar 8 belgidan uzun bo‘lsa — “Yaxshi parol”, 
bo‘lmasa — “Juda qisqa” deb yozsin."""


parol = input("Parol kiriting: ")
sanash = len(parol)
if sanash >= 8:
    print("Yaxshi parol")
elif sanash < 8:
    print("Juda qisqa")