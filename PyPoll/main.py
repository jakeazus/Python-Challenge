#Beginning of PyPoll Code
import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')
#Define the function
# def election_calc(election_data):
#     voterID = int(election_data[0])
#     candidate = str(election_data[2])

#     total = len(voterID)
    #The total number of votes can be represented by using the length function
    #total_votes = len(voterID)

# creates blank list for candidates
candidates_received_votes = []
#creates blank dict for candidates and the vote they received 
candidates_voted = {}

total = 0 
winner_of_election_votes = 0


with open(election_data_csv, newline="") as csvfile:

#     # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total = total + 1
        candidate_name = row[2]
        if candidate_name not in candidates_received_votes:
            candidates_received_votes.append(candidate_name)
            candidates_voted[candidate_name] = 0
        candidates_voted[candidate_name] = candidates_voted[candidate_name] + 1
print(f'Election Results')
print(f'-------------------------')    
print(f'Total Votes: {total}')
print(f'-------------------------')   


#Using this loop to calculate percentage votes and the winner, loops through four times
pypoll_text_file = os.path.join('Analysis', 'pypoll_output_text_file.txt')
with open(pypoll_text_file, 'w') as textfile:
    textfile.write(f'Election Results\n')
    textfile.write(f'-------------------------\n')
    textfile.write(f'Total Votes: {total}\n')
    textfile.write(f'-------------------------\n')    
    for candidate_name in candidates_received_votes:
        #the votes received lines pulls the individual votes for each candidate
        votes_received = candidates_voted[candidate_name]
        percent_candidate_won = (votes_received/total) * 100
        if votes_received > winner_of_election_votes:
            winner_of_election_votes = votes_received
            election_winner = candidate_name
        print(f"{candidate_name}: {percent_candidate_won:.3f}% ({votes_received})")
        textfile.write(f"{candidate_name}: {percent_candidate_won:.3f}% ({votes_received})\n")
    print(f"-------------------------\nWinner: {election_winner}\n-------------------------")
    textfile.write(f"-------------------------\nWinner: {election_winner}\n-------------------------\n")



#output text file








