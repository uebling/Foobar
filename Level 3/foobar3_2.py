
l1 = [1,1,1]
l2 = [1,2,3,4,5,6]
l3 = [324,4,1,2,324,22,1,23,44,11,67,45]

l4 = [n for n in range(1,2001)]
l5 = [1 for n in range(1,2001)]

lst = l1

def solution(l):

	nt = 0
	list_of_pairs = [0] * len(l)
	for i in range(len(l)-1):
		for j in range(i+1,len(l)):
			if l[j] % l[i] == 0:
				list_of_pairs[i] += 1

	for i in range(len(l)-1):
		for j in range(i+1,len(l)):
			if l[j] % l[i] == 0:
				nt += list_of_pairs[j]

	return nt
print(solution(l1),solution(l2),solution(l3),solution(l4))
