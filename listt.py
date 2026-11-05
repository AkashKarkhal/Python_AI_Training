Employees = ["Akash", "Pranjali", "Shiv","Sahil","Prince","Atharva","Hitesh"]
print(Employees)
for employee in Employees:
    print(employee)
    
Employees.append("Sanjana")
print(Employees)

print(Employees[1])
print(Employees[::1])
Employees.reverse()
print(Employees)

Emp2 = Employees.copy()
print(Emp2)

print(len(Employees))

print(Employees[1:1])

print(Employees.count("Akash"))