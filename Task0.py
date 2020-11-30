"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
last=len(calls)
print("First record of texts,",texts[0][0],"texts",texts[0][1],"at time",texts[0][2])
print("Last record of calls,",calls[last-1][0],"calls",calls[last-1][1],"at time",calls[last-1][2])

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
numbers = set()
for i in range(len(texts)):
    numbers.add(texts[i][0])
    numbers.add(texts[i][1])
for i in range(len(calls)):
    numbers.add(calls[i][0])
    numbers.add(calls[i][1])
count = len(numbers)
print("There are", count, " different telephone numbers in the records.")
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.


Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

numbers = []
bangore_number=0
all_numbers=0
for i in range(len(calls)):
    y = calls[i][0]
    # matches number in parenthesis
    bangore = re.search("(\((\d+)\))", calls[i][0])

    if bangore is not None:
        bangore = bangore.group(0)

    if bangore == "(080)":
        fixed = re.search("(\((\d+)\))", calls[i][1])

        tele = re.search("(140\d+)", calls[i][1])
        mobile = re.search("(\d{4})", calls[i][1])

        if fixed is not None:

            all_numbers+=1
            if fixed.group(0) not in numbers:
                numbers.append(fixed.group(0))
            if fixed.group(0)=='(080)' :
                bangore_number+=1

        elif tele is not None:
            all_numbers += 1
            if tele.group(0) not in numbers:
                numbers.append(tele.group(0))

        elif mobile is not None:
            all_numbers += 1
            x=mobile.group(0)[0]
            if mobile.group(0) not in numbers and (mobile.group(0)[0] == '9' or mobile.group(0)[0] == '8' or mobile.group(0)[0] == '7'):
                numbers.append(mobile.group(0))

        else:
            exit()

numbers.sort(key=str)

print("The numbers called by people in Bangalore have codes:")
for each in range(len(numbers)):
    print(numbers[each], "\n")
print(round(bangore_number/all_numbers*100, 2),"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

non_tele_numbers = set()
pos_tele_numbers = set()
for i in texts:
    non_tele_numbers.add(i[0])
    non_tele_numbers.add(i[1])
for i in calls:
    pos_tele_numbers.add(i[0])
    non_tele_numbers.add(i[1])
possible_tele_numbers =  sorted(pos_tele_numbers.difference(non_tele_numbers))
print("These numbers could be telemarketers: \n{}".format('\n'.join(possible_tele_numbers)))