# Level 2
Level 2 has 2 problems, each with a time limit of 72 hours (if I remember correctly).

## Problem 1
Write a function that takes in a list of single digits and outputs the **largest possible number** that can be created with these digits and that is **divisible by 3**. This can be solved in 3 steps:
0. Sort the list to make things simpler.
1. If the sum of all digits is divisible by 3, reverse-sort them, glue them together (by turning them into strings), output the number.
2. If not, we must decide which digit to drop. We want to drop as few numbers as possible, and the smallest ones first. So we start from the beginning where the smallest number is and check if removing it makes the remaining sum divisible by 3. If yes, remove it and finish.
3. If 2 does not remove anything, remove the smallest number that itself is not a multiple of 3


## Problem 2
Get the shortest number of jumps on an 8x8 chessboard for a **knight** to reach field **dest** from field **src**. The 2 fields are given as single integers from 0 to 63, not as x-y coordinates.
I first create three helper functions:
1. One to get the (x,y) coordinates from the number, because I prefer to think in terms of them rather than treating the board as a 1d list.
2. Another one to transform it back. 
3. A function that returns a list of all reachable target fields from an input field. I have to take into account the boundaries of the field of course.

Then I don't just try to calculate the distance to the target field, but to all fields. Because the field is quite small, that should not be a problem. It is rather simple now create an array with the same size as the board:
1. The starting field gets 0, because that is its distance from itself.
2. All other fields get a very large number like 999
3. Loop over all possible target fields, assign them distance 1
4. Loop over all fields with distance 1 and assign their targets fields distance 2, unless there is already a shorter distance assigned
5. Then loop over all fields with distance 2 etc... until no more 999s are there. Of course one could stop once the target field is reached, but in level 2 apparently runtim is not an issue yet.
Then output the distance, done!
