#!/usr/bin/env python
import re
def CrimesPerHour():
    input_file = "ComplaintData.txt"
    violentCrimeRegex = "Robbery|Harrassment|Assault|Rape|Arson|Murder|Kidnapping"
    violentCrimeRegex = re.compile(violentCrimeRegex.upper())
    f = open(input_file)
    day = ''
    hour = ''
    crimeCount = 0
    for line in f:
        fields = line. split('|')
        fields[1] = fields[1][:2]
        if not (fields[0] == day and fields[1] == hour):
            yield day, hour, crimeCount
            day = fields[0]
            hour = fields[1]
            crimeCount = 0
        if re.search(violentCrimeRegex, fields[2]):
            crimeCount+=1
    yield day, hour, crimeCount


        
    
    
