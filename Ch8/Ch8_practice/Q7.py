def remove(list, word):
    for item in list:
        list.remove(word)
        return list
    
list = ["Jeel", "Rohan", "Mann", "Ram"]
print(remove(list, "Rohan"))
