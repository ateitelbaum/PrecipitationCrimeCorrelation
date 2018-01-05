#generates date and hour, dictionary of violent crime counts 

#!/usr/bin/env python
import re
def crimesPerHour():
    input_file = "ComplaintData.txt"

    violentCrimeRegex = "Robbery|Harrassment|Assault|Rape|Arson|Murder|Kidnapping"
    violentCrimeRegex = re.compile(violentCrimeRegex.upper())
    
    day = ''
    hour = ''
    crimeCount = {}

    f = open(input_file)
    for line in f:
        #field0 = date and time, field1 = time, field2 = crime 
        fields = line. split('|')
        #extracts only the hour 
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
            #checks if the dictionary has a value for that crime yet
            if crime in crimeCount:
                crimeCount[crime]+=1
            else:
                crimeCount[crime] = 1
    #takes care of the lastline
    yield day + ' '+ hour, crimeCount
    f.close()



        
    
    
