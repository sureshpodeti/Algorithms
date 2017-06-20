'''
Maximum path sum for each position with jumps under divisibility condition:
 Given an array of n positive integers. Initially we are at first position. We can jump position y to position x if y divides x and y < x. The task is to print maximum sum path ending with every position x where 1 <= x <= n.

Here position is index plus one assuming indexes begin with 0.

 dynamic programming solution:
  time complexicity: O(n^2)
  space complexicity: O(n)
'''

def max_sum_path(A, m):
 s = [0]*(m+1)

 s[1] = A[0]

 for j in range(2, m+1):
  for i in range(1, j):
   if j%i == 0:
    s[j] = max(s[j], s[i]+ A[j-1])

 return s[1:]




A = [2,3,1,4,6,5]
print "max_sum_path:{}".format(max_sum_path(A, len(A)))
