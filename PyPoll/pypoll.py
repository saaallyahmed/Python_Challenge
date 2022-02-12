import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
  

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    Candidate = []
    Votes=[]
    
    for row in csvreader:
        Candidate.append(row[2])
        
    Total_Votes = len(Candidate)
    

        
    Khan_Votes = Candidate.count("Khan")
    Correy_Votes = Candidate.count ("Correy")
    Li_Votes = Candidate.count("Li")
    OTooley_Votes = Candidate.count("O'Tooley")
    
   
   
    
    Khan_Win = Khan_Votes/Total_Votes
    Correy_Win = Correy_Votes/Total_Votes
    Li_Win = Li_Votes/Total_Votes
    OTooley_Win = OTooley_Votes/Total_Votes
    
 #find the Candidate with the most votes
    Candidates_List = [Khan_Win, Correy_Win, Li_Win,OTooley_Win] 
    maxVotes =Candidates_List.index(max(Candidates_List))
    if maxVotes == 0:
        Winner = "Khan"
    elif maxVotes == 1:
        Winner = "Correy"
    elif maxVotes == 2:
        Winner = "Li"
    else:
        Winner ="OTooley"



    
print ("Election Results")
print (f"Total Votes: {Total_Votes}")
print (f"Khan: {Khan_Win:.3%} ({Khan_Votes})")
print (f"Correy: {Correy_Win:.3%} ({Correy_Votes})")
print (f"Li: {Li_Win:.3%} ({Li_Votes})")
print (f"OTooley: {OTooley_Win:.3%} ({OTooley_Votes})")
print(f"Winner: {Winner}")
