import csv

def part_1(file_input, length) -> int:
	fishies = file_input.copy()
	for i in range(length):
		fishies = grow_fish(fishies)
	return len(fishies)

def part_2(file_input, length):
	return  grow_fish_without_memory(file_input, length)[length-1][1]

def grow_fish_without_memory(fishs, length):
	cycle = 0
	#meta_data will be new fish, regenerated fish and total fish on that day
	fish_meta_data = [[] for i in range(length)]
	for i in range(9):
		new_fish= 0
		for fish in fishs:
			if fish == 0:
				new_fish += 1
		fishs = grow_fish(fishs)
		fish_meta_data[i] = [new_fish, len(fishs)]

	
	for i in range(9, length):

		regenerated_fish = fish_meta_data[i-7][0] + fish_meta_data[i-9][0]
		fish_meta_data[i] = [regenerated_fish, fish_meta_data[i-1][1] + fish_meta_data[i-7][0] + fish_meta_data[i-9][0]]
	
	return fish_meta_data

def grow_fish(file_input):
	for fish_index in range(len(file_input)):
		if file_input[fish_index] > 0:
			file_input[fish_index] -= 1
		elif file_input[fish_index] == 0:
			file_input[fish_index] = 6
			file_input.append(8)
	return file_input


def read_file(file_name):
	with open(file_name, newline='\n') as f:
		reader = csv.reader(f)
		row = next(reader)
		return [int(x) for x in row]

	return decreasing_counter

assert(part_1([0,1],2) == 4)	

test_input = [0,1,2,3,4,5,6]
assert(part_1(test_input, 20) == part_2(test_input, 20))

file = read_file("day6_input.csv")
part_1_answer = part_1(file, 80)
print("part 1 answer is", part_1_answer)

file_2 = read_file("day6_input.csv")
fishies = part_2(file_2, 256)
print("part 2 answer", fishies)






































