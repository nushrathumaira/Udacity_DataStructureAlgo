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
# use regular expression to define pattern for bangalore area code
bangalore_area_code = r'^\(080\)'
area_code = r'^\(.*\)'
mobile_prefix = r'^\d{4}'

# create nested list of matched indexes
#matched_list = [(index,index2,p) for index, c in enumerate(calls) #for index2, p in enumerate(c)if re.search(bangalore_area_code,p)]



#bangalore_caller_list = []
bangalore_receivers = set()
from_bangalore = 0
to_bangalore = 0

for index,c in enumerate(calls):
    caller = c[0]
    receiver = c[1]
   
    if re.search(bangalore_area_code,caller):
        from_bangalore += 1
        bangalore_receivers.add(receiver)
        if re.search(bangalore_area_code,receiver):
            to_bangalore += 1
 


percentage_bangalore_receivers = round((to_bangalore / from_bangalore) * 100, 2)


#receivers_by_bangalore=[  c[1] for c in calls if c[0] in bangalore_caller_list]
sorted_receivers_by_bangalore = sorted(bangalore_receivers)
print("The numbers called by people in Bangalore have codes:")
codes = set()
for number in sorted_receivers_by_bangalore:
    code = re.match(area_code,number) or re.match(mobile_prefix,number)
    if code[0] not in codes:
        codes.add(code[0])
        print(code[0])
    
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage_bangalore_receivers))
 
