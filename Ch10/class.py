class Employee:
    language = "Python" # This is a class attribute
    salary = 120000

Ram = Employee()
Ram.name = "Ram" # This is an instance attribute
print(Ram.name, Ram.language, Ram.salary)

Om = Employee()
Om.name = "Om"
print(Om.name, Om.salary, Om.language)
