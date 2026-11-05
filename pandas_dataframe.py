import pandas as pd
import numpy as np

employee_data = {
    "Employee_ID":["E101","E102","103","E104"],
    "Employee_Name":["Akash","Pranjali","Prince","hitesh"],
    "Department":["Data Engineer","Sales","Finance","IT"],
    "City":["Pune","Hyderabad","Chennai","Delhi"],
    "Salary":[50000,6000,90000,80000],
    "Experience":[5,9,8,3],
    "Rating":[10,9,5,4]
}

employee_df = pd.DataFrame(employee_data)
print(employee_df)
print(employee_df.head())
print(employee_df.head(3))
print(employee_df.tail())
print(employee_df.tail(3))
print(employee_df.shape)
print(employee_df.columns)
print(employee_df.dtypes)

print(employee_df[[
    "Employee_Name","Salary"
]])

result = employee_df[
    employee_df["Salary"] > 80000
]
print(result)

performance = employee_df[
    employee_df["Rating"]>4.5
]
print(performance)

salesdeparment = employee_df[
    employee_df["Department"] =="Sales"
]
print(salesdeparment)

Delhicity = employee_df[
    employee_df["City"] == "Delhi"
]
print(Delhicity)

rating_salary = employee_df[
    (employee_df["Rating"]>=4.5) & (employee_df["Salary"]>=70000)
]
print(rating_salary)

dept = employee_df[
    (employee_df["Department"]=="IT") | (employee_df["Department"] == "Finance")
]
print(dept)


isinmethod= employee_df[employee_df[ "Department"].isin(
    ["IT" , "Finance"]
)]
print(isinmethod)

employee_df["Annual Salary"] = employee_df["Salary"]*12
print(employee_df)



employee_df["Incremented Salary"] = employee_df["Annual Salary"] * 1.08
print(employee_df)

employee_df["Bonus"] = employee_df["Incremented Salary"] *0.05
print(employee_df)

employee_df["Compensation"] = employee_df["Incremented Salary"] + employee_df["Bonus"]
print(employee_df)

print(employee_df["Salary"].min())
print(employee_df["Salary"].mean())
print(employee_df["Salary"].sum())
print(employee_df["Salary"].max())
rating_mean = employee_df["Rating"].mean()
print("Average Rating: ", rating_mean)

dept_count = employee_df["Department"].count()
print("Number of Departmens: ", dept_count)

dept_len = len(employee_df["Department"])
print(dept_len)

unique_dept = employee_df["Department"].unique
print(unique_dept)

asseding_salary = employee_df["Salary"].sort_values
print(" Accessiding order salary",  asseding_salary)

sort_acc = employee_df.sort_values(by= "Salary").head(3)
print(sort_acc)

sort_desc = employee_df.sort_values(by= "Salary", ascending=False).head(3)
print(sort_desc)






