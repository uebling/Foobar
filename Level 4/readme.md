# Level 4
Level 4 has 2 problems, each with a time limit of 15 days. A big jump!

## Problem 1
### Gun to a guard fight
You and a bad guy are trapped in a room with mirror walls. Calculate how many ways there are to shoot him with a laser gun that has a maximum effective range. And don't shoot yourself.

This problem was surprisingly easy for level 4. The main challenge was to figure out what they mean by "dimensions" of the room and where the walls are relative to the lattice points. Then I stumbled over a Python peculiarity where I changed elements of a list without wanting to nor realizing that I did it.

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
Reach the exit before the door closes and collect as many bunnies on the way as possible.
