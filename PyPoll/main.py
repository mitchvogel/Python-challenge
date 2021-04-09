import os
import csv

# Path to collect data from Resources folder
csv_path = os.path.join('Resources', 'election_data.csv')

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

        CandidateCount = row[2]

        if CandidateCount in candidatetracker:
            candidatetracker[CandidateCount] = candidatetracker[CandidateCount] + 1
        else:
            candidatetracker[CandidateCount] = 1

KhanVotes = candidatetracker['Khan']
CorreyVotes = candidatetracker['Correy']
LiVotes = candidatetracker['Li']
OTooleyVotes = candidatetracker["O'Tooley"]
vote_count = sum(candidatetracker.values())

Khan_Percent_Vote = ((candidatetracker['Khan'])/(vote_count)) * 100
Correy_Percent_Vote = ((candidatetracker['Correy'])/(vote_count)) * 100
Li_Percent_Vote = ((candidatetracker['Li'])/(vote_count)) * 100
OTooley_Percent_Vote = ((candidatetracker["O'Tooley"])/(vote_count)) * 100

# winner = []

# winner.append(KhanVotes)
# winner.append(CorreyVotes)
# winner.append(LiVotes)
# winner.append(OTooleyVotes)

# electionwinner = max(winner)

# print(electionwinner)
# print(candidatetracker(electionwinner))


#print("Election Results")
#print("-----------------------------------------------------------")


