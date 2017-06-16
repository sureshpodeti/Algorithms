'''
 Minimum #.of jumps reach to end from the beginning:
  Given an array of non-zero integers:
   eg:  [1,3,5,8,9,2,6,7,8,9]
       each number denote the #.of jumps atmost one can take from the current position,
         example, first one should visit index 0 --> 1 , from one one can visit index(2,3,4)

  we need to return minimum #.of jumps to reach to the end from the beginning
  
 time complexicity: O(n^2)
 space complexicity: O(n)
'''
from sys import maxint
def minimum_jumps(A):
 s = [0]*len(A)
 
 if A[0] == 0: 
  return maxint

 for j in range(1, len(s)):
  for i in range(0, j):
   if i+A[i] >= j:
    s[j] = s[i] + 1
    break

 return s[len(s) -1]




A = raw_input().split(' ')
A = map(int, A)
print "minimum_jumps({}):{}".format(A, minimum_jumps(A))
