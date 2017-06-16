'''
 Minimum #.of jumps reach to end from the beginning:
  Given an array of non-zero integers:
   eg:  [1,3,5,8,9,2,6,7,8,9]
       each number denote the #.of jumps atmost one can take from the current position,
         example, first one should visit index 0 --> 1 , from one one can visit index(2,3,4)

  we need to return minimum #.of jumps to reach to the end from the beginning
  
 time complexicity: exponential
'''
from sys import maxint
def minimum_jumps(A, i):
 if i >= len(A)-1:
  return 1
 
 if A[i] == 0:
  return maxint

 global_value = maxint
 
 j = i+1
 max_value = 0
 while (j < i+A[i]+1) and i<len(A):
  max_value += minimum_jumps(A, j)
  j += 1   
  global_value = min(max_value, global_value)

 return global_value



A = raw_input().split(' ')
A = map(int, A)
print "minimum_jumps({}):{}".format(A, minimum_jumps(A, 0))
