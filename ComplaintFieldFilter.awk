#filters data so it only prints complaints in Manhattan between 2007-2016
#prints date, time and crime

#!/usr/bin/awk -f
BEGIN{
    FS = ","
    OFS = "|"
    inputFile = "NYPDComplaintData.csv"                                   

    #filter out only Manhattan, and between 2007-2016
    while((getline < inputFile ) > 0){
	if (($0 ~  "MANHATTAN") && ($2 ~ /200[7-9]$|201[0-6]$/)){
	    #date, time, crime 
	    print $2, $3, $8        
	}
    }
}
