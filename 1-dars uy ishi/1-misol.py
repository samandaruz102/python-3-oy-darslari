"""Internet tezligi `Mb/s` (megabit/sekund) bilan beriladi.
Foydalanuvchi fayl hajmini `MB` (megabayt) bilan kiritadi."""


fayl_hajmi = float(input("Fayl hajmi (MB): "))
tezlik = float(input("Tezlik (Mb/s): "))

vaqt = (fayl_hajmi * 8) / tezlik

print(f"Fayl {vaqt} soniyada yuklanadi")