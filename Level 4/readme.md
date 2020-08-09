# Level 4
Level 4 has 2 problems, each with a time limit of 15 days. A big jump!

## Problem 1
### Gun to a guard fight
You and a bad guy are trapped in a room with mirror walls. Calculate how many ways there are to shoot him with a laser gun that has a maximum effective range. And don't shoot yourself.

This problem was surprisingly easy for level 4 because it played right into my strengths. The main challenge was to figure out what they mean by "dimensions" of the room and where the walls are relative to the lattice points. Then I stumbled over a Python peculiarity where I changed elements of a list without wanting to nor realizing that I did it.

The inputs here are:
1. The "dimensions" of the room (which is rectangular)
2. your_position: coordinates as a list of **integers**
3. guard_position: also coordinates as a list of integers
4. distance: effective range of the laser

Output:
Number of ways to shoot the guard

#### Layout of the room:
As with everything in Foobar, the room is represented in integers. Both positions are given as coordinates on a 2D lattice, while "dimensions" is the length and width of the rectangular room (the description talked about width and height and I got confused how a room which seemed to be 2dimensional with coordinates called x,y could have a height and wondered if maybe "dimensions" denoted the number of dimensions (level 4 is supposed to be very hard, I thought...)).

Good thing there was an example given of a 3x2 room which allowed me to deduce that the walls of the room contain the lattice points (they are not half-way in between them), so the 3x2 room is actually the smallest possible room with enough space for 2 people. It contains coordinates x = 0,1,2,3 and y = 0,1,2 and the only positions which are not part of a wall are (1,1) and (1,2). 

#### Make copies of the room
After figuring this out it is straightforward. Hitting the guard can be done directly or by reflecting off the walls, which is the same as shooting at a mirror image. So we take the room and make copies of it all around the initial room until we reach the range of the laser and get the position of all mirror images within range. As a condensed matter physicist with lots of experience with lattice models this approach is natural, but I get it that people with different backgrounds find this problem very challenging. In my terminology, the initial room is the unit cell and we make copies of it. The difference is that instead of periodic boundary conditions we have mirrors, so each copy has to be flipped accordingly.

Of course we only make copies of the cell which can be within range. It is ok here to just choose a rectangular pattern of cells, even if the corners are out of range, there is no need to calculate how many rectangles fit into a circle.

Then we calculate the coordinates of all mirror images in range of the laser and loop over them to count them. The last thing remaining is just to see if the path is clear. BOTH a mirror image of the player or a mirror image of the guard can be in the way, so we make sure these targets don't count. That's it. 



## Problem 2
### Running with bunnies
Reach the exit before the door closes and collect as many bunnies on the way as possible. Much more challenging for me compared to the previous one, because I never had anything to do with graph theory in my life. So I had to use Google and Wikipedia.

#### Layout
There are up to 7 positions (nodes) here. The starting point, the end point and up to 5 places where there is a bunny. The goal is to pick up as many bunnies as possible before the door at the end point closes. The time it takes to get from a to b is given as a matrix, which is not necessarily symmetric. So going a->b may take a different time than b->a, for whatever reason. The travel time can also be negative, by triggering something which changes the time limit. 

The input is a square matrix (Python list of lists) with zeroes on the diagonal, which contains all travel times. In graph theory, this is known as an **adjacency matrix**. The other input is the time limit.

The solution has to return the best path as a list of the positions you move across. "Best" means to collect as many bunnies as possible and reach the exit before the time limit, and if several paths with the same number of bunnies are possible, return the one with the bunnies which have the lowest id numbers (according to the number of their location). While it is not stated explicitly the example provided made clear that one can carry more than one bunny at the same time.

#### Approach
After lots of fiddling around I came across the **Bellman-Ford** algorithm. This is a method to compute the **shortest** distance between points in a graph. It may be that going a -> b -> c is actually faster than the direct path a -> b, especially in a setup with asymmetric or negative distances. Negative distances can also lead to the existence of inifinite loops, where one can gain inifinite amount of times and therefore is always able to collect all bunnies.

#### Optimized graph and infinite loops
Using this Bellman-Ford algorithm I could obtain a new adjacency matrix which contains the shortest path between each node. This is done by repeatedly checking whether an indirect path is shorter than the direct one, until the matrix doesn't change anymore. An infinite loop manifests in the appearance of non-zero (negative) diagonal elements. As soon as such an element appears, the game is won and I can just end the program and return the full bunny list.

#### Simplified problem
The description explicitly states that one can re-visit previously visited nodes. However, once I had the optimized graph with the shortest routes between each node, I realized that on this graph it is no longer necessary to re-visit nodes (or the end node before I have the maximum possible number of bunnies). This means I just have to find the best path that visits the most possible intermediate nodes. These are up to 5 nodes, if the start is node 0 and the end node N, then the intermediate ones are 1,2,...,N-1, with no more than 5 possible intermediate nodes. I only need to visit each once, so I just have to check all possible permuations of 1,2,...,N-1, which is not a large number (5! = 120).

#### Loop over all permuations
So I loop over all permutation of 1,2,...,N-1 and for each permutation I check what is the longest path within the time limit (in other words, when I have to abort and head for the exit) and which bunnies I grab. From these I get the best result and voila, done!
