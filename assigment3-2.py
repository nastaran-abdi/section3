import random
a=[]
n=int(input(("please enter measurment for n")))
for i in range (n):
    x=random.randint(0,100)
    if x in a:
        pass
    else:
        a.append(x)
print(a)
