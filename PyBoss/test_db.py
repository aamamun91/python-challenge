import os
import csv
import re
from datetime import datetime


datapath = os.path.join('employee_data1.csv')

employee_name = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

with open(datapath, newline="") as employeefile:
	employee = csv.reader(employeefile, delimiter=",")
	next(employee)

	for row in employee:
		employee_name.append(row[1])
		dob.append(row[2])
		#datetime.strptime(str(dob), '%Y-%m-%d')
		#dob.strftime('%d/%m/%Y')
		ssn.append(row[3])
		state.append(row[4])

	for i in employee_name:
		first_name.append(i.split(' ', 1)[0])
		last_name.append(i.split(' ', -1)[1])


print(dob)

date_obj = datetime.strptime(str(dob), '%Y-%b-%d')
print(date_obj.strftime('%d/%m/%Y'))

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}