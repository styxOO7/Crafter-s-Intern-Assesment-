import csv
import random
import pandas as pd

# Define the financial year as a string
financial_year = "FY2023"

# Define the header row
header = ["Date", "Sales"]

# Generate 365 days of sales data for FY2023
sales_data = []
start_date = "2022-04-01"
end_date = "2023-03-31"
date_range = pd.date_range(start=start_date, end=end_date)
for date in date_range:
    sales = random.randint(100, 1000) # generate a random sales value between 100 and 1000
    row = [date.strftime("%Y-%m-%d"), sales] # convert the date object to a string in the format "YYYY-MM-DD"
    sales_data.append(row)

# Write the sales data to a CSV file
filename = f"sales_data_{financial_year}.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(sales_data)

print(f"Sample CSV file '{filename}' generated successfully!")
