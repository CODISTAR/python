a = int(input("enter a number1: "))
b = int(input("enter a number2: "))
c = int(input("enter a number3: "))
# calculating average
avg = (a + b + c) / 3
# showing average is greater than which variable
if avg > a and avg > b and avg > c:
    print(avg, "is greater than", a, b, c)
elif avg > a and avg > b:
    print(avg, "is greater than", a, b)
elif avg > a and avg > c:
    print(avg, "is greater than", a, c)
elif avg > b and avg > c:
    print(avg, "is greater than", b, c)
elif avg > a:
    print(avg, "is greater than", a)
elif avg > b:
    print(avg, "is greater than", b)
elif avg > c:
    print(avg, "is greater than", c)
else:
    print ("invalid input")
    34
