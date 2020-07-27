def solution(src, dest):
    
    #Mini-function to get x-y-coordinates in case I need it
    def coords(field):
        return (field // 8,field % 8)
        
    #And its inverse
    def field(coords):
        return coords[0]*8 + coords[1] % 8
        
    #Make a list of all targets accessible from field n
    def all_targets(n):
        l = []
        #All possible jumps in coordinates
        l2 = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        for i,j in l2:
            #Don't jump off the field! Convert back to field numbers
            if (-1 < coords(n)[0]+i < 8) and (-1 < coords(n)[1]+j < 8):
                l.append(field((coords(n)[0]+i,coords(n)[1]+j)))
        return l
        
    #Make a list of distances to starting point:
    #999 is default value, will never be reached while calculating distances
    distances = [999 for n in range(64)]
    #Distance from starting point to itself is 0
    distances[src] = 0
    dist = 0
    
    #Now we calculate the real distances (number of hops), until no more 999 are in the list
    #Get all fields with distance 1, then loop over them to get all with dist 2, ...
    while 999 in distances:
        for n in range(64):
            if distances[n] == dist:
                for t in all_targets(n):
                    if distances[t] == 999:
                        distances[t] = dist+1
        dist += 1
        
    #Now we have all distances from the starting point in a list, just return the one for the target field
    return distances[dest]