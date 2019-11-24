
filename = "budget_data.csv"

import csv

input_file = open(filename, "r")
csvreader = csv.reader(input_file)

#calculate total months of in dataset, return pointer to 0 when done
total_months = len(list(csvreader)) - 1
input_file.seek(0) 

# calculate sum of Profit and Losses
reader = csv.DictReader(open(filename))
total = sum(float(row["Profit/Losses"]) for row in reader)

#  print results
print("Financial Analysis")
print("---------------------------")
print("Total number of months: " + str(total_months))
print("Total: $" + str(total))


input_file.close()