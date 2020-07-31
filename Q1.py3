"""
author: Guan Xin Miao
UPI: smia076
"""
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
	for i in range(2):

		for j in range(read_line_num):
			if i == 1:
				yield file_list[current_line]
			current_line += 1
		read_line_num = int(file_list[current_line])
		current_line += 1	
	"""
	while(True):
		if read_line_num == 0:
			#out_put_l.append(read_line_num)
			return out_put_l

		out_put_l = []

		#out_put_l.append(read_line_num)
		
		
		current_line += 1
"""
	


def main():
	txt_input = sys.stdin

	for i in read(txt_input):
		#if isinstance(i, int): pass
		print(i, end = "")

main()