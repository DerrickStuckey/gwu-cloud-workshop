## read CSV from S3

us_10year_rates <- read.table("http://s3.amazonaws.com/stuckeys-bucket/us_10year_rates.csv",
                              header=TRUE, sep=",")

summary(us_10year_rates)

head(us_10year_rates)

mean(us_10year_rates$interest_rate)

