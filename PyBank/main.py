'''
PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''


# Import Dependencies
import os 
import csv
import pandas as pd

# Creating path to csv file
csvpath = os.path.join("C:/Users/17202/Documents/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv")

csv_path = "https://raw.githubusercontent.com/carchu9/Python-Challenge/main/PyBank/Resources/budget_data.csv"
budget_df = pd.read_csv(csv_path)

# Creating path to txt file
output =  ("C:/Users/17202/Documents/GitHub/Python-Challenge/PyBank/Analysis/Financial_Analysis.txt")

# Listing the variables
totalmonths = 0
monthchange = []
netchangelist = []
greatestincrease = ["", 0]
greatestdecrease = ["", 999999999]
totalnet = 0
revchange = 0
revchangelist = []


# Open the csvfile 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    # Store the header and make the firstrow variable
    csv_header = next(csvreader)
    firstrow = next(csvreader)
    
    # Count the total months
    totalmonths += 1
    # Calculate the total net revenue over the entire period
    totalnet += int(firstrow[1])
    # Create Variable to hold the previous rev in order to calculate average change
    previousrev = int(firstrow[1])
    
    # Loop through the data to find:
    for row in csvreader:
        
        # the total amount of months in the data
        totalmonths += 1
        # The total net revenue over the entire period
        totalnet += int(firstrow[1])
        
        # Calculating average change in revenue between the months over the 
        #entire period
        revchange =int(row[1]) - previousrev
        previousrev = int(row[1])
        revchangelist += [revchange]
        monthchange += [monthchange]
    
        # Looking for the month and amount that showed the greatest amount of
        # increase in revenue
        if revchange > greatestincrease[1]:
            greatestincrease[1] = revchange
            greatestincrease[0] =  row[0]

        # Looking for the month and amount that showed the greatest amount of
        # decrease in revenue  
        if revchange < greatestdecrease[1]:
            greatestdecrease[1] = revchange
            greatestdecrease[0] = row[0]
        revave = sum(revchangelist)/len(monthchange)

# Identifying the total number of months in the dataset
totalnumofmonths = len(budget_df["Date"].value_counts())
totalnumofmonths

# Identifying the total amount of revenue over the entire period
total = budget_df["Profit/Losses"].sum()
total

# Print to terminal
print("Financial Analysis")
print("------------------------------------------")

print("Total Months: " +str(totalnumofmonths))
print("Total: $" + str(total))
print("Average Change: $" + str(round(revave, 2)))
print("Greatest Increase in Profits: " + str(greatestincrease[0]) + " ($" + str(greatestincrease[1]) +")")
print("Greatest Decrease in Profits: " + str(greatestdecrease[0]) + " ($" + str(greatestdecrease[1]) +")")

# Using path to create/make changes to the txt file
with open(output, "w") as f:
    f.write("Financial Analysis\n")
    f.write("-------------------------------\n")
    f.write("\n")
    f.write("Total Months: " + str(totalnumofmonths) + "\n")
    f.write("Total: " + str(total) + "\n")
    f.write("Average Change: " + str(round(revave, 2)) + "\n")
    f.write("Greatest Increase in Profits: " + str(greatestincrease[0]) + " ($" + str(greatestincrease[1]) +")\n")
    f.write("Greatest Decrease in Profits: " + str(greatestdecrease[0]) + " ($" + str(greatestdecrease[1]) +")\n")
    f.close


