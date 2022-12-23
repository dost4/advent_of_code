file = open('day22.txt','r')
lines = file.read().splitlines() 


def parse(lines):
	finished = False
	graph = []
	for line in lines:
		if finished:
			instructions = line
		else:
			if line == "":
				finished = True
			else:
				graph.append(list(line))
	return graph, instructions

def parse_instructions(instruction):
	inst = []
	current_num = ""
	for i in range(len(instruction)):
		if ord(instruction[i]) < 58:
			current_num += instruction[i]
		else:
			inst.append((int(current_num),instruction[i]))
			current_num = ""
	if current_num != "":
		inst.append((int(current_num),""))
	return inst

def part1(graph, inst):
	instructions = parse_instructions(inst)
	x, y = 0, 0
	for i in range(len(graph[0])):
		if graph[0][i] == ".":
			x = i
			break
	heading = 0
	counter = 0
	c = 0
	for move, dire in instructions:
		c += 1
		if c == 2002:
			return x,y,heading
		if counter < 15:

		if heading == 0:
			for i in range(move):
				if x + 1 >= len(graph[y]) or graph[y][x+1] == " ":
					move_x = 0 
					while graph[y ][move_x] == " ":
						move_x += 1
					if graph[y][move_x] == "#":
						break
					else:
						x = move_x
						continue

				elif graph[y][x+1] == "#":
					break
				else:
					x += 1
		elif heading == 1:
			for i in range(move):
				if y+1 >= len(graph) or x >= len(graph[y+1]) or graph[y+1][x] == " ":
					move_y = 0 
					
					while graph[move_y ][x] == " ":
						move_y += 1
					if graph[move_y][x] == "#":
						break
					else:
						y = move_y
						continue

				elif graph[y+1][x] == "#":
					break
				else:
					y += 1
		elif heading == 2:
			for i in range(move):
				if x - 1 < 0 or graph[y][x - 1] == " ":
					move_x = len(graph[y])-1
					
					while graph[y ][move_x] == " ":
						move_x -= 1

					if graph[y][move_x] == "#":
						break
					else:
						x = move_x
						continue

				if graph[y][x-1] == "#":
					break
				x -= 1
		elif heading == 3:
			for i in range(move):
				if y - 1 < 0 or graph[y-1][x] == " ":
					
					move_y = len(graph) -1
					while len(graph[move_y]) < x:
						move_y -= 1

					while graph[move_y][x] == " ":
						move_y -= 1
					if graph[move_y][x] == "#":
						break
					else:
						y = move_y
						continue

				elif graph[y-1][x] == "#":
					break
				else:
					y -= 1
		else:
			print("issue with heading")

		if dire == "R":
			heading += 1
			if heading == 4:
				heading = 0
		elif dire == "L":
			heading -= 1
			if heading == -1:
				heading = 3
		counter += 1

	return x,y,heading


g, i = parse(lines)
x,y,d = part1(g,i)

print(x,y,d)
print((y+1)*1000+4*(x+1) + d)