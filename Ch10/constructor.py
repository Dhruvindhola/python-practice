class Employee:
    language = "Python" # This is a class attribute
    salary = 120000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")


Ram = Employee("Ram", 130000, "C++")
print(Ram.name, Ram.salary, Ram.language)
