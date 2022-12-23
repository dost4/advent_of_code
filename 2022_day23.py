file = open('day23.txt','r')
lines = file.read().splitlines() 


def parse(lines):
	graph = []
	for line in lines:
		graph.append(list(line))
	return graph

def check_for_elves(graph, y,x):

	if x == 0 and y == 0:
		return graph[0][1] == "#" or graph[1][1] == "#" or graph[1][0] == "#"
	if x == len(graph[0])-1 and y == 0:
		return graph[0][x-1] == "#" or graph[1][x] == "#" or graph[1][x-1] == "#"
	if x == len(graph[0])-1 and y == len(graph)-1:
		return graph[y-1][x-1] == "#" or graph[y-1][x] == "#" or graph[y][x-1] == "#"
	if x == 0 and y == len(graph)-1:
		return graph[y-1][x] == "#" or graph[y-1][x+1] == "#" or graph[y][x+1] == "#"

	if x == 0:
		return graph[y+1][x] == "#" or graph[y-1][x] == "#" or graph[y][x+1] == "#" or graph[y-1][x+1] == "#"  or graph[y+1][x+1] == "#"
	if x == len(graph[0])-1:
		return graph[y+1][x] == "#" or graph[y-1][x] == "#" or graph[y][x-1] == "#" or graph[y-1][x-1] == "#"  or graph[y+1][x-1] == "#"
	if y == 0:
		print("checking", y, x)
		return graph[y+1][x-1] == "#" or graph[y+1][x] == "#" or graph[y+1][x+1] == "#" or graph[y][x+1] == "#" or graph[y][x-1] == "#" 
	if y == len(graph)-1:
		return graph[y-1][x-1] == "#" or graph[y-1][x] == "#"  or graph[y-1][x+1] == "#"  or graph[y][x-1] == "#" or graph[y][x+1] == "#"
	return graph[y-1][x-1] == "#" or graph[y-1][x] == "#" or graph[y-1][x+1] == "#" or graph[y+1][x-1] == "#" or graph[y+1][x] == "#" or graph[y+1][x+1] == "#" or graph[y][x-1] == "#" or graph[y][x+1] == "#"


def check_north(graph,y,x):
	if y == 0:
		return False

	if x == 0:
		return  graph[y-1][x] == "#" or graph[y-1][x+1] == "#"  or graph[y-1][x+1] == "#"
	if x == len(graph[0])-1:
		return  graph[y-1][x] == "#" or graph[y-1][x-1] == "#"  or graph[y-1][x-1] == "#"
	
	return graph[y-1][x-1] == "#" or graph[y-1][x] == "#" or graph[y-1][x+1] == "#"

def check_south(graph,y,x):
	if y == len(graph)-1:
		return False


	if x == 0:
		return  graph[y+1][x] == "#" or graph[y+1][x+1] == "#" 
	if x == len(graph[0])-1:
		return  graph[y+1][x] == "#" or graph[y+1][x-1] == "#"  
	return graph[y+1][x-1] == "#" or graph[y+1][x] == "#" or graph[y+1][x+1] == "#"

def check_east(graph,y,x):
	if x == len(graph[0])-1:
		return False

	if y == 0:
		return  graph[y][x+1] == "#" or graph[y+1][x+1] == "#"  
	if y == len(graph)-1:
		return  graph[y-1][x+1] == "#" or graph[y][x+1] == "#"  
	
	return graph[y+1][x+1] == "#" or graph[y-1][x+1] == "#" or graph[y][x+1] == "#"


def check_west(graph,y,x):
	if x == 0:
		return False

	if y == 0:
		return  graph[y][x-1] == "#" or graph[y+1][x-1] == "#"  
	if y == len(graph)-1:
		return  graph[y-1][x-1] == "#" or graph[y][x-1] == "#"  
	
	return graph[y+1][x-1] == "#" or graph[y-1][x-1] == "#" or graph[y][x-1] == "#"


def check_for_conflicts(graph, elf_position_map):
	for new_vals, old_list in elf_position_map.items():
		if len(old_list) > 1:
			for y,x in old_list:
				graph[y][x] = "#"
			graph[new_vals[0]][new_vals[1]] = "."
	return graph

def part1(graph):
	direction = ["N", "S", "W", "E"]
	moved = True
	days = 0
	#for _ in range(10):
	while moved:
		days += 1
		new_graph = [["."] *(len(graph[0]) + 2) for _ in range((len(graph) + 2))]
		elf_position_mapping = {}
		
		moved = False
		for y in range(len(graph)):
			for x in range(len(graph[0])):
				if graph[y][x] == ".":
					continue
				if not check_for_elves(graph,y,x):
					new_graph[y+1][x+1] = "#"
					continue
				moved = True

				placed = False
				for i in range(len(direction)):
					if placed: 
						break
					if direction[i] == "N" and not check_north(graph,y,x):
						
						new_graph[y][x+1] = "#"
						if (y,x+1) in elf_position_mapping:
							elf_position_mapping[(y,x+1)].append((y+1,x+1))
						else:
							elf_position_mapping[(y,x+1)] = [(y+1,x+1)]
						placed = True
					elif direction[i] == "S" and not check_south(graph,y,x):
						new_graph[y+2][x+1] = "#"
						if (y+2,x+1) in elf_position_mapping:
							elf_position_mapping[(y+2,x+1)].append((y+1,x+1))
						else:
							elf_position_mapping[(y+2,x+1)] = [(y+1,x+1)]
						placed = True
					elif direction[i] == "E" and not check_east(graph,y,x):
						new_graph[y+1][x+2] = "#"
						if (y+1,x+2) in elf_position_mapping:
							elf_position_mapping[(y+1,x+2)].append((y+1,x+1))
						else:
							elf_position_mapping[(y+1,x+2)] = [(y+1,x+1)]
						placed = True
					elif direction[i] == "W" and not check_west(graph,y,x):
						new_graph[y+1][x] = "#"
						if (y+1,x) in elf_position_mapping:
							elf_position_mapping[(y+1,x)].append((y+1,x+1))
						else:
							elf_position_mapping[(y+1,x)] = [(y+1,x+1)]
						placed = True
				

				if not placed:
					new_graph[y+1][x+1] = "#"


		graph = check_for_conflicts(new_graph, elf_position_mapping)

		d = direction.pop(0)
		direction.append(d)

		elves = 0
	return days
	# Uncomment for part 1
	# min_x, max_x, min_y, max_y = None, None, None, None
	# for y in range(len(graph)):
	# 	for x in range(len(graph[0])):
	# 		if graph[y][x] == "#":
	# 			elves += 1
	# 			if min_x is None or x < min_x:
	# 				min_x = x
	# 			if max_x is None or x > max_x:
	# 				max_x = x
	# 			if min_y is None or y < min_y:
	# 				min_y = y
	# 			if max_y is None or y > max_y:
	# 				max_y = y
	# print(min_x, max_x, min_y, max_y,elves )
	# return ((max_x - min_x+1) * (max_y - min_y+1) - elves)

graph = parse(lines)
print(part1(graph))






















				
