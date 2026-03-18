son = int(input("Son kiriting: "))

while son != 1 and son != 4:
    yigindi = 0
    
    while son > 0:
        raqam = son % 10
        yigindi += raqam ** 2
        son //= 10
    
    son = yigindi

if son == 1:
    print("Happy Number")
else:
    print("Unhappy Number")