#! /usr/bin/env python3

import csv
import json
import sys

data = {}

with open(sys.argv[1], "r") as f:
	reader = csv.DictReader(f, delimiter=";")
	for row in reader:
		for key in row:
			row[key] = row[key].replace(",",".")
			if row[key].isdigit():
				row[key] = int(row[key])
			
		row["Nr"] = int(row["Nr"])
		
		
		data[row["Nr"]] = row

with open(sys.argv[1]+".json", "w") as f:
	json.dump(data, f)