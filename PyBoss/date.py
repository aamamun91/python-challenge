

import datetime

date1=["2015-01-30"]
date1=str(date1)

print(type(date1))

date1 = datetime.datetime.strptime(date1, "%Y-%m-%d").strftime("%d-%m-%Y")

print(date1)