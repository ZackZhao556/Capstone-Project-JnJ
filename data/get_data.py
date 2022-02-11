# set up credentials: https://docs.aws.amazon.com/cli/latest/userguide/welcome-examples.html

import boto3
import pandas as pd
 
s3 = boto3.client('s3')
s3.download_file('jnj-capstone-2022', 'tweets.csv', 'tweets.csv')
pd.read_csv("tweets.csv")
