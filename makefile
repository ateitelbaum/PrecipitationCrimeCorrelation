

all: ComplaintData.txt PrecipitationData.csv plot.pdf

ComplaintData.txt: ComplaintFieldFilter.awk NYPDComplaintData.csv
	gawk -f ComplaintFieldFilter.awk | sort -r -n -b -t'/' -k3 -k1 -k2 -k3.6,3.13  > ComplaintData.txt   #the sort sorts based on date then hour 

PrecipitationData.csv: WeatherData.csv
	cut -f6,25 -d ',' < WeatherData.csv | sort -n -r > PrecipitationData.csv 

plot.pdf: crimesPerPrecipitation.py pdfPlot.py CrimesPerHour.py HourlyPrecipitation.py
	python3 crimesPerPrecipitation.py 

clean:
	rm -f *~ ComplaintData.txt PrecipitationData.csv result.txt plot.pdf
