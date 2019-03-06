digits = {x for x in '0123456879'}


def valid(string):
	num = ''
	for c in string:
		if c in digits:
			num += c
	if len(num) != 10 or num[0] == '1' or num[0] == '0' or num[3] == '1' or num[3] == '0':
		return 'INVALID'
	if num[1] == '9' or (num[4] == num[5] == '1'):
		return 'INVALID'
	return 'VALID'


cases = int(input())
for x in range(cases):
	num = input()
	print(num + ' ' + valid(num))