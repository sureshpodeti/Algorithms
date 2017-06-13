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
   
   dynamic programming solution:
    **kadane's algorithm**
      Here we generate the longest sum subarray which ends at the current index,we check for all indexes in the array
        Suppose we know the longest sum subarray which ends at i, can we find longest sum subarray which ends at i+1???
         Yes, lonest sum subarray which ends at i+1, may include {(longest sum subarray which ends at i+ the i+1 element) ,or
           (current element of (i+1)th position)}

        |----subarray(A)----------------------|
      -------------------------------------------------------------------
             |_LSSA ends at index i_(M)_______| (i+1)element
                 |________subarray_(B)________|
     
       we know, sum(M) > sum(A) 
                sum(M) > sm(B)
          so,  sum(M) + A[i+1] > sum(A) + A[i+1]

       hence, it is correct to say that lonest sum subarray which ends at i+1, may include {(longest sum subarray which ends at i+ the i+1 element) ,or
           (current element of (i+1)th position)}
      
       time complexicity of the algorithm: O(n)
       
          
'''
from sys import maxint
def longest_sum(A):
 global_max = current_max = A[0]
 for x in A[1:]:
  current_max = max(current_max+x, x)
  global_max = max(global_max, current_max)
 return global_max



A =raw_input().split(' ')
A = map(int, A)
print "longes_sum({}):{}".format(A, longest_sum(A))
