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
