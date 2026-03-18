son = 1020003
raqamlar = 0
daraja = 1
while son != 0:
    if son % 10: 
        raqamlar = raqamlar + (son % 10)  * daraja # 123
        daraja *= 10 # 100
    son //= 10 # 1
print(raqamlar)

# 123
