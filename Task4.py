"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

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

