import csv
import os

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader:
        votes = votes + 1
        total_candidates = row[2]        

        if row[2] not in candidate_options:
            
            candidate_options.append(row[2])

            candidate_votes[row[2]] = 1
            
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
    
    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items())

print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")





