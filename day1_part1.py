import csv

def part_1(file_name: str) -> int:
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		
		previous_row = None
		decreasing_counter = 0
		for row in csv_reader:
			data = int(row[0])
			if previous_row and previous_row < data:
				decreasing_counter += 1
			previous_row = data
	return decreasing_counter

def part_2(file_name: str) -> int:
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		#will now be a tuple of 3 elements
		previous_row = (None,None,None)
		decreasing_counter = 0
		for row in csv_reader:
			data = int(row[0])
			#the difference between any triple is just the edge numbers as the middle 2 are shared
			if previous_row[2] and previous_row[2] < data:
				decreasing_counter += 1
			previous_row = (data, previous_row[0], previous_row[1])
	return decreasing_counter

def generic_day1(file_name: str, lookback_window: int) -> int:
	with open(file_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		previous_row = [None for i in range(lookback_window)]
		decreasing_counter = 0
		for row in csv_reader:
			data = int(row[0])
			#the difference between any triple is just the edge numbers as the middle 2 are shared
			if previous_row[lookback_window-1] and previous_row[lookback_window-1] < data:
				decreasing_counter += 1
			#keep the new at 0th and pop the last one off
			previous_row = [data] + previous_row[:-1]

	return decreasing_counter


assert(part_1("test_input_1.csv") == 4)
assert(part_1("test_input_2.csv") == 0)
assert(part_1("test_input_3.csv") == 0)

print("day 1 input with 1 lookback", part_1("day1_input.csv"))


assert(part_2("test_input_1.csv") == 2)
assert(part_2("test_input_2.csv") == 0)
assert(part_2("test_input_3.csv") == 0)

print("day 1 input with 3 lookback", part_2("day1_input.csv"))

assert(generic_day1("test_input_1.csv", 1) == 4)
assert(generic_day1("test_input_2.csv",1) == 0)
assert(generic_day1("test_input_3.csv",1) == 0)

print("day 1 input with 1 lookback", generic_day1("day1_input.csv", 1))

assert(generic_day1("test_input_1.csv", 3) == 2)
assert(generic_day1("test_input_2.csv", 3) == 0)
assert(generic_day1("test_input_3.csv", 3) == 0)

print("day 1 input with 3 lookback", generic_day1("day1_input.csv", 3))
