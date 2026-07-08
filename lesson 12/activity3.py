# Input a number
num = int(input("Enter the number : "))
t = num
numLen = 0
# Iterate the loop to find the number of digits
while t > 0:
    numLen = numLen + 1
    t = int(t / 10)
# Apply conditions based on digit length
if numLen >= 4:  # condition 1
    numLen = int(numLen / 2)
    chk = 0

    while num>0: # condition 2
        r = num % 10
        chk = chk + r * (10 ** (numLen - 1))
        numLen = numLen - 1
        num = int(num/10)
        product = chk * chk
    print(product)
else:
    print("the number does not have 4 or more digits")
