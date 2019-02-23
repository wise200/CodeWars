digits = set('0123456789'.split())

def valid(string):
	num = ''
	for c in string:
		if c in digits:
			num += c
	if len(num) != 10 or num[0] == '1' or num[0] == '0' or num[3] == '1' or num[3] == '0':
		return 'INVALID1'
	if num[1] == '9' or (num[4] == num[5] == '1'):
		return 'INVALID2'
	return 'VALID'


cases = int(input())
for x in range(cases):
	num = input()
	print(num + ' ' + valid(num))