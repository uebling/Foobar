def solution(area):
    import math
    panel_list = []
    
    #In case I need the area later for some nice output
    num = area
    while num >= 1:
        #This finds the largest possible integer square that fits in area
  #      square = math.isqrt(num)**2
        square = int(num**0.5)**2
        #then I subtract it, and put it in a list
        #repeat until 1 is reached, which is the smallest square
        num = num - square
        panel_list.append(square)

    return panel_list

#Below are some test cases
print(str(solution(12)))
print(solution(19))
print(solution(15324))
