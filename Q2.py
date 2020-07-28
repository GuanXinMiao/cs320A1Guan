import sys

def read(txt):
	file_list = []
	for i in txt:
		file_list.append(i)

	return file_list

def convert(l):
	for i in l:
		for k in range(len(i)): i[k] = int(i[k])

def stable_marriage(problem_list):
	current_line = 0
	num_of_nodes = int(problem_list[current_line])
	current_line += 1
	instance_num = 1
	while(num_of_nodes != 0):
		blue_list, pink_list = [],[]

		for i in range(num_of_nodes):
			blue_list.append(problem_list[current_line].split())
			current_line += 1
		for i in range(num_of_nodes):
			pink_list.append(problem_list[current_line].split())
			current_line += 1
		convert(blue_list)
		convert(pink_list)
		
		pink_l = gale_shapley(blue_list, pink_list, num_of_nodes)
		print("Instance %d:"%instance_num)
		print_output(pink_l)
		num_of_nodes = int(problem_list[current_line])
		current_line += 1
		instance_num += 1

def print_output(pink_l):
	d = {}
	N = len(pink_l)
	for i in range(N): d[pink_l[i]] = i + 1

	for i in range(N):
		print("Blue node %d matched with pink node %d"%(i + 1, d[i+1]))

def pink_perfers(pink_l, pink_node, b, b1, N):

	for i in range(N):
		if(pink_l[pink_node][i] == b + 1): return True
		if(pink_l[pink_node][i] == b1): return False
	return False

def gale_shapley(blue, pink, N):
	freeNode = N
	blue_free, pink_match = [True for i in range (N)], [None for i in range(N)]
	#print(blue, pink)
	
	while(freeNode > 0):
		# pick the first free blue node
		b = 0
		while (b < N and not blue_free[b]): b += 1
		
		i = 0
		while (i < N and blue_free[b]):
			pink_node = blue[b][i]
			# if pink haven't match yet, these blue and pink matches
			if (pink_match[pink_node - 1] is None):
				pink_match[pink_node - 1] = b + 1
				blue_free[b] = False
				freeNode -= 1

			#if the pink matched find current enaggement
			else:
				b1 = pink_match[pink_node - 1]

				if(pink_perfers(pink, pink_node, b, b1, N)):
					pink_match[pink_node - 1] = b + 1
					blue_free[b] = False
					blue_free[b1 - 1] = True
			i += 1
	return pink_match
			
def main():
	txt_input = sys.stdin
	p_list = read(txt_input)
	stable_marriage(p_list)

main()