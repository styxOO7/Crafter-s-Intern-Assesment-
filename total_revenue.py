import csv

# function for calculating revenue:
def calculate_total_revenue(csv_file):
    total_revenue = 0
    with open(csv_file, "r") as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            date = row[0]
            sales = float(row[1])
            if "2022-04-01" <= date <= "2023-03-31":
                total_revenue += sales
    return total_revenue

# driver function:
if __name__ == "__main__":
    csv_file = "sales_data_FY2023.csv"
    total_revenue = calculate_total_revenue(csv_file)
    print(f"Total revenue from Financial Year 2023: $ {total_revenue:.2f}")
