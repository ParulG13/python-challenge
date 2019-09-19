import csv
import os

# input file
file_path = os.path.join("election_data.csv")
#output file
output_file_path = "election_data_analysis.txt"

#open file in write mode
outFile = open(output_file_path, "w+")

# function to write output in console and file
def printOutput(vLine):
  print(vLine)
  outFile.write(vLine)
  outFile.write("\n")

#dict for storing key as candidate names and value as number of votes
candidate_vote_count_d = {}

# read file
with open(file_path, 'r') as input_file:
    input_read = csv.reader(input_file, delimiter=',')
    # ignore the header
    csv_header = next(input_read)

    total_votes = 0
    vote_count = 0

    # access row by row data from file
    for row in input_read:
        candidate_name = row[2]
        total_votes = total_votes + 1

        # Increment candidate vote count
        if candidate_name in candidate_vote_count_d:
            vote_count = candidate_vote_count_d.get(candidate_name)
            vote_count = vote_count + 1
            candidate_vote_count_d[candidate_name] = vote_count

        # get the candidate names as key for the first time
        else:
            candidate_vote_count_d[candidate_name] = 1

    # calculate percentage for each candidate
    # display winner

# display output
printOutput("Election Results")
printOutput("---------------------------")
printOutput("Total Votes: {}".format(total_votes))
printOutput("---------------------------")
for candidate, votes in candidate_vote_count_d.items():
    # get vote percenatge and format to round and print 3decimals
    vote_percent = format((votes / total_votes) * 100, '.3f')
    printOutput("{} : {}% ({})".format(candidate, vote_percent, votes))
    # find the winner
    winner_votes = max(candidate_vote_count_d.values())
    if votes == winner_votes:
        winner = candidate
printOutput("---------------------------")
printOutput("Winner: {}".format(winner))
printOutput("---------------------------")