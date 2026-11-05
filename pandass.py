import pandas as pd
import numpy as np
#create pandas series....
salary_series = pd.Series([
    6500, 7000, 8000, 4000, 30000
])
print(salary_series)
#check properties....
print(salary_series.index)
print(salary_series.values)
print(salary_series.dtype)

#series with custom index....
employee_series = pd.Series(
    [
        "Shiv", "Atharva", "Shreyansh", "Sahil","Prince","Hitesh","Akashdeep","Pranjali"
    ],
    index=[
        "E101","E102","E103","E104","E105","E106","E107","E108"
    ]
)

print(employee_series)
print(employee_series["E101"])
print(employee_series["E107"])
