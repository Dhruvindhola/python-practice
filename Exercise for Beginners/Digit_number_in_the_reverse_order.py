# input the number
num = int(input("Enter a number with multiple digit: "))
n = 0

# Extracting and printing digits 
# in reverse order
while num > 0:
    a = num % 10
    num = num - a
    num = num/10
    print(int(a), end = " ")
    n = n + 1
