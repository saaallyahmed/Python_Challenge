import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()
    # Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:
  

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
 # Track various 

    month = []
    profit_loss = []

    
    
    # Read each row of data after header 
    
    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))
        num_months = len(month)
        total = sum(profit_loss)
        
        change = []
        
    for y in range(1,num_months):
        current = profit_loss[y]
        previous = profit_loss[y-1]
        difference = current - previous
        change.append(difference)
        sum_of_changes = sum(change)
        Count_of_changes = len(change)
        Average_of_changes = round(sum_of_changes/Count_of_changes,2)
        Decrease = min(change)
        Increase = max(change)
        greatest_increase = change.index(Increase) + 1
        greatest_increase = (month [change.index(Increase) + 1])
        greatest_decrease = change.index(Decrease)
        greatest_decrease = (month [change.index(Decrease) + 1])
        
print("financial Anylysis")
print(f"Total: ${total}")
print(f"Total months:{num_months}")
print(f"Average change: ${Average_of_changes}")
print(f"Greatest Increase in profits: {greatest_increase} ${Increase}")
print(f"Greatest Increase in profits: {greatest_decrease} ${Decrease}")
        
    