
def unpack(coins, val):
	if coins % val == 0:
		return ((coins-val) // val, val)
	return (coins // val, coins % val)

def reduce(g, s, b):
	bronze = unpack(b, 5)
	b = bronze[1]
	s += bronze[0]
	silver = unpack(s, 10)
	s = silver[1]
	g += silver[0]
	print(str(g) + ' ' + str(s) + ' ' + str(b))
	
cases = int(input())
for x in range(cases):
	vals = [int(x) for x in input().split()]
	reduce(vals[0], vals[1], vals[2])
