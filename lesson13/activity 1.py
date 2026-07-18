# asking input
n=int(input ("enter a number:"))
print ("half pattern pyramid of stars ")
for i in range (1,n+1):
    for j in range (1,i+1):
        print ("*",end=" ")
    print ()