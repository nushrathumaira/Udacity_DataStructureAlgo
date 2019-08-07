"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import collections
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def get_time_spent(x):
    return int(x[3])

def max_time(list, key_func=None):
    if not list:
        raise ValueError('empty list')
    longest_call_duration = 0
    longest_call_number = None
    call_duration = collections.defaultdict(int)
    # directionary of number-duration pairs
    for item in list:
        for number in item[0:2]:
            call_duration[number] += key_func(item)     
        #iterate through all numbers to find longest
        if call_duration[number] > longest_call_duration:
            longest_call_duration=call_duration[number]
            longest_call_number=number
	    
    return longest_call_number, longest_call_duration
    
    
telephone,call_time = max_time(calls,key_func=get_time_spent)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(telephone,call_time))
