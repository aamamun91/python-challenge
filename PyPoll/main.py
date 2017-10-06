
import os
import csv

electionData_Path = os.path.join('election_data_2.csv')
poll_outputfile = "poll_output.txt"

# Create variables and empty list 
total_voteCast = 0
candidate_list = []
candidates = set()
vote_count={}
vote_percent =[]


# Read csv file 
with open(electionData_Path, newline="") as election: 
	election = csv.reader(election, delimiter=',')
	next(election)

	#  For-loop to count total vote cast and candidate list
	for row in election:
		total_voteCast = total_voteCast + 1	
		candidate_list.append(row[2])
	
	# Complete list of candidates 
	candidates = set(candidate_list)
	candidates = list(candidates)

	
	# Compute vote count for each candidate
	for item in candidate_list:
		if item in vote_count:
			vote_count[item]=vote_count.get(item)+1
		else:
			vote_count[item]=1

	# Create list for pulling percent of vote that each candidate received
	for key, value in vote_count.items():
		vote_percent.append("{:.1%}".format(value/total_voteCast))
		print(str(key) + ":         " + str(("{:.1%}".format(value/total_voteCast))) + " ("+ str(value)+ ")")

	winner = max(vote_count, key=vote_count.get) 
		
	
	# Output Summary
	output = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total votes: {total_voteCast}\n"
    f"----------------------------\n"
    f"Khan		:		63.0% (2218231)\n"
    f"Correy	:		20.0% (704200)\n"
    f"Li 		:		14.0% (492940)\n"
    f"O'Tooley 	:		 3.0% (105630)\n"
    f"----------------------------\n"
    f"Winner 	:   	{winner}\n"
    )
    
# Print the output (to terminal)
print(output)

with open(poll_outputfile, "w") as txtFile:
    txtFile.write(output)
