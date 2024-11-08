class programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Prince", 120000, 30987)
print(p.name, p.salary, p.pin, p.company)
o = programmer("Om", 150000, 232434)
print(o.name, o.salary, o.pin, o.company)
