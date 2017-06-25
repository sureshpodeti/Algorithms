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
'''
from sys import maxint
def min_squares(n):
 if n == 0 or n == 1:
  return n

 min_value = maxint
 for x in range(1,n):
  if x*x > n:
   break
  value = 1 + min_squares(n-x*x)

  min_value = min(min_value , value)

 return min_value
 

n = int(raw_input())
print "min_squares:{}".format(min_squares(n))
