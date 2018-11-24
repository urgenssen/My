
def get_summ(one, two, delimiter=' & '):
	x = str(one) + str(delimiter) + str(two)
	return x.upper()


sum_string = get_summ('Learn', 'python')
print (sum_string)
