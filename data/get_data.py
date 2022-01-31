# set up credentials: https://docs.aws.amazon.com/cli/latest/userguide/welcome-examples.html

import boto3
import sqlite3
import pandas as pd
 
s3 = boto3.client('s3')
s3.download_file('jnj-capstone-2022', 'jnj_capstone.sqlite', 'data/jnj_capstone.sqlite')
con = sqlite3.connect('data/jnj_capstone.sqlite')

df = pd.read_sql_query("select * from requests", con)
print(df.head())

con.close()
