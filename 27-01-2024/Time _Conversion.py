"""Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45"""

"logic 1:"

from datetime import datetime

def timeConversion(s):
    
    time_object = datetime.strptime(s, '%I:%M:%S%p')

    result = time_object.strftime('%H:%M:%S')
    return result

input_time = '07:05:45PM'
output_time = timeConversion(input_time)
print(output_time)

"logic 2:"

def timeConversion(s):
    
    hh, mm, ss = map(int, s[:-2].split(':'))
    am_pm = s[-2:]

    if am_pm == 'AM' and hh == 12:
        hh = 0
    elif am_pm == 'PM' and hh != 12:
        hh += 12

    result = '{:02d}:{:02d}:{:02d}'.format(hh, mm, ss)
    return result

input_time = '07:05:45PM'

output_time = timeConversion(input_time)
print(output_time)
