import urllib

link = "https://s3.amazonaws.com/stuckeys-bucket/us_interest_rates.csv"
f = urllib.urlopen(link)
myfile = f.read()
print(myfile)
