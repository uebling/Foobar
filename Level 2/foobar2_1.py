def solution(l):
    #Sorting the list might help
    l.sort()
    
    #Check if divisible by 3, if not remove as few/small numbers from list as necessary
    while sum(l) % 3 != 0:
        #Sorting means this starts from the smallest digit
        for digit in l:
            if (sum(l) - digit) % 3 == 0:
                l.remove(digit)
                break #Remove only once!
        #If nothing was removed, try removing the smallest number not divisible by 3
        if sum(l) % 3 != 0:
            for digit in l:
                if digit % 3 !=0:
                    l.remove(digit)
                    break
        if sum(l) == 0:
            break
    
    #Now we turn the list into a number
    #First check if it is empty
    if len(l) == 0:
        return 0
    else:
    #Just sort the list on reverse and put the numbers together
        l.sort(reverse=True)
    #I turn them into strings so I can concatenate, then back to int
        result_str = str()
        for digit in l:
            result_str = result_str + str(digit)
        return int(result_str)


print(solution([3,1,4,2]))
print(solution([3,1,4,2,2]))
print(solution([3,1,4,1,5,9]))
print(solution([3,7,7]))
print(solution([7,7]))
