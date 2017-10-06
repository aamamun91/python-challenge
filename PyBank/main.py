

import csv

# Files to load and output (Remember to change these)
filepath = "budget_data_1.csv"
outputFile = "budget_analysis_1.txt"


# Initialize the variables to be computed 
total_month = 0
last_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
total_revenue = 0

# Read the csv and convert it into a list of dictionaries
with open(filepath) as revenue_data:
    revenue1 = csv.DictReader(revenue_data)

    for row in revenue1:
        # Compute total number of months
        total_month = total_month + 1
        total_revenue = total_revenue + int(row["Revenue"])

        # Compute revenue change
        revenue_change = int(row["Revenue"]) - last_revenue
        last_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # Compute the greatest increase
        if (revenue_change > 0):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = max(revenue_change_list)

        # Compute the greatest decrease
        if (revenue_change < 0):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = min(revenue_change_list)

#print(revenue_change_list)
#print(revenue_change)

# Compute average revenue change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output
print(output)

# Results to text file
with open(outputFile, "w") as txtFile:
    txtFile.write(output)