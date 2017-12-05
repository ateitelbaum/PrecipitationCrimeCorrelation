#!/usr/bin/awk -f
BEGIN{
    FS = ","
    OFS = "|"
    inputFile = "NYPDComplaintData.csv"                          #1
    outputFile = "ComplaintData.txt"
    offenseLevelRegex = "(FELONY|MISDEMEANOR|VIOLATION)"         #2

    while((getline < inputFile ) > 0){
	if ($0 ~  "MANHATTAN"){
	    match($0, offenseLevelRegex, arr) 
	    print $2, $3, $8, arr[1] > outputFile
	}
    }
}
