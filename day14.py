import csv
from typing import Dict


def read_file(file_name: str) -> (str, Dict[str, str]):
	with open(file_name, newline='\n') as f:
		reader = csv.reader(f)
		#get the starting pattern
		input_str = next(reader)[0]
		#skip empty row
		next(reader)
		paths = {}
		for row in reader:
			row_elements=row[0].split(" -> ")
			paths[row_elements[0]] = row_elements[1]
	return input_str, paths
			
def part_1(inp: str, paths: Dict) -> int:
	
	for i in range(10):
		inp = build_string_one_day(inp, paths)
		low, high = count_lowest_and_heighest_occurence(inp)
	
	lowest_char, highest_char = count_lowest_and_heighest_occurence(inp)

	return highest_char - lowest_char

			
def part_2(inp: str, paths: Dict) -> int:
	#calculate which sections become which other sections
	path_changes = {}
	for input_s, output_s in paths.items():
		path_changes[input_s] = [input_s[0] + output_s,output_s + input_s[1]]
	#count the occurence of each section in the  beginning
	section_count = {}
	for i in range(1, len(inp)):
		section = inp[i-1:i+1]
		section_c = section_count.get(section, 0)
		section_count[section] = section_c + 1

	for i in range(40):
		section_count = day_forward_dictionary(section_count, path_changes)

	lowest_char, highest_char = count_stuff_dict(section_count)

	return highest_char - lowest_char


def day_forward_dictionary(section_count: Dict[str, int], path_changes: Dict[str, str]) -> Dict[str, int]:
	new_section_count = {}
	for section, c in section_count.items():
		new_sections = path_changes.get(section, [])
		for new_section in new_sections:
			n = new_section_count.get(new_section, 0)
			new_section_count[new_section] = c + n


	return new_section_count


def count_stuff_dict(section_count: Dict, last_char: str) -> (int, int):
	char_count = {}
	for k,v in section_count.items():
		first_char = k[0]
		first_count = char_count.get(first_char, 0)
		char_count[first_char] = first_count + v

	lowest, highest = char_count['N'], 0
	highest_char = max(char_count, key=char_count.get)
	lowest_char = min(char_count, key=char_count.get)

	return char_count[lowest_char], char_count[highest_char]


def count_lowest_and_heighest_occurence(inp: str) -> (int, int):
	set_of_char = set(inp)
	lowest_count, highest_count = inp.count(inp[0]), 0
	low_char, high_char = "", ""
	for c in set_of_char:
		char_count = inp.count(c)
		if lowest_count > char_count:
			lowest_count = char_count
			low_char = c
		if highest_count < char_count:
			highest_char = char_count
			high_char = c 
	return lowest_count, highest_char

def build_string_one_day(inp: str, paths: Dict[str, str]):
	#initialize with initial char which never changes
	new_str = inp[0]
	sections_counts = {}
	for i in range(1, len(inp)):
		section = inp[i-1:i+1]
		section_count = sections_counts.get(section, 0)
		sections_counts[section] = section_count + 1
		new_item = paths.get(section, "")
		#add new char
		new_str += new_item
		#add next char
		new_str += inp[i]
	return new_str

input_str, paths = read_file("day14_input.csv")
res = part_1(input_str, paths)
print("part 1", res)
input_str, paths = read_file("day14_input.csv")

res = part_2(input_str, paths)
print(res)
