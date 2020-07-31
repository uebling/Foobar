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
