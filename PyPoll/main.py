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
import pandas as pd

# Creating a path to the csv file 
csv_path = ("C:/Users/17202/Documents/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv")

# Using pandas to create a dataframe and read the csv
election_df = pd.read_csv(csv_path)

# This is the path for my txt file that will be used at the end
output = ("C:/Users/17202/Documents/GitHub/Python-Challenge/PyPoll/Analysis/Election Results.txt")


# Viewing the head of the dataframe
election_df.head()

# Counting the length of the ballot ID's to get a number of votes placed
totalvotes = len(election_df["Ballot ID"].value_counts())

# Looking up all the unique names of the candidates
candidates = election_df["Candidate"].unique()

# First gathering how many times the candidates  were mentioned in the data from
# the Candidate column. Then counting the length of the  data to get the amount
# of votes for each candidate
DDraw = election_df.loc[(election_df["Candidate"] == "Diana DeGette")]
DD= len(DDraw.value_counts())

RADraw = election_df.loc[(election_df["Candidate"] == "Raymon Anthony Doane")]
RAD = len(RADraw.value_counts())

CCSraw = election_df.loc[(election_df["Candidate"] == "Charles Casper Stockham")]
CCS = len(CCSraw.value_counts())

# Dividing each candidate's votes by the total amount of votes to get the 
# percentage of votes per candidate

CCSper = (CCS/totalvotes) * 100

DDper = (DD/totalvotes) * 100

RADper = (RAD/totalvotes) * 100

# Counting the Candidate column to see who's name appears the most to show who 
# won the election
winner = (election_df["Candidate"].value_counts().idxmax())


# Printing the results in terminal
print("Election Results")

print("----------------------------------")

print("Total Votes: " + str(totalvotes))

print("----------------------------------")

print("Charles Casper Stockham: " + str(round(CCSper,3)) + "%" + " (" + str(CCS) +  ")" )

print("Diane DeGette: " + str(round(DDper,3)) + "%" + " (" + str(DD) +  ")" )

print("Raymon Anthony Doane: " + str(round(RADper,3)) + "%" + " (" + str(RAD) +  ")" )

print("----------------------------------")

print("Winner: " + winner)

print("----------------------------------")

# Write this to output file

with open(output, "w") as f:
    f.write("Election Results\n")
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("\n")
    f.write("Total Votes: " + str(totalvotes) +"\n")
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("\n")
    f.write("Charles Casper Stockham: " + str(round(CCSper,3)) + "%" + " (" + str(CCS) +  ")\n")
    f.write("Diane DeGette: " + str(round(DDper,3)) + "%" + " (" + str(DD) +  ")\n" )
    f.write("Raymon Anthony Doane: " + str(round(RADper,3)) + "%" + " (" + str(RAD) +  ")\n" )
    f.write("\n")
    f.write("----------------------------------\n")
    f.write("\n")
    f.write("Winner: " + winner +"\n")
    f.write("\n")
    f.write("----------------------------------\n")


