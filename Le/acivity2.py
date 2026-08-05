def cube(num):
    return num ** 3

def t(number):
 if number % 3 ==0:
    return cube(number)
 else:
    return False
print(t(6)) 
print(t(5)) 