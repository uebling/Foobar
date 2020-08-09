import decimal

def solution(s):
    '''Completely new attempt, after reading about Beatty sequences. There is a 
    way to calculate a recursion formula for the sum. Lots of work on paper, very short code...'''
    decimal.getcontext().prec = 101
    
    n = int(s)
    sqrt2 = decimal.Decimal(2).sqrt()

    def beatty(nr):
        if nr < 1:
            return 0
        if nr == 1:
            return 1
        ns = int(nr*(sqrt2-1)) #that identity took me the longest to find
        L = (nr+ns)*(nr+ns+1)/2 - ns*(ns+1)
        return L - beatty(ns)
    res = beatty(n)
    res = str(res)
    
    return res

print("input '77', result: {}, expected 4208".format(solution('77')))
print("input '5', result: {}, expected 19".format(solution('5')))
print("input '348548384', result: {}, expected 85903557513082823".format(solution('348548384')))
print(solution('99999999999999999999999999999999999999999999999999999999999999999999999999'))
