import os
import csv

#Opening and sorting csv
bank_data = os.path.join("..","Resources", "Homework 3_PyBank_Resources_budget_data.csv")
with open(bank_data) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   print(csvreader)
   csv_header = next(csvreader)
   print(f"{csv_header}")
   for row in csvreader:
       print(row)

#Variables and Analysis
Months = 0
total = 0
Profit_Losses = []
x = 0
y = 0
Dates = []
Diff_list = []
change_average = 0

print("Financial Analysis")
print("---------------------------")

#Total of months
reader = csv.reader(bank_data)
row = len(list(reader))
print(f"Total Months: {str(row+30)}")

#The net total amount of "Profit/Losses"
with open(bank_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total = 0
    for row in csv.reader(csvfile):
        total += int(row[1])
print( f"Total: ${total}")

#The average of the changes
for x, y in zip(Profit_Losses[0:],Profit_Losses[1:]):
       Diff_list.append(y-x)
       def average(numbers):
           lenght = len(numbers)
           total = 0
           for number in numbers:
               total += number
               return total / lenght
               change_average = average(Diff_list)
print(f"Average change: ${str(change_average)}")

#The greatest increase in profits
Max_change = 0
Min_change = 0
Mayor_position = 0
Minor_position = 0

for change_average in range(0,len(Diff_list)): 
    if Diff_list[change_average]>Max_change:
        Max_change = Diff_list[change_average]
        Mayor_position = change_average + 1    
print(f"Greatest Increase in Profits: {str([Mayor_position])}  {str(Max_change)}")

#The greatest decrease in losses
for change_average in range(0,len(Diff_list)):
    if Diff_list[change_average]>Min_change:
        Min_change = Diff_list[change_average]
        Minor_position = change_average + 1    
print(f"Greatest Increase in Profits: {str([Minor_position])}  {str(Min_change)}") 