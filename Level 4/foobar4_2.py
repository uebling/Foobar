from itertools import permutations
from copy import deepcopy

def solution(times, times_limit):
    n = len(times[0])
    #note to myself: times[a][b] is the time from a to b
    all_bunnies = [j for j in range(n-2)] #ID of all bunnies
    all_bunny_positions = [j+1 for j in range(n-2)] #Nodes where they sit
    
    def shorter(matrix):
        '''Makes a new matrix which finds a shorter path from a to b via c
        Lesson from challenge 4-1: in python a function can change a list even when it shouldn't. Make deep copy!'''
        newmat = deepcopy(matrix)
        for a in range(n):
            dist = deepcopy(matrix[a])
            for b in range(n):
                for c in range(n):
                    if b != c:
                        if dist[c] + matrix[c][b] < dist[b]:
                            dist[b] = dist[c] + matrix[c][b]

            newmat[a] = dist
        return newmat

    #If one application of "shorter" gives us a negative diagonal element, we have an endless loop
    for i in range(n):
        if shorter(times)[i][i] < 0:
            return all_bunnies
    
    '''Let's get the really shortest paths from a to b
    Repeat "shorter" until it doesn't change anymore this is finite because I eliminated endless loops above'''
    shortlist = deepcopy(times)
    while shortlist != shorter(shortlist):
        shortlist = shorter(shortlist)
    
    #The optimized graph now is much simpler, no node needs to be visited more than once 
    
    #Other special case: impossible to even reach the exit:
    if shortlist[0][n-1] > times_limit:
        return []
        
    def longest(tup,matrix,limit):
        '''Now that all paths visit each node only once, we construct the longest possible
        path of a permutation of the bunny positions that fits within the time limit'''
        t = 0
        res = [0]
        path = res + list(tup) + [n-1]
        i = 0
        for i in range(n-1):
            #time to exit via the next node in the path
            time_next_exit = t + matrix[path[i]][path[i+1]] + matrix[path[i+1]][n-1]
            if time_next_exit > limit:
                res.append(n-1)
                return res
            t = t + matrix[path[i]][path[i+1]]
            res.append(path[i+1])
        return tuple(res)

    def bunny_collector(path):
        '''Collects all bunnies along a path'''
        bunnies = set()
        for i in range(len(path)-1):
            if i > 0:
                bunnies.add(path[i]-1)
        return bunnies
    

    best_path = longest(tuple(all_bunny_positions),shortlist,times_limit)
    best_collection = bunny_collector(best_path)
    
    #All possible paths can be generated from all permuations over the bunnies
    #this is up to 5! not too much 
    for perm in permutations(all_bunny_positions):
        path = longest(perm,shortlist,times_limit)
        bunnies = bunny_collector(path)
        if len(bunnies) > len(best_collection)\
        or (len(bunnies) == len(best_collection) and sum(bunnies) < sum(best_collection)):
            best_path = path
            best_collection = bunnies
        if best_collection == set(all_bunnies):
            break
        
    return sorted(best_collection)
	
matrix1 = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
matrix2 = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
matrix3 = [[0, 2, 2, -1, 1], [9, 0, 2, -1, 1], [9, 3, 0, -1, 1], [9, 3, 2, 0, 1], [9, 3, 2, -1, 0]]
print(solution(matrix1,1))
print(solution(matrix2,3))
print(solution(matrix3,2))
