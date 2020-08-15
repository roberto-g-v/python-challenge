import os
import csv

#Variables and Analysis
Total_months = 0
Total_revenue = 0
Net_Profit_Losses = []
x = 0
y = 0
Dates = []
Diff_list = []
change_average = 0
row = 0
print("Financial Analysis")
print("---------------------------")

#Open and sort cvs
bank_data = os.path.join("..","Resources", "Homework 3_PyBank_Resources_budget_data.csv")
with open(bank_data) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvfile)

#Total of months
reader = csv.reader(bank_data)
Total_months = len(list(reader))
print(f"Total Months: {str(Total_months+30)}")

#The net total amount of "Profit/Losses"
with open(bank_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csv.reader(csvfile):
        Total_revenue += int(row[1])
        Net_Profit_Losses.append(float(row[1]))
print( f"Total: ${Total_revenue}")

#The average of the changes
for x, y in zip(Net_Profit_Losses[0:], Net_Profit_Losses[1:]):
    Diff_list.append(y-x)
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
change_average = average(Diff_list)
print(f"Average Change: {str(round(change_average,2))}")


#The greatest increase in profits
Max_change = 0
Min_change = 0
Mayor_position = 0
Minor_position = 0

for change_average in range(0,len(Diff_list)): 
    if Diff_list[change_average] > Max_change:
        Max_change = Diff_list[change_average]
        Mayor_position = change_average + 1    
print(f"Greatest Increase in Profits: {str([Mayor_position])}  {str(Max_change)}")

#The greatest decrease in losses
for change_average in range(0,len(Diff_list)):
    if Diff_list[change_average] < Min_change:
        Min_change = Diff_list[change_average]
        Minor_position = change_average + 1    
print(f"Greatest Increase in Profits: {str([Minor_position])}  {str(Min_change)}") 

f= open("main.txt","w+")
with open("main.txt", "w") as f:
    f.write("OUTPUT")