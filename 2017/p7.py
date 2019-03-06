
def read():
	list = [int(x) for x in input().split()]
	list.pop(0)
	return list

list = read()
while len(list) > 0:
	list = sorted(list, reverse=True)[:3]
	print(list[0] * list[1] * list[2])
	list = read()
	
