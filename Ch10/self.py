class Employee:
    language = "Python" 
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Ram = Employee()
Ram.language = "Java" 
Ram.getInfo()
Ram.greet()
