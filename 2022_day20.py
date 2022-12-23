
file = open('day20.txt','r')
lines = file.read().splitlines() 

def perform_op(input_l, seen, i):
	op, original_op = input_l[i], input_l[i]
	while op <= -5000:
		op += 4999

	if op == 0:
		seen[i] = 1
	elif op > 0:
		if op >= 5000:
			plus = op // 5000
			op = op % 5000
			op += plus

		if op + i >= len(input_l) :
			#wrap around
			end_elements = len(input_l) - i -1
			begining_index = op - end_elements
			el = input_l.pop(i)
			seen.pop(i)

			input_l.insert(begining_index, el)
			seen.insert(begining_index, 1)
			
		else:
			el = input_l.pop(i)
			seen.pop(i)
			input_l.insert(op+i, el)
			seen.insert(op+i, 1)
			
	else:
		#negatives

		if op + i <= 0:
			#wrap around
			begining_elements = i
			end_index = op + begining_elements
			el = input_l.pop(i)
			seen.pop(i)
			if end_index == 0:
				end_index = len(input_l)
				input_l.insert(end_index, el)
				seen.insert(end_index, 1)
			else:
				input_l.insert(end_index, el)
				seen.insert(end_index, 1)
			
		else:
			el = input_l.pop(i)
			seen.pop(i)
			input_l.insert(i+op, el)
			seen.insert(i+op, 1)
			
	return input_l, seen, i

import time
def perform_op_part2(input_l, i):
	op, original_op = input_l[i][1], input_l[i][1]
	# start = time.time()
	#totally stole this from someone bc i was lazy
	insert_key = (i + input_l[i][1]) % (len(input_l)-1)
	if op == 0:
		print(i)
	elif op > 0:

		# sub_time = time.time()
		# print("sub", sub_time- start )
		if op + i >= len(input_l) :
			#wrap around
			el = input_l.pop(i)
			# pop_time = time.time()

			input_l.insert(insert_key, el)
			insert_time = time.time()
			# print("insert", insert_time-pop_time )
		else:
			el = input_l.pop(i)
			# pop_time = time.time()
			# print("pop", pop_time- sub_time )
			input_l.insert(insert_key, el)
			insert_time = time.time()
			# print("insert", insert_time-pop_time )
	else:
		#negatives
		# sub_time = time.time()
		if op + i <= 0:
			#wrap around
			begining_elements = i
			end_index = op + begining_elements
			el = input_l.pop(i)

			# pop_time = time.time()
			# print("pop", pop_time- sub_time )

			if end_index == 0:
				end_index = len(input_l)
				input_l.insert(insert_key, el)
			else:
				input_l.insert(insert_key, el)
				insert_time = time.time()
			# print("insert", insert_time-pop_time )
			
		else:
			el = input_l.pop(i)

			# pop_time = time.time()
			# print("pop", pop_time- sub_time )
			input_l.insert(insert_key, el)
			insert_time = time.time()
			# print("insert", insert_time-pop_time )
	return input_l, i

def part1(lines):
	input_l = []
	for line in lines:
		input_l.append(int(line))
	operations = input_l.copy()
	seen = [0 for x in input_l]
	i = 0
	calls =0
	while sum(seen) != len(input_l):
	
		if seen[i] == 1:
			i += 1
		else:
			calls += 1
			input_l, seen, i= perform_op(input_l, seen, i)

	return input_l

def part2(lines):
	input_l = []
	i = 0
	for line in lines:
		input_l.append((i,int(line)*811589153))

		i += 1
	mix_count = 10
	for _ in range(mix_count):
		count = 0
		for i in range(len(input_l)):
			for j in range(len(input_l)):
				if input_l[j][0] == i:

					input_l, i= perform_op_part2(input_l, j)

					break

	
	return [x for _,x in input_l]
#tests
#move positive forward
input_test = [2,1,-3,3,-2,0,4]
seen = [0,1,0,0,0,0,0]
inp,s,i = perform_op(input_test, seen, 0)
assert(inp == [1, -3, 2, 3, -2, 0, 4])
assert(seen == [1,0,1,0,0,0,0])
# assert(i == 1)
#positive wrap around
input_test = [1, 2, -3, 0, 3, 4, -2]
seen = [1,1,1,1,1,0,1]
inp,s,i = perform_op(input_test, seen, 5)
assert(inp == [1, 2, -3, 4, 0, 3, -2])
assert(seen == [1,1,1,1,1,1,1])
# assert(i == 6)
#negative wrap around
input_test = [1, -3, 2, 3, -2, 0, 4]
seen = [1,0,1,0,0,0,0]
inp,s,i = perform_op(input_test, seen, 1)
assert(inp == [1, 2, 3, -2, -3, 0, 4])
assert(seen == [1,1,0,0,1,0,0])
# assert(i == 2)
#negative move around
input_test = [1, 2, 3, -2, -3, 0, 4]
seen = [1,1,1,1,0,1,0]
inp,s,i = perform_op(input_test, seen, 4)
assert(inp == [1, -3,2, 3, -2, 0, 4])
assert(seen == [1,1,1,1,1,1,0])
# assert(i == 5)
#test_input
file_1 = open('day20_test.txt','r')
lines_1 = file_1.read().splitlines() 
res = part1(lines_1)
assert(res == [1, 2, -3, 4, 0, 3, -2])

res = part1(lines)
zero = res.index(0)
print(zero,zero+1000, len(res))
print(res[zero+1000] + res[zero + 2000] + res[zero + 3000-len(res)])

res_2 = part2(lines)



zero = res_2.index(0)
print(zero,zero+1000, len(res_2))
print(res_2[zero+1000] + res_2[zero + 2000] + res_2[zero + 3000-len(res_2)])

