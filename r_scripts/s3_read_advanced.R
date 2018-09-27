install.packages("xml2")
# Do you want to install from sources the package which needs compilation?
# y/n: n

install.packages("aws.s3")
# if that fails try:
# install.packages("aws.s3", repos = c("cloudyr" = "http://cloudyr.github.io/drat"), INSTALL_opts = "--no-multiarch")

library("aws.s3")

# obtain from ~/.aws/credentials
Sys.setenv("AWS_ACCESS_KEY_ID" = "",
           "AWS_SECRET_ACCESS_KEY" = "",
           "AWS_DEFAULT_REGION" = "us-east-1")

# list all the buckets for this account
bucketlist()

# list all the s3 objects in bucket 'gwu-workshop-stuckey'
workshop_bucket <- get_bucket(bucket = 'gwu-workshop-stuckey')
for (obj in workshop_bucket) {
  key <- obj$Key
  print(key)
}

# read the object we are interested in, "us_interest_rates.csv", as a dataframe, using read.csv
us_interest_rates <- s3read_using(read.csv, object="us_interest_rates.csv", bucket="gwu-workshop-stuckey")
head(us_interest_rates)

