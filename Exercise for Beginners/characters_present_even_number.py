# accept input string from a user
word = input("Enter word and number:")
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x=list(word)
for i in x[0::3]:
    print(i)