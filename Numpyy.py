import numpy as np

salary = np.array([65000,58000,72000,80000,85000,68000,90000,76000])
print(salary)

print("Numppy Operations")
print("dimension ",salary.ndim)
print(" type", type(salary))
print(" shape ", salary.shape)
print("size ", salary.size)
print("data type ", salary.dtype)

# salary = np.array([[65000,58000,72000,80000,85000,68000,90000,76000]])
# print(salary)
# print(salary.ndim)

rating = np.array([4,5,4,2,8,4,6,4])
print(rating)

print(".....Rating Properties.....")
print(rating.min())

print(rating.shape)
print(rating.size)
print(rating.dtype)



print("numpy indexing")

print("first salary", salary[0])
print("third party", salary[2])
print("last salary", salary[-1])
print("second last salary", salary[-2])
print("third last salary", salary[-3])

# salary = np.array([65000,58000,72000,80000,85000,68000,90000,76000])


print(salary[0:3])
print(salary[-3:])
print(salary[2:])

high_salary = salary[salary>75000]
print("Highest salary: ", high_salary)
print("employee count whose are highest salary than 750000", len(high_salary))


high_rating = rating[rating>4.5]
print("Highest salary: ", high_rating)
print("employee count whose are highest rating than 4.5--> ", len(high_rating))


#where clause using ternary operator in numpy......
new_salary = np.where(salary > 70000, salary * 1.10, salary * 1.05)
print("original salary ", salary)
print("updated salary ", new_salary)


increment = np.where(salary < 70000, salary * 1.10, salary * 1.05)
print(increment)

bonus = np.where(
    rating >=4.5,
    salary * 0.15,
    salary *0.05
)
print(bonus)

incremented_salary_after_bonus = salary + bonus
print(incremented_salary_after_bonus)

