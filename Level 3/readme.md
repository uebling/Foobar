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
### Bomb, baby
You have 2 populations of self-replicating bombs with a given reproduction cycle. Calculate the lowest number of cycles to reach a target population from an initial population. I forgot the exact names of the bomb types, but they started with M and F, appropriate for being able to reproduce. I use these letters to denote the number of each. They can reproduce according to two rules. \
A: (M,F) -> (M,M+F)\
B: (M,F) -> (M+F,F)\
The goal is to find the number of reproduction cycles (A,B operations) needed to get from (M,F) = (1,1) to any target number where M,F can be up to 10^50! Also some target numbers might be unreachable, in that case, the solution should return the string "Impossible". Also important **The input and output are strings** presumably to make using huge numbers easier.

This was a really nice challenge and rather easy to figure out. I quickly realized that one can represent the entire process as a binary tree with A,B operations splitting it up, and that it would be much simpler to find the way back to (1,1) from the target numbers rather than trying to use some search algorith to find the target from the start. The operations A,B can be represented by 2x2 matrices which are so simple that inverting them or calculating their n-th power is trivial. What is less trivial is using latex in markdown on Github, so I'll not write is down as matrices:\
A^-1: (M,F) -> (M,F-M)\
B^-1: (M,F) -> (M-F,F)\
A^-n: (M,F) -> (M,F-nM)\
B^-n: (M,F) -> (M-nF,F)\
This is because only one of the numbers changes each time.

To get to the start from any point in the tree, one just has to reach the edge, which is where either M or F is equal to 1. The rule is simple: if F > M use A^-1, if M>F use B^1, until one of them is 1. Since we know how many inverse operations we need until M-F filps sign, we just do one big step using the powers of A^-1 and B^-1. This makes is fast enough to handle even huge numbers for M,F.

The impossible sitations are where M % F = 0 and none of them is 1. This will eventually lead to a situation where M = F, which cannot be reached from the starting point.
