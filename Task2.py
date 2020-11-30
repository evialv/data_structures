"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import re
from collections import Counter
from datetime import datetime

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
numbers={}
for i in range(len(calls)):
    y=calls[i][2]
    x= calls[i][2]
    datetime_object = datetime.strptime(x, '%d-%m-%Y %H:%M:%S')
    if datetime_object.month == 9 and datetime_object.year == 2016:
        if calls[i][0] not in numbers:
            k=calls[i][0]
            numbers[calls[i][0]] = int(calls[i][3])
        else:
            numbers[calls[i][0]] += int(calls[i][3])
        if calls[i][1] not in numbers:
            numbers[calls[i][1]] = int(calls[i][3])
        else:

            numbers[calls[i][1]] += int(calls[i][3])



k = Counter(numbers)
high = k.most_common()


print(high[0][0],"spent the longest time,",high[0][1]," seconds, on the phone during September 2016.")
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

