monthly_salary = float(input("Enter yuour monthly salary: "))
credit_score = float(input("Enter your credit score: "))
existing_loan_amount = float(input("Enter Existing Loan Amount: "))
employement_type = input("Enter your employment type: ")

if(monthly_salary>80000 and credit_score>750 and existing_loan_amount<2000):
    print("Your Loan Approved Successfully: ")
    
elif(monthly_salary>50000 and credit_score>650):
    print("Approved With Caution...")
    
elif(credit_score<600):
    print("Your Loan is Reject due to low credit score: ")
 
else:
    print("Your Application is under manual review kindly wait we will inform you thanks...")        