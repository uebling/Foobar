# Level 3
Level 3 has 3 problems, each with a time limit of 4 days. Here I wrote down the name of each challenge, makes it easier to find other solutions on the internet.

## Problem 1
### queue-to-do
There are workers standing in a queue of length L, each of these workers has a number, and they are ordered consecutively. In other words, if the first has number s, the second has s+1, etc. The securiry guys record each number and calculate the XOR checksum. Then they let all workers pass until the next queue assembles. There, they just check the first L-1 workers, and repeat the progress until they check no more numbers. They calculate the checksum for all workers they check and the challenge is to recreate the number with the parameters L,s as input.

This was the first problem that took me some time to figure out. First I had no idea what "XOR-checksum" means, but this can be easily found out on wikipedia. A ^ B means representing both numbers A,B as binaries, then performing an XOR operation on each bit. Also, before programming this all by hand I found out that it is built into Python by default, using the ^ symbol. Strange that something obscure like this requires no library, while elementary functions like sqrt and cos do, but Python is weird. After realizing this, getting all the numbers for the sum was easy, but some test cases just wouldn't pass. I realized that there is a well-hidden hint in the description that I have to be **faster** than the security guards. So my results were correct but not fast enough, apparently this ^ operation is not the most efficient. So, the key here is to use the rules and a periodicity of the XOR operation:

1. What we have to compute here are sums of the type 5^6^7^8^9^.., i.e. over consecutive numbers.
2. Properties of XOR are: A^A = 0, 0^A=A, A^B=B^A, A^(B^C) = (A^B)^C
3. This means that m^m+1^...^n = (0^1^...^m-1)^(0^1^...^m-1)^(m^m+1^...^n) = (0^1^...^m-1)^(0^1^...^n), so every partial sum we need can be expressed in terms of sums starting with 0.
4. The sum 0^1^...^n is periodic, its value is either n, 1, n+1 or 0.
5. With this, we can calculate the result with much fewer explicit ^ operations, and pass all test cases.

## Problem 2
### Find the access codes
Get the number of all possible lucky triples out of a given input list l. A lucky triple is a list of 3 integers a,b,c where a=<b=<c and b divides c and a divides b. Something like (3,6,24). This problem again has a simple solution (for each a and b, loop over all c and count), but it fails some of the test cases, so likely there is a speed issue again. even though this time I could not find a hint in the description about speed. But the list can be up to 2000 elements long which means having more than a billion triples to check. The solution here is to count lucky pairs first and make a list of them by counting for each list element how many lucky pairs it can form with the remaining numbers to the right of it (basically counting for each b how many fitting c-values there are). Then another loop goes over all a and just checks how many lucky pairs fit to it. This reduces the computational cost from N^3 to N^2, where N is the length of the list, enough to pass all test cases. There are probably even better ways to do this.

## Problem 3
You have 2 populations of self-replicating bombs with a given reproduction cycle. Calculate the lowest number of cycles to reach a target population from an initial population.
