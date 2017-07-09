stack = []
buff = []

examp = "4+8*2*4^7*6^1-1/2"
oper = "+-*/%^"
oper_priority = {
	0: ['+', '-'],
	1: ['*', '/', '%'],
	2: ['^']
	}

def read_str(my_str):
	i = 0
	while i < len(my_str):
		if my_str[i].isdigit():
			new_num, i = make_num(my_str, i)
			stack.append(new_num)
		elif my_str[i] in oper:
			check_buff(my_str[i])
			i += 1
	
	while len(buff):
		stack.append(buff.pop()[1])

	print(stack)
	print(buff)

def make_num(my_str, str_ind):
	raw_ind = str_ind
	isDig = False

	while not isDig and str_ind < len(my_str):
		isDig = True
		if my_str[str_ind].isdigit():
			str_ind += 1
			isDig = False
		elif my_str[str_ind] is '.':
			str_ind += 1
			isDig = False

	if '.' in my_str[raw_ind: str_ind + 1]:
		return float(my_str[raw_ind: str_ind]), str_ind
	else:
		return int(my_str[raw_ind: str_ind]), str_ind

def oper_search(curr_oper):
	for i in oper_priority.keys():
		if curr_oper in oper_priority[i]:
			return i, curr_oper
	return False, 0

def check_buff(read_oper):
	if len(buff) == 0:
		buff.append(oper_search(read_oper))
		return None

	read_prior, oper = oper_search(read_oper)
	print(read_prior, oper)
	buff_prior, buff_oper = buff[len(buff) - 1]
	print(buff_prior, buff_oper)
	print(buff)
	while read_prior <= buff_prior and len(buff) > 0:
		stack.append(buff[len(buff) - 1][1])
		del buff[len(buff) - 1]
		if len(buff) > 0:
			buff_prior = buff[len(buff) - 1][0]

#	if read_prior <= buff_prior:
#		print("he")
#		stack.append(buff[len(buff) - 1][1])
#		del buff[len(buff) - 1]
#		buff.append((read_prior, read_oper))
	else:
		buff.append((read_prior, oper))


read_str(examp)
