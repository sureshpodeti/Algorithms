'''
 Given an array, we need to return the length of longest increasing subsequence in that.
 
 eg: A = [50, 3, 10, 7, 4, 0,80]
      
 The idea is, if we know the longest increasing subsequence which at index i. 
 can we found LIS which ends at i+1 ????
 
 Yes, we need to follow the below algorithm to do that.

 time complexicity : O(n^2
 space complexicity: O(n)
 
'''
def lis(A):
 s = [1]*len(A)
 
 for j in  range(1, len(A)):
  for i in range(0, j):
   if A[i] < A[j] and s[i]>=s[j]:
    s[j] += 1

 return s[len(s) -1]


A = raw_input().split(',')
A = map(int, A)
print "LIS:({}):{}".format(A, lis(A))
