print("enter marks obtained by you in 5 subjects:")
a=int(input("enter marks for subject 1: "))
b=int(input("enter marks for subject 2: "))
c=int(input("enter marks for subject 3: "))
d=int(input("enter marks for subject 4: "))
e=int(input("enter marks for subject 5: "))
tatl= a+b+c+d+e
avg= tatl/5
validrange=(range(0,101))
if avg not in validrange:
    print("invalid input. please enter marks between 0 and 100.")
elif avg in range(90, 101):
    print("grade A")
elif avg in range(80, 90):
    print("grade B")
elif avg in range(70, 80):
    print("grade C")
elif avg in range(60, 70):
    print("grade D")
elif avg in range(50, 60):
    print("grade E")
else:
    print("grade F t1ry again next time work harder")