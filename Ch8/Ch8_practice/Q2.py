def fahrenheit(f):
    return 5*(f-32)/9

f =int(input("Enter temperature in F: "))
c = fahrenheit(f)
print(f"{round(c, 2)}")

