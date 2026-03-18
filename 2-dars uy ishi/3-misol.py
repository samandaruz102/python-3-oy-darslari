A = int(input("A sonini kiriting: "))
B = int(input("B sonini kiriting: "))
jam = 0
for i in range(A, B + 1):
    if i % 2 == 0:
        jam += i
print(f"A dan B gacha juft sonlar yig'indisi: {jam}")