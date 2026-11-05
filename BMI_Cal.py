weight =  float(input("Enter your weight"))
height = float(input("Enter your Height"))
BMI = weight / (height * height)
print(BMI)
if(BMI <=18.5):
    print("underweight")
elif(BMI >=18.5 and BMI <=24.9):
    print("Normal") 
elif(BMI >=25 and BMI <=29.9 ):
    print("Overweight")     
else:
    print("obese")