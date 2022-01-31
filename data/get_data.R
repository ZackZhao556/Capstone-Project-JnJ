library(aws.s3)
library(readr)

# set default region to us-west-1, R thinks you want us-east-1
Sys.setenv(AWS_DEFAULT_REGION = "us-west-1")

x <- get_object(
  object = "jnj_capstone.sqlite",
  bucket = "jnj-capstone-2022", 
  file = "data/jnj_capstone-r.sqlite"
)

write_file(x, "data/jnj_capstone.sqlite")
