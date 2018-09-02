
install.packages("xml2")
# Do you want to install from sources the package which needs compilation?
# y/n: n

install.packages("aws.s3")
library("aws.s3")

# on command line:
# aws sts --profile gwu get-session-token --duration-seconds 129600
# AWS_ACCESS_KEY_ID: col 2
# AWS_SECRET_ACCESS_KEY: col 4
# AWS_SESSION_TOKEN: col 5 (whole thing)

Sys.setenv("AWS_ACCESS_KEY_ID" = "",
           "AWS_SECRET_ACCESS_KEY" = "",
           "AWS_DEFAULT_REGION" = "us-east-1",
           "AWS_SESSION_TOKEN" = "")

bucketlist()
get_bucket(bucket = 'gwu-workshop-stuckey')

# textdata <- readBin(con=get_object("s3://gwu-workshop-stuckey/us_interest_rates.csv"),what=character())

us_interest_rates <- s3read_using(read.csv, object="s3://gwu-workshop-stuckey/us_interest_rates.csv")
us_interest_rates
head(us_interest_rates)

