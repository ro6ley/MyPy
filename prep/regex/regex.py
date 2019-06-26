import re

line = 'hello, my name is Ex, RegEx and today is August 24th'

match = re.search(r"([a-zA-Z]+) (\d+)", line)

# Find the date in the above statement
if match:
    print('Found the date: {}'.format(match.group()))
else:
    print('Date not found.')
