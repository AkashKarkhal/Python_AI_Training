age = int(input("enter age: "))
smoker = input("smoker (yes/no): ").lower()
bmi - float(input("enter bmi: "))
disease = input("serve pre-existing disease (yes/no): ").lower()

if disease == "yes" and age >60:
    print("Insurance Rejected")
elif smoker == "yes" and age > 50:
    print("High Premium")
elif bmi >=25:
    print("Medium Premium") 
elif age <30 and smoker == "no" and bmi <25 and disease == "no":
    print("Low Premium")
    
else:
    print("standard Premium")               