# Level 5
Level 5 has 1 problem, with a time limit of 22 days.

## Problem 1: Dodge the lasers
Calculate the sum ![f1]. Sounds simple, but n can be any number from 1 to 10^100.

Those weird half-brackets above denote the **Floor** function, which rounds down a number to its integer part. This can be computed easily in Python using the int(x) function, or the floor(x) function from the math library, which cannot be used in the Foobar environment however. The problem here is that calculating the whole sum up to 10^100 takes forever, so it is obvious from the start that we are looking for some sort of shortcut or an explicit formula.

### How not to do it
On Wikipedia I came across an explicit formula for a sum ![f2] for the case of a rational number r = p/q and n being a multiple of q. The square root of 2 is not rational, but on a computer with a finite precision every number is rational. Here, sqrt(2) = 1.41421356237309504 = 141421356237309504/100000000000000000. There are also ways of approximating sqrt(2) via continued fractions, such as shown [here](https://en.wikipedia.org/wiki/Square_root_of_2). With this one could calculate the sum up to a value which allows sqrt(2) to be represented as a rational number and do the rest of the sum drirectly, but this can still mean having to calculate too many terms directly. If I ignore the conditions for the explicit formula and just use a value for n which is not a multiple of q, I actually get lots of test cases right but some results are off by +/-1.

### How to do it
After more searching at some point I came across [Beatty's Theorem](https://www.cut-the-knot.org/proofs/Beatty2.shtml). This link contains everything to solve this problem. The sequence ![f3] is apparently called a Beatty sequence. Beatty's Theorem says that for each ![Br] there is a complementary series ![Bs] where 
1/r+1/s=1.
Both series partition the natural numbers, which means that every natural number is either in B_r or B_s, never in both. In our case, ![f4] and ![f5], and with s being an integer (which can be pulled out of the floor function) plus sqrt(2), this already smells like a recursive solution can be constructed.

The next step is to find out to which term we have to sum up ![Br] and ![Bs] to get the sum over all integers up to a certain number N. Since N=N/r+N/s, and therefore ![f6], we know how many terms of each sum we need:
![f7], where ![nr] and ![ns].


[f1]: http://chart.apis.google.com/chart?cht=tx&chl=\sum_{i=1}^n\left\lfloor\sqrt(2)i\right\rfloor
[f2]: http://chart.apis.google.com/chart?cht=tx&chl=\sum_{i=1}^n\left\lfloor{ri}\right\rfloor
[f3]: http://chart.apis.google.com/chart?cht=tx&chl=B_r=\left\lfloor{ri}\right\rfloor
[Br]: http://chart.apis.google.com/chart?cht=tx&chl=B_r
[Bs]: http://chart.apis.google.com/chart?cht=tx&chl=B_s
[f4]: http://chart.apis.google.com/chart?cht=tx&chl=r=\sqrt{2}
[f5]: http://chart.apis.google.com/chart?cht=tx&chl=s=2%2B\sqrt{2}
[f6]: http://chart.apis.google.com/chart?cht=tx&chl=N-1=\left\lfloor\frac{N}{r}\right\rfloor{}%2B{}\left\lfloor\frac{N}{s}\right\rfloor
[f7]: http://chart.apis.google.com/chart?cht=tx&chl=\sum_{i=1}^{N-1}i=\sum_{i=1}^{n_r}\left\lfloor\sqrt(2)i\right\rfloor%2B\sum_{i=1}^{n_s}\left\lfloor2%2B\sqrt(2)i\right\rfloor
[nr]: http://chart.apis.google.com/chart?cht=tx&chl=n_r=\left\lfloor\frac{N}{\sqrt{2}}\right\rfloor
[ns]: http://chart.apis.google.com/chart?cht=tx&chl=n_r=\left\lfloor\frac{N}{2%2B\sqrt{2}}\right\rfloor
