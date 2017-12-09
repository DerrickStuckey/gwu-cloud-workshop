import urllib.request

link = "https://s3.amazonaws.com/stuckey-test-bucket/us_interest_rates.csv"
f = urllib.request.urlopen(link)
myfile = f.read()
print(myfile)
