import csv
import sys
import os

# Split Database by multi small documents
def data_spliter_toCSV(data_file, each_max_row):
	file_name = ""
	number = 0
	os.makedirs("chunks", exist_ok=True)
	with open(data_file) as data:
		reader = csv.DictReader(data, fieldnames=["email"])
		for index, row in enumerate(reader):
			if index % each_max_row == 0:
				file_name = f"chunks/chunk_{number}.csv"
				number += 1
				print(f"file: chunk_{number}.csv")
			with open(f"chunks/chunk_{number}.csv", "a") as chunk:
				writer = csv.DictWriter(chunk, fieldnames=["email"])
				writer.writerow({"email" : row["email"]})



data_spliter_toCSV(str(sys.argv[1]), int(sys.argv[2]))

# to run 
# python3 main.py file_name_toSplit number_lines
# or
# python main.py file_name_toSplit number_lines
