import csv

rows = []

with open('static/Cars.csv', 'r') as csvfile:
	csvreader = csv.DictReader(csvfile)
	rows = list(csvreader)

# print(rows)
# for row in rows[:5]:
# 	print(row['Id'] + "-" + row['Name'] + "-" + row['Price'])