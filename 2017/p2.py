
def read():
	return [float(x) for x in input().split()]


nums = read()
while nums[0] != 0 or nums[1] != 0 or nums[2] != 0:
	vt = nums[0] * nums[2]
	at2 = .5 * nums[1] * nums[2] ** 2
	print(vt + at2)
	nums = read()