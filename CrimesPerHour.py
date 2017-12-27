#!/usr/bin/env python
import re
def crimesPerHour():
    input_file = "ComplaintData.txt"
    violentCrimeRegex = "Robbery|Harrassment|Assault|Rape|Arson|Murder|Kidnapping"
    violentCrimeRegex = re.compile(violentCrimeRegex.upper())
    f = open(input_file)
    day = ''
    hour = ''
    crimeCount = {}
    

    for line in f:
        #field0 = date and time, field1 = crime 
        fields = line. split('|')
        fields[1] = fields[1][:2]

        #if theres a new day/hour combo
        if not (fields[0] == day and fields[1] == hour):
            if day:
                yield day +' '+  hour, crimeCount

            #reset hourly crime count    
            day = fields[0]
            hour = fields[1]
            crimeCount = {}
            
        #update crime count
        violentCrime = re.search(violentCrimeRegex, fields[2])
        if violentCrime:
            crime = violentCrime.group(0).lower()
            if crime in crimeCount:
                crimeCount[crime]+=1
            else:
                crimeCount[crime] = 1
    yield day + ' '+ hour, crimeCount

if __name__ == "__main__":
    x = list(crimesPerHour())
    for i in x:
        print(i)


        
    
    
