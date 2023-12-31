"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s="12:01:00PM"
Return '12:01:00'.

s="12:01:00AM"
Return '00:01:00'.
"""

def time_conversion(s: str):
    # Write your code here
    if s.endswith('PM') and s[:2] < '12':
        return str(int(s[:2])+12) + s[2:-2]
    elif s.endswith('AM') and s[:2] >= '12':
        return str(int(s[:2])-12).zfill(2) + s[2:-2]
    else:
        return s[:-2]
    

if __name__ == '__main__':
    s = input()
    result = time_conversion(s)
    print(result)