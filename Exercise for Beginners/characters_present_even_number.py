word = input("Enter word and number:")
print("Original String:", word)

x=list(word)
for i in x[0::3]:
    print(i)