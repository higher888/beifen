import pandas
import csv

df = pandas.read_csv('business_original.csv')
header = ["business_id", "full_address", "hours.Monday.open", "hours.Monday.close", "hours.Tuesday.open", "hours.Tuesday.close", "hours.Wednesday.open", "hours.Wednesday.close", "hours.Thursday.open", "hours.Thursday.close", "hours.Friday.open", "hours.Friday.close", "hours.Saturday.open", "hours.Saturday.close", "hours.Sunday.open", "hours.Sunday.close", "open", "city", "review_count", "name", "longitude", "state", "stars", "latitude"]
df.to_csv('businessTable.csv', colums = header)

