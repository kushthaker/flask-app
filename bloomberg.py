#LIST TABLES EXAMPLE

# #!/usr/bin/env python

# import boto3

# # Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# # the environment before running this program.

# AWS_REGION = 'us-east-1'

# db = boto3.client('dynamodb',
#                   region_name = AWS_REGION)
                    
# tables = db.list_tables()
# print type(tables)
# print dir(tables['TableNames'][10])

#!/usr/bin/env python


# DESCRIBE TABLE EXAMPLE

import boto3

# Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# the environment before running this program.


AWS_REGION = 'us-east-1'

db = boto3.client('dynamodb',
                  region_name = AWS_REGION)
                    
table = db.describe_table(TableName = '2012')
print "\n"
print table['Table']['KeySchema']
print "\n"

# QUERY TABLE EXAMPLE

#!/usr/bin/env python

import boto3
from boto3.dynamodb.conditions import Key

# Remember to set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in
# the environment before running this program.

AWS_REGION = 'us-east-1'

db = boto3.resource('dynamodb',
                    region_name = AWS_REGION)
                    
table = db.Table('2012')
data = table.query(KeyConditionExpression = Key('Ticker').eq('GDP PIQQ Index') & Key('Date').between('2005-01-01', '2014-01-30'))

for i in data['Items']:
	print i['Date']
	print i['Value']

