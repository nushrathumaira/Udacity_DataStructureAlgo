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



all_numbers = set()
for t in texts:
    all_numbers.add(t[0])
    all_numbers.add(t[1])
for c in calls:
    all_numbers.add(c[1])
    
 
"""
Criterion for the number which is doing telemarketing: (all should be satisfied)
Number which is making calls.
Number which is not receiving any calls.
Number which is not sending any text messages.
Number which is not receiving any text messages.
"""

telemarketers = set()
for c in calls:
    if c[0] not in all_numbers:
        telemarketers.add(c[0])
        
print("These numbers could be telemarketers: ")
for number in sorted(telemarketers):
     print(number)