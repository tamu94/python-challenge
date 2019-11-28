# provide file name to open with polling data
filename = "election_data.csv"

import csv
#read csv file and create lists from csv columns 
voter_ID = []
county = []
candidate = []

with open(filename, "r") as input_file:
    csvreader = csv.reader(input_file, delimiter =",")
    for row in csvreader:
        candidate.append(row[2])
        county.append(row[1])
        voter_ID.append(row[0])
countrows = voter_ID
nrows = len(countrows)
total_votes = nrows - 1

# total votes by cadidate and create Dict of results vote_total_dict
candidate.pop(0)
vote_total_dict = dict( [ (i, candidate.count(i)) for i in set(candidate) ] )

# determines the winner
winner = max(vote_total_dict, key=vote_total_dict.get)

##### print results #####
print("Election Results")
print("------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------------")

for key, value in sorted(vote_total_dict.items(), key=lambda x: x[1], reverse=True): 
    print(f"{key}: {round(value/total_votes*100,3)}% ({value})")

print("------------------------------------------------")
print(f"Winner: {winner}")
print("------------------------------------------------")


##### write to text file #####
with open("testfile.txt", "w") as f:
    f.write("Election Results\n")
    f.write("----------------------------------------------\n")
    f.write("Total Votes: " + str(total_votes))
    f.write("\n------------------------------------------------")
    f.write('\n')
    for key, value in sorted(vote_total_dict.items(), key=lambda x: x[1], reverse=True): 
        f.write(f"{key}: {round(value/total_votes*100,3)}% ({value})\n")

    f.write("------------------------------------------------")
    f.write("\nWinner: " + winner)
    f.write("\n------------------------------------------------")