import timestamp
from conf import tokens

for each_token in tokens:
    dropstamp = timestamp.Timestamp(token = each_token)
    dropstamp.timestamp()
