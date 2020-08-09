def solution(x,y):

	m = int(x)
	f = int(y)
	c = 0

	while m != 1 and f != 1:
	#	print(m,f)
		if m > f:
			if m % f == 0:
				return "impossible"
			n = (m - f)//f+1
			m = m - n*f
			c += n
		elif m < f:
			if f % m == 0:
				return "impossible"
			n = (f - m)//m+1
			f = f - n*m
			c += n
		else:
			return "impossible"
	#print(m,f)
	return str(c + max(m,f) - 1)

print(solution('2','1')) #1
print(solution('4','7')) #4
print(solution('2','4')) #imp
print(solution('1'+'0'*49,'9'*50)) #To check how long it takes for very large numbers
