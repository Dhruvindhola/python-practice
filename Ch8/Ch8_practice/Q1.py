a = 10
b = 17
c = 15

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    if(c>b and c>a):
        return c
    
print(greatest(a, b, c))