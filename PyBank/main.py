import csv
import os

inputFilePath = os.path.join('Resources', 'budget_data.csv')
outputFilePath = os.path.join('analysis', 'results.txt')

# Open the data file
with open(inputFilePath, 'r') as inputFile:
    inputReader = csv.DictReader(inputFile)
    
    # Set up initial conditions using the first data entry
    row = next(inputReader)
    profit = int(row['Profit/Losses'])
    totalProfit = profit
    changeInProfit = {}
    previousProfit = profit

    # Process the remaining data
    for row in inputReader:
        profit = int(row['Profit/Losses'])
        totalProfit += profit
        changeInProfit[row['Date']] = profit - previousProfit
        previousProfit = profit

totalMonths = len(changeInProfit) + 1

# Sort the changes in profit by value
sortedChangeInProfit = sorted(changeInProfit.items(), key = lambda item: item[1])

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
open(outputFilePath, 'w').write(output)
