"""Foydalanuvchi ismini kiritsin. Dastur uni kichik harflarga o‘tkazib,
oldiga @ qo‘shib username hosil qilsin."""


ism = input("Ismingizni kiriting: ")

username = "@" + ism.lower()

print(username)