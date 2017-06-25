# _*_ coding: utf-8 _*_
'''
  maximum product cutting:
    We have a rod of length 'n'. we need make atleast one cut.
    cut the rope in different parts of integer lengths in a way
    that maximizes product of lengths of all parts.

    brute-force approach:
     Let f(n) gives the maximum product obtained by cutting the 'n' length rod
    
     we can make cut at (n-1) different locations. 
       try making cut at each location and we have following cases:
        1. we can make cut at x ∈ {1,...,n-1} , and we could get:
           a.  x*(n-x) product or 
           b. x*f(n-x) product
        then, we should figure out the a, b. like that we need to find the same at
        x in all possible locations . and finally we should return the maximum product

   dynamic programming approach:
     recurrence formula: 
      f(n) = max{i*(n-i), i*f(n-i)} Ɐ i ∈  {1,2,3, .., n-1}
     time complexicity: O(n^2)
     space complexicity: O(n)
'''

from sys import maxint

def max_product(n):
 s = [0]*(n+1)
 
 for j in range(2, n+1):
  max_value = -maxint
  for i in range(1, j):
   value = max(i*(j-i), i*s[j-i])
   max_value = max(max_value, value)

  s[j] = max_value

 return s[n]

n = int(raw_input())
print "maximum_product:{}".format(max_product(n))
