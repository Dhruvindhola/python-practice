age = int(input("Enter your age: "))

# If statement no: 1
if(age%2 == 0):
    print("age is even")

# If statement no: 2
if(age>=18):
    print("You are above the age of consent")

elif(age<0):
    print("You are entering an invalid age")

elif(age==0):
    print("You are entering 0 which is not valid age")
    
else:
    print("You are below the age of consent")
