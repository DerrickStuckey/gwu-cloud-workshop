import urllib.request
import csv
import codecs

link = "https://s3.amazonaws.com/stuckey-test-bucket/us_interest_rates.csv"
f = urllib.request.urlopen(link)

years = []
rates = []

reader = csv.DictReader(codecs.iterdecode(f,'iso-8859-1'))
for row in reader:
	years.append(row['Year'])
	rates.append(float(row['interest_rate']))


avg_rate = float(sum(rates)) / len(rates)

print("Average interest rate between %s and %s:" % (years[0], years[-1]))
print("%0.2f" % avg_rate)


