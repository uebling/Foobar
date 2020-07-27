def solution(start, length):
    
    #XOR checksum from 0 to n
    #Faster than actually calculationg it, using periodicity
    def csum0(n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n+1
        elif n % 4 == 3:
            return 0
    #Checksum for consecutive number from first to last
    #Using x ^ x = 0 and 0 ^ x = x
    def csum(first,last):
        if first == 0:
            return csum0(last)
        else:
            return csum0(last) ^ csum0(first -1)

    cs = 0
    for n in range(length):
        #Get first worker of each queue + the lenght of the queue
        worker = start + n*length
        queue = length - n
        cs = cs ^ csum(worker,worker + queue - 1)
        
    return cs
