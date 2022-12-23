file = open('day21.txt','r')
lines = file.read().splitlines() 


def parse(lines):
	d = {}
	for line in lines:
		split = line.split(": ")
		key = split[0]
		if len(split[1]) < 6:
			op = ""
			leaves = [int(split[1])]
		elif split[1][5] == "-":
			op = "-"
			split_1 = split[1].split(" - ")
			leaves = [split_1[0], split_1[1]]
		elif split[1][5] == "+":
			op = "+"
			split_1 = split[1].split(" + ")
			leaves = [split_1[0], split_1[1]]
		elif split[1][5] == "*":
			op = "*"
			split_1 = split[1].split(" * ")
			leaves = [split_1[0], split_1[1]]
		elif split[1][5] == "/":
			split_1 = split[1].split(" / ")
			op = "/"
			leaves = [split_1[0], split_1[1]]
		else:
			print("somtehitng went wrong")
		d[key] = (op, leaves)
	return d




def part1(d):
	

	def traverse(node):

		op, leaves = d[node]
		if op == "":
			return leaves[0]
		else:
			leaf_1 = traverse(leaves[0])
			leaf_2 = traverse(leaves[1])

			if op == "+":
				return leaf_1 + leaf_2
			elif op == "-":
				return leaf_1 - leaf_2
			elif op == "*":
				return leaf_1 * leaf_2
			elif op == "/":
				return leaf_1 / leaf_2
			else:
				print( "got a bad op")
	
	return traverse("root")

def part2(d):
	
	result = {}
	human = {}
	def traverse(node):

		op, leaves = d[node]
		if op == "":
			if node == "humn":
				human[node] = True
				return leaves[0],True

			human[node] = False
			result[node] = leaves[0]
			return leaves[0], False
		else:
			leaf_1, h_1 = traverse(leaves[0])
			leaf_2, h_2 = traverse(leaves[1])
			
			res = 0
			if op == "+":
				res = leaf_1 + leaf_2
			elif op == "-":
				res = leaf_1 - leaf_2
			elif op == "*":
				res = leaf_1 * leaf_2
			elif op == "/":
				res = leaf_1 / leaf_2
			else:
				print( "got a bad op")


			result[node] = res
			if h_1 == True or h_2 == True:
				human[node] = True

				return res, True
			human[node] = False
			return res, False
	
	def fix(node, goal):
		op, leaves = d[node]
		
		if node == "humn":
			print("readed human", goal)
			return goal
		if op == "":
			print("something broke")
		leaf_1, leaf_2 = leaves[0], leaves[1]

		if op == "+":
			if human[leaf_1]:
				res = fix(leaf_1, goal - result[leaf_2])
			else:
				res = fix(leaf_2, goal - result[leaf_1])
		elif op == "-":
			if human[leaf_1]:
				res = fix(leaf_1, goal + result[leaf_2])
			else:
				res = fix(leaf_2, result[leaf_1] - goal )
		elif op == "*":
			if human[leaf_1]:
				res = fix(leaf_1, goal / result[leaf_2])
			else:
				res = fix(leaf_2, goal / result[leaf_1])
		elif op == "/":
			if human[leaf_1]:
				res = fix(leaf_1, goal * result[leaf_2])
			else:
				res = fix(leaf_2, result[leaf_1] / goal )
		return res
	
	op, leaves = d["root"]
	sub_tree_1, h_1 = traverse(leaves[0])
	sub_tree_2, h_2  = traverse(leaves[1])
	print(sub_tree_1, h_1 )
	print(sub_tree_2, h_2 )
	if h_1:
		return fix(leaves[0], sub_tree_2)
	return fix(leaves[1], sub_tree_1)







d = parse(lines)
print(part2(d))
