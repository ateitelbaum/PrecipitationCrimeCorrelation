#yield a generator object with date and hour, precipitation

#!/usr/bin/env python

# format the date the same as the crime data
def formattedDayHour(dayHour):
    month = dayHour[5:7]
    day = dayHour[8:10]
    year = dayHour[0:4]
    hour = dayHour[11:13]
    return month + '/' + day + '/' + year + ' ' + hour

#generator object of hourly precipitationx
def hourlyPrecip():
    input_file = "PrecipitationData.csv"
    date = 0
    precipAmount = 1
    curDayHour = 0
    precip = -1

    f = open(input_file)
    for line in f:
        #field0 = date, field1 = precipitaion
        fields = line.split(',')
        dayHour = fields[0][:13]

        #if there is a new date hour combo yield previous date hour data
        if not curDayHour == dayHour:
            if precip == 0:
                fDayHour = formattedDayHour(curDayHour)
                yield fDayHour, "dry"
            elif precip == 1:
                fDayHour = formattedDayHour(curDayHour)
                yield fDayHour, "precip"
            curDayHour = dayHour
            #reset precip
            precip = -1

        #record precipitation
        if precip == -1 and fields[precipAmount] == "0.00\n":
            precip = 0
        elif not (fields[precipAmount] == '\n'):
            precip = 1
    f.close()
