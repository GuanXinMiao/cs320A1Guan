import sys
import string
def read(txt):
	file_list = []
	for line in txt:
		file_list.append(line)

	current_line = 0
	read_line_num = int(file_list[current_line])
	current_line += 1
	out_put_l = []

	while(True):
		if read_line_num == 0:
			out_put_l.append(read_line_num)
			return out_put_l

		out_put_l = []

		out_put_l.append(read_line_num)
		for i in range(read_line_num*2):
			out_put_l.append(file_list[current_line])
			current_line += 1
		read_line_num = int(file_list[current_line])
		current_line += 1

	


def main():
	txt_input = sys.stdin
	for i in read(txt_input):
		if isinstance(i, int): print(i)
		else: print(i, end = "")

main()