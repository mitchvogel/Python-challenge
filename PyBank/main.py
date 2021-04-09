import os
import csv


# Path to collect data from Resources folder
csv_path = os.path.join('Resources', 'budget_data.csv')

# lists to keep track of the month result and date of the period
month_result = []
date = []

# variables
total = 0
total_change = 0
month_start = 0
month = 0

# Read the CSV file
with open(csv_path, 'r') as csv_file:
    
    # Split data at commas
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skip header
    csv_header = next(csv_reader)

    
    # loop thru rows 
    for row in csv_reader:

        # month counter
        month = month + 1
        
        # tracking of date/month
        date.append(row[0])

        # profits running total
        total = total +int(row[1])

        # calculate average change in profits each period
        month_end = int(row[1])

        if month_start == 0:
            monthly_profit_change = 0
        else:
            monthly_profit_change = month_end - month_start

        # store monthly profit change in list
        month_result.append(monthly_profit_change)

        # total change in profit accounting for losses or profit
        total_change = total_change + monthly_profit_change

        # reset month start for next months calulation
        month_start = month_end

        # refencing monthly profit change list to determine biggest inc and biggest dec
        greatest_profit = max(month_result)
        greatest_loss = min(month_result)

        # utilizing bigges inc/biggest dec to grab the date of that period
        increase_period = date[month_result.index(greatest_profit)]
        decrease_period = date[month_result.index(greatest_loss)]

# (month - 1) accounting for initial January value
average_change = float(total_change/(month - 1))
average_decimal = round(average_change, 2)

print("Financial Analysis")
print("-----------------------------------------------------------")
print("Total Months: " + str(month))
print("Total Profits: " + "$" + str(total))
print("Average Change: " + "$" + str(average_decimal))
print("Greatest Increase in Profits: " + str(increase_period) + " $ " + str(greatest_profit))
print("Greatest Decrease in Profits: " + str(decrease_period) + " $ " + str(greatest_loss))


textfile = open('fin_analysis.txt', 'w')
textfile.write("Financial Analysis\n")
textfile.write("----------------------------------------------------------\n\n")
textfile.write("Total Months: " + str(month) + "\n")
textfile.write("Total Profits: " + "$" + str(total) + "\n")
textfile.write("Average Change: " + "$" + str(int(average_decimal)) + "\n")
textfile.write("Greatest Increase in Profits: " + str(increase_period) + " $ " + str(greatest_profit) + "\n")
textfile.write("Greatest Decrease in Profits: " + str(decrease_period) + " $ " + str(greatest_loss) + "\n")
textfile.close()