# _*_ coding: utf-8 _*_
'''
 Minimum squares need to make given numer 'n'.
 eg: n =6
  1^2 + 1^2 + 1^2 +1^2 + 1^2 + 1^2 = 6
  1^2 + 1^2 + 2^2 = 3
  so, answer is 3.
  

  brute-force approach:
   Let f(n) denote  the minimum no.of squares to make given number 'n'
   eg: 
    n = 8
   solutions are:
  1^2 + 1^2 + 1^2 + 1^2 + 1^2 + 1^2 + 1^2 + 1^2 = 8, #=8
  1^2 + 1^2 + 1^2 + 1^2  + 2^2= 8, #=5
  2^2 + 2^2 = 8 , #= 2
  min(8, 5,2) = 2 (answer)

  we are trying all possibilities, we can be formed by 1, 2, 3 ... as
  the starting square, and returning the min value of them

  recurrence relation:
  f(n) = 1 + min(f(n-x)) Ɐ x  ∈ {1,2,3,..c} where c*c<= n
  
  base case:
   if n == 0 or n == 1 then 
     return n


 dynamic programming approach:
  time complexicity: O(n^2) 
  space complexicity: O(n) 
'''
from sys import maxint
def min_squares(n):
 s = [0]*(n+1)
 s[1] = 1
 
 for j in  range(2, n+1):
  min_value = maxint
  for i in range(1, j):
   if i*i > j:
    break

   value = 1 + s[j-i*i]

   min_value = min(min_value, value)

  s[j] = min_value

 return s[n]

n = int(raw_input())
print "min_squares:{}".format(min_squares(n))
