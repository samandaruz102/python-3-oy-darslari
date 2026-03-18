son = int(input("Son kiriting: "))
jam = 0
while son > 0:
    jam += son % 10
    son //= 10
print("Sonning raqamlari yig'indisi: ", jam)