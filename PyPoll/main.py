'''
PyPoll Instructions

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

Your analysis should align with the following results:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''



# Import Dependencies
import os
import csv

# Creating a path to the csv and txt file 
csv_path = os.path.join("C:/Users/17202/Documents/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv")
output = ("C:/Users/17202/Documents/GitHub/Python-Challenge/PyPoll/Analysis/Election Results.txt")

# Creating variables
TotalVotes = 0
Candidates = []
candidatevotes = {}

# Open csv file
with open (csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    firstrow = next(csvreader)

    # Counting total votes
    TotalVotes += 1
    Candidates = firstrow[2]
    
    # Reading each row of data
    for row in csvreader:
        
        TotalVotes += 1
        Candidates = row[2]
        
        if row[2] not in candidatevotes:
            candidatevotes[row[2]] = 1
        
        else:
            candidatevotes[row[2]] += 1

# Printing the results in terminal
print("Election Results")

print("----------------------------------")

print("Total Votes: " + str(TotalVotes))

print("----------------------------------")

for candidate, votes in candidatevotes.items():
    print(candidate + ": " + "{:.3%}".format(votes/TotalVotes) + "  (" + str(votes) + ")")

print("----------------------------------")

winner = max(candidatevotes, key=candidatevotes.get)
    
print(f"Winner: {winner}")

print("----------------------------------")

# Write this to output file

with open(output, "w") as f:
    
    f.write("Election Results\n")
    f.write("\n")
    f.write("---------------------------\n")
    f.write("\n")
    f.write("Total Votes: " + str(TotalVotes)+ "\n")
    f.write("\n")
    f.write("---------------------------\n")
    f.write("\n")
    
    for candidate, votes in candidatevotes.items():
        f.write(candidate + ": " + "{:.3%}".format(votes/TotalVotes) + "  (" + str(votes) + ") +\n")
    f.write("\n")
    f.write("---------------------------\n")
    f.write("\n")
    
    winner = max(candidatevotes, key=candidatevotes.get)
    f.write(f"Winner: {winner}+ \n")
    f.write("\n")


