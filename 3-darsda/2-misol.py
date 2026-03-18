from random import randint


royxat = []
for i in range(20):
    son = randint(1,100)
    royxat.append(son)
print(royxat)

royxat.sort()
print(royxat)
print(royxat[1], royxat[-2])
