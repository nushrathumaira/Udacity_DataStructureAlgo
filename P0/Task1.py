"""
Read file into texts and calls.
It's ok if you don't understand how to read files.

"""
from collections import Counter
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#flat_list = [item for sublist in texts for item in sublist]
#c = Counter(flat_list)
texts_and_calls = texts+calls
unique_phone_numbers = []

for index, items in enumerate(texts_and_calls):
    if items[0] not in unique_phone_numbers:
        unique_phone_numbers.append(items[0])
    if items[1] not in unique_phone_numbers:
        unique_phone_numbers.append(items[1])
print("There are {} different telephone numbers in the records".format(len(unique_phone_numbers)))
#print("There are {} different telephone numbers in the records".format(len(c.keys())))
#list_set = set(tuple(l1[0],l1[1]) for l1 in texts)
