# cheking whether a number is divisible by another number
numn=int(input("enter a number:(numerator):"))
numd=int(input("enter a number (denominator):"))
if numn%numd==0:
    print("\n" + str(numn) + " is divisible by " + str(numd))
else:
    print("\n" + str(numn) + " is not divisible by " + str(numd))