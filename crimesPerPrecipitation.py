#!usr/bin/env python
from HourlyPrecipitation import hourlyPrecip
from CrimesPerHour import crimesPerHour
crimeCountPrecip = {}
crimeCountDry = {}
pHourCount = 0        #hours with precipitation
dHourCount = 0        #hours with no preciptation

for c in crimesPerHour():
    for p in hourlyPrecip():
        if p[1] == "dry":
            dHourCount+=1
        if p[1] == "precip":
            pHourCount += 1
        if p[0] > c[0]:
            print(p[0] , c[0])
        if p[0] == c[0]:
            for crime in c[1]:
                if p[1] == "dry":
                    if crime in crimeCountDry:
                        crimeCountDry[crime] +=1
                    else:
                        crimeCountDry[crime] = 1
                else:
                    if crime in crimeCountPrecip:
                        crimeCountPrecip[crime] +=1
                    else:
                        crimeCountPrecip[crime] = 1
print("Dry:")
for i in crimeCountDry:
    x = crimeCountDry[i] / dHourCount
    print(i, x)
print("Wet:")
for i in crimeCountPrecip:
    x = crimeCountPrecip[i] / pHourCount
    print(i, x) 
        
         
        
    
        
    
    
    
    
