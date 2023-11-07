import csv
import os

inputFile = os.path.join('Resources', 'election_data.csv')
outputFile = os.path.join('analysis', 'results.txt')
voteCounts = {}
totalVotes = 0

# Open the data file
input = csv.DictReader(open(inputFile, 'r'))

# Sum the votes
for row in input:
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
open(outputFile, 'w').write(output)
