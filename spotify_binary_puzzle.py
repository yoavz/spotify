def int_to_binary(integer):
	bin_string = ''
	i = 0
	while integer > 2**i :
		i += 1
	pos = i - 1
	while pos >= 0:
		if integer >= 2**pos:
			bin_string += '1'
			integer -= 2**pos
		else:
			bin_string += '0'
		pos -= 1
	return bin_string


def binary_to_int(bin_string):
	integer = 0
	for i in range(1, len(bin_string)+1):
		if bin_string[-i] == '1':
			integer += 2**(i-1)
	return integer


a = int(raw_input('Input: '))
bin_string = int_to_binary(a)
reverse = bin_string[::-1]
integer = str(binary_to_int(reverse))
print 'Output: ' + integer

