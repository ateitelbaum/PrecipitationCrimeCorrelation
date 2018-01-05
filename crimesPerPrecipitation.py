#finds the average weekly crime count for each violent crime of dry weather and precipitation 

#!usr/bin/env python
from HourlyPrecipitation import hourlyPrecip
from CrimesPerHour import crimesPerHour
import pdfPlot

crimeCountPrecip = {}
crimeCountDry = {}
pHourCount = 0        #hours with precipitation
dHourCount = 0        #hours with no preciptation

#generator object with crimes per hour
cGen = crimesPerHour()
c = next(cGen)

for p in hourlyPrecip():
    if p[1] == "dry":
        dHourCount+=1
    if p[1] == "precip":
        pHourCount += 1
    #takes care of missing precipitation values, files are in decreasing time order 
    while (p[0] < c[0]):
        c = next(cGen)
    if p[0] == c[0]:
        #updates crime count
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
        try:            
            c = next(cGen)
        except StopIteration:
            pass
        
#formats data for graphing
keys = ['kidnapping', 'murder', 'arson', 'rape', 'robbery','harrassment','assault']
dryAverage = []
precipAverage = []
dryTotal = 0
precipTotal = 0

#finds average crimes for precipitation and dry for a week
for i in keys:
    dry = crimeCountDry[i] / dHourCount * 168
    dryTotal += dry
    dryAverage.append(dry)
    
    precip = crimeCountPrecip[i] / pHourCount * 168
    precipTotal += precip
    precipAverage.append(precip)
#adds total crime count for dry and precipitation
keys.append("total")
dryAverage.append(dryTotal)
precipAverage.append(precipTotal)
#plots graph
pdfPlot.plot(keys, precipAverage, dryAverage)

        
         
        

        
    
    
    
    
