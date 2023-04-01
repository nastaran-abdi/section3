a = []

for i in range (5):
    b=int(input ("please enter your number"))
    a.append(b)

if sorted(a) == a:
    print("it is sorted")
else:
    print("it is not sorted")