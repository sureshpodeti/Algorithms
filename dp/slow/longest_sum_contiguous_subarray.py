'''
 Longest sum contigous subarray:
  Given an one-dimensional array. we need to find the logest contigous subarray which gives the maximum sum
  eg: A = [a,b,c]

  brute-force algorithm: Generate and test
   a1= [a]
   a2= [a, b]
   a3= [a,b,c]
  
   b1 = [b]
   b2 = [b,c]
   
   c1 = [c]
   so, we need to return  the max(a1,a2,a3,b1,b2,c1)
   time complexicity of the brute-force algorithm is O(n^2)
      
'''
from sys import maxint
def longest_sum(A):
 max_value = - maxint
 for i in range(0, len(A)):
  sum = A[i] 
  for j in range(i+1, len(A)):
   sum += A[j]
   max_value = max(max_value, sum)
 return max_value



A =raw_input().split(' ')
A = map(int, A)
print "longes_sum({}):{}".format(A, longest_sum(A))
