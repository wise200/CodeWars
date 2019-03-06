

def ser(start, length):
	i = start
	string = str(start)
	while len(string) <= length:
		i += 1
		string += str(i)
	return 0 if i == start else i-1
	
def read():
	return [int(x) for x in input().split()]
	
list = read()
while list[0] != 0 or list[1] != 0:
	print(str(list[0]) + ' ' + str(list[1]) + ' ' + str(ser(list[0],list[1])))
	list = read()