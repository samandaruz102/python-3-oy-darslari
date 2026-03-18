N = int(input("Son kiriting: "))
jami = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        jami += i
print(f"N gacha bolgan toq sonlar yig'indisi {jami} ")