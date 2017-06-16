'''
 Maximum sum increasing subsequence:
 Given an array, find the maximum sum increasing subsquence:
 
 time complexicity: O(n^2)
 space complexicity: O(n)
'''

def max_sum(A):
 s = []
 for i in range(len(A)):
  s.append(A[i])
 
 for j in range(1,len(s)):
  for i in range(0, j):
   if A[i] < A[j] and (s[i]+A[j] >= s[j]):
    s[j] = s[i] + A[j]
    

 return max(s)

A = raw_input().split(' ')
A = map(int, A)

print "MSIS:{}".format(max_sum(A))
