import csv
import os

inputFile = os.path.join(os.getcwd(), 'Resources', 'budget_data.csv')
outputFile = os.path.join(os.getcwd(), 'analysis', 'results.txt')

# Open the data file
input = csv.DictReader(open(inputFile, 'r'))
    
# Set up initial conditions using the first data entry
row = next(input)
profit = int(row['Profit/Losses'])
totalProfit = profit
changeInProfit = {}
previousProfit = profit

# Process the remaining data
for row in input:
    profit = int(row['Profit/Losses'])
    totalProfit += profit
    changeInProfit[row['Date']] = profit - previousProfit
    previousProfit = profit

# Sort the changes in profit by value
sortedChangeInProfit = sorted(changeInProfit.items(), key = lambda item: item[1])
totalMonths = len(sortedChangeInProfit) + 1

# Format output ***************************************************************************************
output = f"""Financial Analysis

----------------------------

Total Months: {totalMonths}

Total: ${totalProfit}

Average Change: ${round(sum(changeInProfit.values()) / (totalMonths - 1), 2)}

Greatest Increase in Profits: {sortedChangeInProfit[-1][0]} (${sortedChangeInProfit[-1][1]})

Greatest Decrease in Profits: {sortedChangeInProfit[0][0]} (${sortedChangeInProfit[0][1]})"""
# Format output end ***********************************************************************************

# Write output to the terminal and a .txt file
print(output)
open(outputFile, 'w').write(output)
