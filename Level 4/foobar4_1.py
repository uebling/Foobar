def solution(dimensions, your_position, guard_position, distance):
    #Looks like this time the library works
    from fractions import gcd
    #Transform coordinates from the cell with the player/guard into its mirror cells
    def get_coords(cell,in_cell):
        #The mirroring depends on the parity of the cell numbers
        #Be careful not to mutate the input
        x = in_cell[0]
        y = in_cell[1]
        if cell[0] % 2 == 1:
            x = dimensions[0] - x
        if cell[1] % 2 == 1:
            y = dimensions[1] - y
        return (x+cell[0]*dimensions[0],y+cell[1]*dimensions[1])
    
    #function to see if a position is in range
    def in_range(target):
        return (target[0]-your_position[0])**2 + (target[1]-your_position[1])**2 <= distance **2

    #find which cell a lattice point is in
    def in_cell(point):
        if point[0] % dimensions[0] == 0 or point[1] % dimensions[1] == 0:
            return "wall" #Point is actually at a wall and therefore safe
        else:
            return (point[0]//dimensions[0],point[1]//dimensions[1])
    
    #Is the path clear?        
    def is_safe(target):
        #First I want the firing vector
        shot = (target[0]-your_position[0],target[1]-your_position[1])
        #there are g lattice positions between shooter and target, including the target
        g = abs(gcd(shot[0],shot[1]))
        if g == 1:
            return True #Direct hit
        else:
            shot = (shot[0]//g,shot[1]//g)
            for i in range(1,g):
                #Get the mirror cell where the intermediate position of the beam is
                beam = (your_position[0]+i*shot[0],your_position[1]+i*shot[1])
                cell = in_cell(beam)
                if cell == "wall":
                    continue
                else:
                    #I consider it "unsafe", if a mirror image of the player OR the guard 
                    #is in the way, the latter to avoid overcounting
                    if get_coords(cell,tuple(your_position)) == beam or get_coords(cell,tuple(guard_position)) == beam:
                        return False
                    else:
                        continue
        return True
    
    #Now the main program
    #first check for the case, where the room is too small
    #smaller rooms than 3x2 do not fit player and guard
    #Use this to see if the library works this time
    if dimensions[0]*dimensions[1] < 6:
        return 0
    if (guard_position[0]-your_position[0])**2 + (guard_position[1]-your_position[1])**2 > distance**2:
        return 0
    #Looks like that was in test case 5
    
    nmax = (distance//dimensions[0],distance//dimensions[1])
    
    c = 0
    for a in range(-nmax[0],nmax[0]+1):
        for b in range(-nmax[1],nmax[1]+1):
            target = get_coords((a,b),tuple(guard_position))
            if in_range(target) and is_safe(target):
                c += 1
    
    return c
    

print(solution([3,2], [1,1], [2,1], 4)) #7
print(solution([300,275], [150,150], [185,100], 500)) # 9