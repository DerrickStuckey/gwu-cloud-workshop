import urllib
import csv

link = "https://s3.amazonaws.com/stuckeys-bucket/us_interest_rates.csv"
f = urllib.urlopen(link)

years = []
rates = []

reader = reader = csv.DictReader(f)
for row in reader:
	years.append(row['Year'])
	rates.append(float(row['interest_rate']))

avg_rate = float(sum(rates)) / len(rates)

print("Average interest rate between %s and %s:" % (years[0], years[-1]))
print("%0.2f" % avg_rate)


