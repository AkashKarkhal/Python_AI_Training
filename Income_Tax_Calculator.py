annual_income = float(input("Enter your Annual Income: "))
age = float(input("Enter your age: "))
investment_amount = float(input("Enter your investment amount: "))

if(age>=60):
    print("Allow...")
    
if(annual_income<=500000):
    print("Income Tax 0")    
elif(annual_income>=500000 and annual_income<=1000000):
    print("Income Tax 10%")  
elif(annual_income >=1000000 and annual_income<=2000000):
    print("Income Tax 20%")
else:
    print("Tax 30%")          