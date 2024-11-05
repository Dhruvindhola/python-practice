import os

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    os.makedirs("tables", exist_ok=True)
    
    with open(f"tables/table_{n}", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)