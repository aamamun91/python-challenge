

import csv
import os

electionData_Path = os.path.join('election_data_2.csv')


total_voteCast = 0
candidate_list = []
candidates = set()
vote = []
percent_vote = []
output={}


with open(electionData_Path, newline="") as election: 
	election = csv.reader(election, delimiter=',')
	next(election)


	for row in election:
		total_voteCast = total_voteCast + 1	
		candidate_list.append(row[2])
	
	print("Total vote cast: " + str(total_voteCast))

	candidates = set(candidate_list)
	candidates = list(candidates)

	for item in candidate_list:
		if item in output:
			output[item]=output.get(item)+1
		else:
			output[item]=1

	for key, value in output.items():
		print(str(key) + ": " + str(("{:.1%}".format(value/total_voteCast))) + " ("+ str(value)+ ")")
