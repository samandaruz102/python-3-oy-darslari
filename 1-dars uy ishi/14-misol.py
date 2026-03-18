"""Foydalanuvchi biror matn kiritsin. Dastur .isalpha(), .isdigit(), 
.isalnum() yordamida satr turi haqida ma’lumot chiqarsin."""


matn = input("Ixtiyoriy matn kiriting: ")
natija1 = matn.isalpha()
natija2 = matn.isdigit()
natija3 = matn.isalnum()
print(f"Faqat harfmi?: {natija1}")
print(f"Faqat raqammi?: {natija2}")
print(f"Harf+Raqammi?: {natija3}")