# provide file name to open with financial data
filename = "budget_data.csv"

import csv
#read csv file and create lists from csv columns Profit & Losses (PandL) and Date (date)
PandL = []
date = []

with open(filename, "r") as input_file:
    csvreader = csv.reader(input_file, delimiter =",")
    for row in csvreader:
        PandL.append(row[1])
        date.append(row[0])
countrows = date
nrows = len(countrows)
total_months = nrows - 1

##create lists of difference in Profit and Loss month to month and record month of change##
change = []
month_change = []
counter = nrows - 2

for i in range(counter):
        diff = float(PandL[i+2]) - float(PandL[i+1])
        change.insert(i, diff)
        month_change.insert(i, str(date[i+2]))

# calculate sum of Profit and Losses total_PandL
reader = csv.DictReader(open(filename))
total_PandL = sum(float(row["Profit/Losses"]) for row in reader)

###calculate average change in profits (average_change) and max increase in profits plus max decrease in profits
#determine month max increase and decrease occured
average_change = round(sum(change) / len(change), 2)
max_increase_profits = max(change)
month_max_increase = month_change[change.index(max_increase_profits)]
max_decrease_profits = min(change)
month_max_decrease = month_change[change.index(max_decrease_profits)]

def print_output():
##### print results #####
    print("Financial Analysis")
    print("------------------------------------------------")
    print("Total number of months: " + str(total_months))
    print("Total: $" + str(int(total_PandL)))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + str(month_max_increase) + " ($" + str(int(max_increase_profits)) + ")")
    print("Greatest Decrease in Profits: " + str(month_max_decrease) + " ($" +str(int(max_decrease_profits)) +")")

print_output()

##### write to text file #####
with open("testfile.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------------------------\n")
    f.write("Total number of months: " + str(total_months))
    f.write("\nTotal: $" + str(int(total_PandL)))
    f.write("\nAverage Change: $" + str(average_change))
    f.write("\nGreatest Increase in Profits: " + str(month_max_increase) + " ($" + str(int(max_increase_profits)) + ")")
    f.write("\nGreatest Decrease in Profits: " + str(month_max_decrease) + " ($" +str(int(max_decrease_profits)) +")")
  

