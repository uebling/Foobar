from itertools import combinations_with_replacement
from fractions import gcd
from math import factorial as fact

# def fact(n):
# 	'''in case math library doesn't work as usual in foobar'''
# 	if n == 0:
# 		return 1
# 	f = 1
# 	for i in range(1,n+1):
# 		f = f*i
# 	return f

def partitions(n,j=1):
	'''Generates all partitions of the integer n, meaning all lists of integers whose sums are equal to n'''
	yield [n]
	for i in range(j,n//2+1):
		if n-i >= i:
			for p in partitions(n-i,i):
				yield [i]+p

def number_of_permuations(lst,n):
	'''gets the number of permutations of the type corresponding to a partition. E.g. a partition [1,2] means
	"swap 2 numbers, leave one alone"'''
	res = 1
	for i in range(1,n+1):
		a = lst.count(i) #how many times is the number there?
		if a > 0:
			res = res * (i**a) * fact(a)
	return fact(n)//res

h = 12
w = 12
s = 2
total = 0
n = 0
for p in partitions(h):
	for q in partitions(w):
		nh = number_of_permuations(p,h)
		nw = number_of_permuations(q,w)
		exponent = 0
		for i in p:
			for j in q:
				exponent += gcd(i,j)

		total = total + nh*nw * s**exponent
		print(p,q)
total = total//fact(h)//fact(w)
print(total)
