import csv
import os

inputFilePath = os.path.join('Resources', 'election_data.csv')
outputFilePath = os.path.join('analysis', 'results.txt')
voteCounts = {}
totalVotes = 0

with open(inputFilePath, 'r') as inputFile:
    inputReader = csv.DictReader(inputFile)

    # Count the votes
    for row in inputReader:
        try:
            voteCounts[row['Candidate']] += 1
        except KeyError:
            voteCounts[row['Candidate']] = 1

totalVotes = sum(voteCounts.values())

# Format output ************************************************************
output = f"""Election Results

-------------------------

Total Votes: {totalVotes}

-------------------------

"""

for candidate, votes in voteCounts.items():
    output += f'{candidate}:{votes / totalVotes: .3%} ({votes})\n\n'

output += f"""-------------------------

Winner: {max(voteCounts, key = voteCounts.get)}

-------------------------"""
# Format output end ********************************************************
    
# Write output to the terminal and a .txt file
print(output)
open(outputFilePath, 'w').write(output)
