class Employee:
    language = "Python" # This is a class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning")


Ram = Employee()
Ram.language = "Java" # This is an instance attribute
Ram.getInfo()
Ram.greet()
