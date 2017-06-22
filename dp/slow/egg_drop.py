# _*_ coding: utf-8 _*_
'''
 Egg drop puzzle:
  we have 'n' storey building, and given two eggs. we need to figureout minimum no.of egg
  drops needed to figure out the critical floor from which egg starts breaking.

  suppose, we where given only one egg. In the worst(dumb) case we would end up trying all
  floors. 

  Here, we have given two eggs and we need to figure out the minimum no.of egg drops.

  brute force solution:
  Let f(k,n) denote the minimum no.of egg drops need to figureout the critical floor in a
  'k' storey building with n = 2 floors.

  suppose, we are at xth floor and we have following cases if we drop the egg from here:
  1. egg can break
  2. egg can not break

  if egg breaks, then we  have to try in the x-1 floors down that . 
  if not breaks, then we should try the floors above xth floor

  f(k,n) = 1 + min{ max{f(x-1, n-1) , f(k-x, n) Ɐ x ∈ {1,2,3, ... , k}}}

  max{f(x-1, n-1) , f(k-x, n) Ɐ x ∈ {1,2,3, ... , k}} ???"
   we have written because in worst case we **must** figure out the minimum drops.

   base case: if k == 1 or k ==0 then
                return k  
              
              if n == 1 then 
                return k          //because for k floors with one egg we should try all
          possible k floors. 
              

   time complexicity: 0(2^n)
'''
from sys import maxint
def min_drops(k, n):
 if k == 1 or k == 0: 
  return k 
  
 # for 
 if n == 1:
  return k
 
 min_value = maxint
 for x in range(1, k+1):
  value = max(min_drops(x-1, n-1) , min_drops(k-x, n))
  
  min_value = min(value, min_value)

 return 1 + min_value
  
  




k = int(raw_input())
print "min_drops:{}".format(min_drops(k, 2))
