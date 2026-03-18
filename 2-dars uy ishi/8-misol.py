son = int(input("Son kiriting: "))
jam = 0
while son > 0:
    jam += (son % 10)**2
    son //= 10
print(jam)