## read CSV from S3

AAPL.prices <- read.table("http://s3.amazonaws.com/gwu-workshop-stuckey/AAPL.csv",
                              header=TRUE, sep=",")

summary(AAPL.prices)

head(AAPL.prices)

mean(AAPL.prices$Adj.Close)
var(AAPL.prices$Adj.Close)

