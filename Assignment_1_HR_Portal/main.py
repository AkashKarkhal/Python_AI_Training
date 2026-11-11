import numpy
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("DataSets/Cadbury_Dairy_Milk_Sales_2025_Synthetic.csv")

print(df.head(10))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.isnull().sum())
print(df.describe())
print(df["City"].unique())
print(df["Region"].unique())


# section B clean and filtering that data
clean_df = df.copy()


clean_df = clean_df.drop_duplicates()

print("Remaining rows:", len(clean_df))


clean_df.columns = (
    clean_df.columns
    .str.strip()
    .str.replace(" ", "_")
)

print("Columns after cleaning:", clean_df.columns)


invalid_quantity = clean_df[clean_df["Quantity"] <= 0]

print("Invalid Quantity records:")
print(invalid_quantity)


invalid_discount = clean_df[
    (clean_df["Discount_Pct"] < 0) |
    (clean_df["Discount_Pct"] > 100)
]

print("Invalid Discount records:")
print(invalid_discount)


invalid_financial = clean_df[
    (clean_df["Net_Revenue_INR"] < 0) |
    (clean_df["Total_Cost_INR"] < 0) |
    (clean_df["Profit_INR"] < 0)
]

print("Invalid Financial records:")
print(invalid_financial)


clean_df["Recalculated_Revenue"] = (
    clean_df["Quantity"] *
    clean_df["Unit_Selling_Price_INR"]
)

print("Recalculated Revenue:")
print(clean_df[["Order_ID", "Recalculated_Revenue"]].head())


invalid_revenue = clean_df[
    (clean_df["Net_Revenue_INR"] -
     clean_df["Recalculated_Revenue"]).abs() > 0.01
]

print("Revenue mismatch records:")
print(invalid_revenue)

print("Total Revenue mismatches:", len(invalid_revenue))


clean_df["Recalculated_Profit"] = (
    clean_df["Recalculated_Revenue"]
    - clean_df["Total_Cost_INR"]
    - clean_df["Delivery_Cost_INR"]
)

print("Recalculated Profit:")
print(clean_df[["Order_ID", "Recalculated_Profit"]].head())


clean_df["Profit_Margin_Pct"] = np.where(
    clean_df["Recalculated_Revenue"] != 0,
    (clean_df["Recalculated_Profit"] /
     clean_df["Recalculated_Revenue"]) * 100,
    0
)

print("Profit Margin:")
print(clean_df[[
    "Order_ID",
    "Recalculated_Revenue",
    "Recalculated_Profit",
    "Profit_Margin_Pct"
]].head())

clean_df["Order_Date"] = pd.to_datetime(
    clean_df["Order_Date"]
)
clean_df["Year"] = clean_df["Order_Date"].dt.year
clean_df["Month"] = clean_df["Order_Date"].dt.month
clean_df["Month_Name"]= clean_df["Order_Date"].dt.month_name()

print(clean_df[["Order_Date", "Year", "Month", "Month_Name"]].head())

clean_df["Quarter"] = clean_df["Order_Date"].dt.quarter
clean_df["Weekday"]= clean_df["Order_Date"].dt.day_name()

print(clean_df[["Order_Date", "Quarter", "Weekday"]])

clean_df["Weekend_Flag"] = np.where(
    clean_df["Order_Date"].dt.dayofweek >= 5,
    "Weekend",
    "Weekday"
)
print(clean_df[["Order_Date", "Weekend_Flag"]])

clean_df["Discount_Band"] = pd.cut(
    clean_df["Discount_Pct"],
    bins=[-0.01,0,5,15,100],
    labels = ["None", "Low", "Medium", "High"]
)
print(clean_df[["Discount_Pct", "Discount_Band"]])

clean_df["Order_Value_Band"] = pd.qcut(
    clean_df["Net_Revenue_INR"],
    q=3,
    labels=["Low", "Medium", "High"],
    duplicates="drop"
)
print(clean_df[["Net_Revenue_INR", "Order_Value_Band"]])

result = clean_df[
    [
        "Order_ID",
        "Product_Name",
        "City",
        "Quantity",
        "Net_Revenue_INR"
    ]
]
print(result)

mumbai_order = clean_df[
    clean_df["City"] == "Mumbai"
]
print(mumbai_order)

silk_orders = clean_df[
    clean_df["Product_Name"] == "Dairy Milk Silk"
]
print("Silk Orders:")
print(silk_orders)

discount_order = clean_df[
    clean_df["Discount_Pct"] > 15
]
print("Discount Orders:")
print(discount_order)
quantity_orders = clean_df[
    clean_df["Quantity"] >= 10
]

print(quantity_orders)

loss_making_order = clean_df[
    clean_df["Recalculated_Profit"] < 0
]
print("Loss Making Orders:")
print(loss_making_order)

northq4 = clean_df[
 (clean_df["Region"] == "North") & 
 (clean_df["Quarter"] == 4)

]
print("North q4 order")
print(northq4)

ecommerce_upi = clean_df[
    (clean_df["Sales_Channel"] == "E-commerce") & 
    (clean_df["Payment_Method"] == "UPI")
]
print("eccomerce upi")
print(ecommerce_upi)

start_date = "2025-01-01"
end_date = "2025-06-30"
date_orderss = clean_df[
    (clean_df["Order_Date"] >= start_date) & 
    (clean_df["Order_Date"] <= end_date)
]
print("dateordersss...")
print(date_orderss)

diary_milk = clean_df[
    clean_df["Product_Name"].str.contains(
        "Dairy Milk",
        case = False,
        na = False
    )
]
print(diary_milk)


# section D Aggregatates

total_revenue = clean_df["Net_Revenue_INR"].sum()
print(" Total Revenue", total_revenue)

total_profit = clean_df["Recalculated_Profit"].sum()
print("total profit", total_profit)

total_quantity = clean_df["Quantity"].sum()
print("Total quantity sold", total_quantity)

avg_order_value = clean_df["Net_Revenue_INR"].mean()
print("Average Order Value", avg_order_value)

channele_order = clean_df.groupby(
    "Sales_Channel"
)["Order_ID"].count()
print(ChildProcessError)


product_revenue = clean_df.groupby("Product_Name")["Net_Revenue_INR"].sum()

print(product_revenue)

profit_region = clean_df.groupby("Region")["Recalculated_Profit"].sum()
print(profit_region)

city_sales = clean_df.groupby("City")["Quantity"].sum()
print(city_sales)

bottom_cities = clean_df.groupby(
   "City" 
)["Recalculated_Profit"].sum().sort_values(
    ascending=True
).head(5)

print(bottom_cities)

mean_med = clean_df.groupby(
    "Sales_Channel"
)["Discount_Pct"].agg(
    ["mean", "median"]
)
print(mean_med)


# section E advanced analytics and joins

monthly_revenue = clean_df.groupby(
    "Month"
)["Net_Revenue_INR"]
print(monthly_revenue)

quarterly_profit = clean_df.groupby(
    "Quarter"
)["Recalculated_Profit"].sum()
print(quarterly_profit)

pivot_table = pd.pivot_table(
    clean_df,
    values="Net_Revenue_INR",
    index="Region",
    columns="Product_Name",
    aggfunc="sum",
    fill_value=0
)
print(pivot_table)

product_revenue = clean_df.groupby(
    "Product_Name"
)["Net_Revenue_INR"].sum()
product_share = (
    product_revenue/product_revenue.sum()
)*100
print("Total Revenue ",total_revenue)
print(" Revenue share by each product in Totaln Revenue", product_share)


products = pd.read_csv("dataSets/Cadbury_Product_Master.csv")
sales_product = pd.merge(
    clean_df,
    products,
    on="Product_ID",
    how="inner"
)
print(sales_product.head(10))

stores = pd.read_csv("DataSets/Cadbury_Store_Master.csv")
sales_store=  pd.merge(
    sales_product,
    stores,
    on="Store_ID",
    how="left"
)
print(sales_store.head(10))



# numpy perform on this datasets

quantity_array = np.array(clean_df["Quantity"])
print(quantity_array)

net_revenu = np.array(clean_df["Net_Revenue_INR"])
print(net_revenu)

print("Dimensions ", quantity_array.ndim)
print("Shape ", quantity_array.shape )
print("size ", quantity_array.size)
print("Data Type ", quantity_array.dtype)

discount_array = np.array(clean_df["Discount_Pct"])
unique_discounts = np.unique(discount_array)
print(unique_discounts)

days = np.arange(1,31)
print(days)

discount_rates = np.linspace(0,30,10)
print(discount_rates)

first_120 = quantity_array[:120]
matrix = first_120.reshape(12,10)
print(matrix)

print(np.sum(net_revenu))

percentile = np.percentile(
    net_revenu,
    [25,50,75,90]
)
print(percentile)

revenue = np.array(clean_df["Net_Revenue_INR"])
conditions = [
    revenue<300,
    (revenue >= 300) & (revenue < 1000),
    revenue >=1000
]
choices = ["low", "medium", "high"]
categories = np.select(
    conditions,
    choices,
    default="Unknown"
)
print(categories)

profit_margin = np.array(
    clean_df["Profit_Margin_Pct"]
) 
rounded_margin = np.round(
    profit_margin,
    2
)
print(rounded_margin)

sorted_revenue  = np.sort(net_revenu)
top_10 = sorted_revenue[-10:][::-1]
print(top_10)

current_revenue = np.sum(net_revenu)
projected_revenue = current_revenue * 1.05
print("current Revenue ", current_revenue)
print("Projected Revenue ", projected_revenue)

np.random.seed(42)

growth_rates = np.random.normal(
    loc=0.05,
    scale=0.02,
    size=1000
)

simulated_revenue = current_revenue * (
    1 + growth_rates
)

print("5th Percentile:",
      np.percentile(simulated_revenue, 5))

print("50th Percentile:",
      np.percentile(simulated_revenue, 50))

print("95th Percentile:",
      np.percentile(simulated_revenue, 95))

# DATA VISUALIZATION
os.makedirs("charts", exist_ok = True)
sns.set_theme(style="whitegrid")



os.makedirs("charts", exist_ok=True)
sns.set_theme(style="whitegrid", palette="deep")

monthly_revenue = clean_df.groupby(
    "Month"
)["Net_Revenue_INR"].sum()

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o",
    linewidth=2,
    markersize=7
)
plt.title("Monthly Net Revenue - 2025", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("charts/V01_monthly_revenue.png", dpi=300)
plt.show()
plt.close()

monthly_profit = clean_df.groupby(
    "Month"
)["Recalculated_Profit"].sum()

plt.figure(figsize=(10, 5))
plt.plot(
    monthly_profit.index,
    monthly_profit.values,
    marker="o",
    linewidth=2,
    markersize=7
)
plt.title("Monthly Profit - 2025", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Profit (INR)")
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("charts/V02_monthly_profit.png", dpi=300)
plt.show()
plt.close()

product_revenue = clean_df.groupby(
    "Product_Name"
)["Net_Revenue_INR"].sum().sort_values(ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(
    product_revenue.index,
    product_revenue.values
)
plt.title("Revenue by Product", fontsize=14)
plt.xlabel("Revenue (INR)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("charts/V03_product_revenue.png", dpi=300)
plt.show()
plt.close()

region_revenue = clean_df.groupby(
    "Region"
)["Net_Revenue_INR"].sum()

plt.figure(figsize=(8, 5))
plt.bar(
    region_revenue.index,
    region_revenue.values
)
plt.title("Revenue by Region", fontsize=14)
plt.xlabel("Region")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("charts/V04_region_revenue.png", dpi=300)
plt.show()
plt.close()

city_revenue = clean_df.groupby(
    "City"
)["Net_Revenue_INR"].sum().sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(10, 5))
plt.bar(
    city_revenue.index,
    city_revenue.values
)
plt.title("Top 10 Cities by Revenue", fontsize=14)
plt.xlabel("City")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/V05_top10_cities.png", dpi=300)
plt.show()
plt.close()

daily_revenue = clean_df.groupby(
    "Order_Date"
)["Net_Revenue_INR"].sum().sort_index()

moving_average = daily_revenue.rolling(
    window=7,
    min_periods=1
).mean()

plt.figure(figsize=(12, 5))
plt.plot(
    daily_revenue.index,
    daily_revenue.values,
    label="Daily Revenue",
    alpha=0.5
)
plt.plot(
    moving_average.index,
    moving_average.values,
    label="7-Day Moving Average",
    linewidth=2
)
plt.title("Daily Revenue Trend", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Revenue (INR)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("charts/V06_daily_revenue.png", dpi=300)
plt.show()
plt.close()

plt.figure(figsize=(9, 5))
sns.boxplot(
    data=clean_df,
    x="Sales_Channel",
    y="Net_Revenue_INR"
)
plt.title("Revenue Distribution by Sales Channel", fontsize=14)
plt.xlabel("Sales Channel")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("charts/V07_channel_revenue.png", dpi=300)
plt.show()
plt.close()

plt.figure(figsize=(9, 5))
sns.histplot(
    data=clean_df,
    x="Discount_Pct",
    bins=20,
    kde=True
)
plt.title("Discount Percentage Distribution", fontsize=14)
plt.xlabel("Discount Percentage")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("charts/V08_discount_distribution.png", dpi=300)
plt.show()
plt.close()

plt.figure(figsize=(8, 5))

plt.hist(
    clean_df["Quantity"],
    bins=15,
    edgecolor="black"
)

plt.title("Order Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Number of Orders")

plt.savefig("charts/V10_quantity_distribution.png")

plt.show()


plt.figure(figsize=(8,5))

plt.scatter(
    clean_df["Net_Revenue_)INR"],
    clean_df["Recalculated_Profit"]
)

plt.title("Revenue vs Profit")
plt.xlabel("Revenue INR")
plt.ylabel("Profit INR")
plt.savefig("charts/V11_revenue_profit_scatter.png")

plt.show()

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=clean_df,
    x="Product_Name",
    y="Profit_Margin_Pct"
)

plt.title("Profit Margin by Product")
plt.xlabel("Product")
plt.ylabel("Profit Margin (%)")

plt.xticks(rotation=45)

plt.savefig("charts/V13_profit_margin_boxplot.png")

plt.show()

quarterly_region = pd.pivot_table(
    clean_df,
    values="Net_Revenue_INR",
    index="Quarter",
    columns="Region",
    aggfunc="sum",
    fill_value=0
)

quarterly_region.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Quarterly Revenue by Region")
plt.xlabel("Quarter")
plt.ylabel("Revenue (INR)")

plt.legend(title="Region")

plt.savefig("charts/V14_quarterly_region.png")

plt.show()