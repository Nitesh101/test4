"""
def length_str(str1):
	tot = 0
	for i in str1:
		tot += 1
	return tot
print length_str('nitesh')
"""
def calucu(str1):
	d = {}
	for i in str1:
		keys=d.items()
		if i in keys:
			d[i] += 1
		else:
			d[i] = 1
	return d
print calucu('ggogle')
