

import os 
import csv
import pandas as pd

csvpath = os.path.join("C:/Users/17202/Documents/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv")

csv_path = "https://raw.githubusercontent.com/carchu9/Python-Challenge/main/PyBank/Resources/budget_data.csv"
budget_df = pd.read_csv(csv_path)

output =  ("C:/Users/17202/Documents/GitHub/Python-Challenge/PyBank/Analysis/Financial_Analysis.txt")


totalmonths = 0
monthchange = []
netchangelist = []
greatestincrease = ["", 0]
greatestdecrease = ["", 999999999]
totalnet = 0
revchange = 0
revchangelist = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    firstrow = next(csvreader)
    
    totalmonths += 1
    totalnet += int(firstrow[1])
    previousrev = int(firstrow[1])
    
    for row in csvreader:
        
        totalmonths += 1
        totalnet += int(firstrow[1])
        
        revchange =int(row[1]) - previousrev
        previousrev = int(row[1])
        revchangelist += [revchange]
        monthchange += [monthchange]
    
        if revchange > greatestincrease[1]:
            greatestincrease[1] = revchange
            greatestincrease[0] =  row[0]
                
        if revchange < greatestdecrease[1]:
            greatestdecrease[1] = revchange
            greatestdecrease[0] = row[0]
        revave = sum(revchangelist)/len(monthchange)


totalnumofmonths = len(budget_df["Date"].value_counts())
totalnumofmonths


total = budget_df["Profit/Losses"].sum()
total

print("Financial Analysis")
print("------------------------------------------")

print("Total Months: " +str(totalnumofmonths))
print("Total: $" + str(total))
print("Average Change: $" + str(round(revave, 2)))
print("Greatest Increase in Profits: " + str(greatestincrease[0]) + " ($" + str(greatestincrease[1]) +")")
print("Greatest Decrease in Profits: " + str(greatestdecrease[0]) + " ($" + str(greatestdecrease[1]) +")")



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


