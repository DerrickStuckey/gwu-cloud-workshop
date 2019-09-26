## read CSV from S3

s3.url <- "http://s3.amazonaws.com/gwu-workshop-stuckey/Apple_Stock/AAPL.csv"

s3.csv <- read.table(s3.url, header=TRUE, sep=",", stringsAsFactors = FALSE)

head(s3.csv)

mean(s3.csv$Adj.Close)
var(s3.csv$Adj.Close)

min(s3.csv$Date)
