'''
 Longest subsequence such that difference b/w adjacent numbers in the 
 sequence is one

 dynamic programming technique:
  time complexicity: O(n^2)
  space complexicity: O(n)
'''

def answer(A):
 s = [1]*len(A)

 for j in range(1, len(A)):
  for i in range(0, j):
   if 



A = [10,9,4,5,4,8,6]
print "solution:{}".format(answer(A))
