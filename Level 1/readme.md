This was the first problem, which is quite simple. I was supposed to write an input integer as a sum of squares, and in case of multiple solutions only the sum with the largest possible square. This can be simply found by calculating the square root of the input and taking its floor. Then you subtract it, put it in a list, repeat until you reach 1. At the end return the list. Time limit was 48 hours, very generous.