import pandas as pd
customers = pd.DataFrame({
   "customer_id": [
       "C101", None, "C103", "C104", "C105",
       "C106", "C107", "C108", "C109", "C110"
   ],
   "customer_name": [
       "Amit", "", "Rahul", "Priya", "Karan",
       "Sneha", "Rohit", "Anjali", "Vikas", "Pooja"
   ],
   "city": [
       "Delhi", "Mumbai", "", None, "Noida",
       "Mumbai", "Bangalore", "Delhi", "Noida", "Pune"
   ],
   "segment": [
       "Premium", "Regular", "Premium", "Regular", "Premium",
       "Premium", "Regular", "Premium", "Regular", "Premium"
   ]
})
print(customers)
#Products Dataset
products = pd.DataFrame({
   "product_id": [
       "P101", "P102", "P103", "P104",
       "P105", "P106", "P107", "P108"
   ],
   "product_name": [
       "Laptop",
       "Mouse",
       "Keyboard",
       "Monitor",
       "Headphones",
       "Tablet",
       "Printer",
       "Smartphone"
   ],
   "category": [
       "Electronics",
       "Accessories",
       "Accessories",
       "Electronics",
       "Accessories",
       "Electronics",
       "Electronics",
       "Electronics"
   ],
   "price": [
       65000,
       1200,
       2500,
       18000,
       3500,
       30000,
       15000,
       45000
   ]
})
#Stores Dataset
stores = pd.DataFrame({
   "store_id": [
       "S101", "S102", "S103", "S104"
   ],
   "store_name": [
       "Delhi Central",
       "Mumbai Central",
       "Pune Mall",
       "Bangalore Hub"
   ],
   "city": [
       "Delhi",
       "Mumbai",
       "Pune",
       "Bangalore"
   ]
})
#Sales Dataset
#I am intentionally adding a few invalid references
# so we can demonstrate data-quality problems during merging.
sales = pd.DataFrame({
   "sale_id": [
       1001, 1002, 1003, 1004, 1005,
       1006, 1007, 1008, 1009, 1010,
       1011, 1012, 1013, 1014, 1015
   ],
   "customer_id": [
       "C101", "C102", "C103", "C104", "C105",
       "C106", "C107", "C108", "C109", "C110",
       "C101", "C103", "C106", "C999", "C105"
   ],
   "product_id": [
       "P101", "P102", "P103", "P104", "P105",
       "P106", "P107", "P108", "P101", "P104",
       "P102", "P106", "P105", "P101", "P999"
   ],
   "store_id": [
       "S101", "S102", "S101", "S103", "S101",
       "S102", "S104", "S101", "S101", "S103",
       "S101", "S101", "S102", "S101", "S999"
   ],
   "quantity": [
       1, 3, 2, 1, 4,
       1, 2, 1, 1, 2,
       5, 1, 3, 1, 2
   ],
   "sale_date": [
       "2026-08-01",
       "2026-08-02",
       "2026-08-03",
       "2026-08-04",
       "2026-08-05",
       "2026-08-06",
       "2026-08-07",
       "2026-08-08",
       "2026-08-09",
       "2026-08-10",
       "2026-08-11",
       "2026-08-12",
       "2026-08-13",
       "2026-08-14",
       "2026-08-15"
   ]
})

# print(customers)
# print(products)
# print(stores)
# print(sales)

# #Customers dataset
# print(customers.head())
# print(customers.shape)
# print(customers.columns)
# print(customers.info)

# #products dataset
# print(products.head())
# print(products.shape)
# print(products.columns)
# print(products.info)

# #stores dataset
# print(stores.head())
# print(stores.shape)
# print(stores.columns)
# print(stores.info)

# #sales dataset
# print(sales.head())
# print(sales.shape)
# print(sales.columns)
# print(sales.info)

# #check missing values
# print(customers.isnull().sum())

print(customers["customer_id"].duplicated().sum())
print(products["product_id"].duplicated().sum())
print(stores["store_id"].duplicated().sum())
print(sales["sale_id"].duplicated().sum())

#merging two tables or datasets

sales_customers = sales.merge(
    customers,
    on="customer_id",
    how="inner"
)

print("Sales with customer")
print(sales_customers)

print(sales_customers.head())
print(sales.shape)
print(sales_customers.shape)

invalid_customers = sales_customers[
    sales_customers["customer_name"].isna()
]
print("Invalid Customers")
print(invalid_customers)

total_quantity = final_df["quantity"].sum()
print("Total quantity sold", total_quantity)

valid_df = final_df[
    final_df["customer_name"].notna()
    & final
]