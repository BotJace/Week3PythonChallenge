import csv

# Define input and output file paths
input_file = "budget_data.csv"
output_file = "budget_analysis.txt"

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(input_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        # Count total number of months
        total_months += 1
        
        # Calculate total profit/loss
        total_profit_loss += int(row[1])
        
        # Track profit/loss changes
        if total_months > 1:
            profit_loss_change = int(row[1]) - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(row[0])
        previous_profit_loss = int(row[1])

# Calculate average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Generate analysis summary
analysis_summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print analysis to terminal
print(analysis_summary)

# Write analysis summary to text file
with open(output_file, "w") as txt_file:
    txt_file.write(analysis_summary)
