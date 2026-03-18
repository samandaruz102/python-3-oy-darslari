son = int(input("SOn kiriting: "))
a = 0
for i in range (1, son, 1):
    if son % i == 0:
        a = a + i 
if son == a:
    print("Mukammal son")
else:
    print("Mukammal son emas")