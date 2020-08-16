import os
import csv

#Variables and analysis
por_primero = 0
por_seg = 0
por_tercero = 0
por_cuarto = 0
primero = 0
segundo = 0
tercero = 0
cuarto = 0
candidates = []
numbervotes = []
totalvotes = 0
aux = candidates

aux = dict()
list_keys= aux.keys

#Open and sort cvs
election_data = os.path.join("Resources","Homework 3_PyPoll_Resources_election_data.csv")
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

#The total number of votes cast
    for x in csvreader:
        totalvotes = totalvotes + 1
        aux = (x[2])

#The total number of votes each candidate won
        if x[2] not in candidates:
            candidates.append(x[2])
            index = candidates.index(x[2])
            numbervotes.append(1)
        else:
            index = candidates.index(x[2])
            numbervotes[index] += 1

    
# Dictionary
from collections import Counter
def winner(input):
    numbervotes = counter(input)
    dict = {}
    for value in numbervotes.value():
        dict[value] = []
    for (key, value) in numbervotes.items():
        dict[value].append(key)

#The percentage of votes each candidate won
    primero = sorted(dict.keys(),reverse=True)[0]
    por_primero = (primero/totalvotes)*100
    segundo = sorted(dict.keys(),reverse=True)[1]
    por_seg = (segundo/totalvotes)*100
    tercero = sorted(dict.keys(),reverse=True)[2]
    por_tercero = (tercero/totalvotes)*100
    cuarto = sorted(dict.keys(),reverse=True)[3]
    por_cuarto = (cuarto/totalvotes)*100

#Find the winning candidate
if x[2] not in candidates:
    candidates.append(x[2])
    index = candidates.index(x[2])
    numbervotes.append(1)
else:
    index = candidates.index(x[2])
    numbervotes[index] += 1

    winner = max(numbervotes)
    index = numbervotes.index(winner)
    winner_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(totalvotes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(numbervotes[i])}")
    print(f"{0:.3f}".format(por_primero))
    

print("--------------------------")
print(f"Winner: {winner_candidate}")
print("--------------------------")

f= open("main.txt","w+")
with open("main.txt", "w") as f:
    f.write("OUTPUT")