# basic import
import os
import csv

# Path to collect data from Resources folder
csv_path = os.path.join('Resources', 'election_data.csv')

# set up total vote variable
vote_count = 0

# Candidate dictionary
candidatetracker = {}

with open(csv_path, 'r') as csv_file:
    
    # Split data at commas
    csv_reader = csv.reader(csv_file, delimiter=",")

    # skip header
    csv_header = next(csv_reader)

    # loop thru rows 
    for row in csv_reader:
        
        # set CandidateCount to grab Candidates Name from csv
        CandidateCount = row[2]

        if CandidateCount in candidatetracker:
            candidatetracker[CandidateCount] = candidatetracker[CandidateCount] + 1
        else:
            candidatetracker[CandidateCount] = 1

# counting total votes for each candidate
KhanVotes = candidatetracker['Khan']
CorreyVotes = candidatetracker['Correy']
LiVotes = candidatetracker['Li']
OTooleyVotes = candidatetracker["O'Tooley"]

# sum of votes / total votes
vote_count = sum(candidatetracker.values())

# calculating percentage of votes for each candidate
Khan_Percent_Vote = round(((candidatetracker['Khan'])/(vote_count)) * 100, 2)
Correy_Percent_Vote = round(((candidatetracker['Correy'])/(vote_count)) * 100, 2)
Li_Percent_Vote = round(((candidatetracker['Li'])/(vote_count)) * 100, 2)
OTooley_Percent_Vote = round(((candidatetracker["O'Tooley"])/(vote_count)) * 100, 2)

# winner thru max function
winner = max(candidatetracker.values())

# set up variable for winner
NameWinner = ""

# looping thru candidates
for Candidate in candidatetracker:
    
    # if candidate votes = winner, they are the winner
    if candidatetracker[Candidate] == winner:
        NameWinner = Candidate

print("Election Results")
print("-----------------------------------------------------------")
print("Total Votes:  " + str(vote_count))
print("-----------------------------------------------------------")
print("Khan:  " + str(Khan_Percent_Vote) + "%   " + str(KhanVotes))
print("Correy:  " + str(Correy_Percent_Vote) + "%   " + str(CorreyVotes))
print("Li:  " + str(Li_Percent_Vote) + "%   " + str(LiVotes))
print("O'Tooley:  " + str(OTooley_Percent_Vote) + "%   " + str(OTooleyVotes))
print("-----------------------------------------------------------")
print("Winner:  " + str(NameWinner))
print("-----------------------------------------------------------")

textfile = open('election_analysis.txt', 'w')
textfile.write("Election Analysis\n")
textfile.write("----------------------------------------------------------\n\n")
textfile.write("Total Votes: " + str(vote_count) + "\n")
textfile.write("----------------------------------------------------------\n\n")
textfile.write("Khan: " + str(Khan_Percent_Vote) +  "%   " + str(KhanVotes) + "\n")
textfile.write("Correy: " + str(Correy_Percent_Vote) +  "%   " + str(CorreyVotes) + "\n")
textfile.write("Li: " + str(Li_Percent_Vote) +  "%   " + str(LiVotes) + "\n")
textfile.write("O'Tooley: " + str(OTooley_Percent_Vote) +  "%   " + str(OTooleyVotes) + "\n")
textfile.write("----------------------------------------------------------\n\n")
textfile.write("Winner:  " + str(NameWinner) + "\n")
textfile.write("----------------------------------------------------------\n\n")
textfile.close()


