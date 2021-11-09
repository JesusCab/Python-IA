import random 
def Rnum(list):
    return[random.choice(list)for _ in range(100)]

x=list(range(11))
listnum= Rnum(x)
Cnum={}
for cant in listnum:
    if cant in Cnum:

    