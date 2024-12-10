import re

def mul(match):
    ##Remove mul( )
    cleaned_match = match[4:-1]
    x, y = cleaned_match.split(',')
    x = int(x)
    y = int(y.strip())
    return x * y

f = open("./inputs/Day3.txt", "r").read()

pattern = r'(mul\(\d{1,3},\s*\d{1,3}\))'
pattern_do = r'do\(\)'
pattern_dont = r"don't\(\)"

regex = re.compile(pattern)
regex_do = re.compile(pattern_do)
regex_dont = re.compile(pattern_dont)

f_parsed = list(regex.finditer(f))
f_do = list(regex_do.finditer(f))
f_dont = list(regex_dont.finditer(f))

events = sorted(
    [(m.start(), "do") for m in f_do] + [(m.start(), "dont") for m in f_dont]
)

sum = 0
switch = True

event_index = 0
for match in f_parsed:
    start = match.start()
    while event_index < len(events) and events[event_index][0] < start:
        event_type = events[event_index][1]
        switch = event_type == "do"
        event_index += 1
    
    if switch:
        sum += mul(match.group(0))

print(sum)
