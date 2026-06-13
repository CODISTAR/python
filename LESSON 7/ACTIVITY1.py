# Variables creation
a = [1, 2, 3, 5, 6]
b = [1, 2, 3, 5, 6]
c = a

# Identity comparisons
print(a is b)        
print(c is a)        
print(b is not a)    
print(c is not a)    

print(id(a))         
print(id(b))         
print(id(c))         
