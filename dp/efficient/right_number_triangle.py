'''

Maximum sum of a path in a Right Number Triangle

Given a right triangle of numbers, find the largest of the sum of numbers that appear on the paths starting from the top towards the base, so that on each path the next number is located directly below or below-and-one-place-to-the-right.

 dynamic programming technique:
  time complexicity: O(n^2)   n = size of the matrix
  space complexicity: O(n^2) 

'''

def right_number(A, m):
 s = [[ 0 for i in range(m)] for x in range(m)]
 
 #intialize the last row
 for j in range(m):
  s[m-1][j] = A[m-1][j]

 #build remaining matrix
 for i in range(m-2, -1, -1):
  for j in range(0, i+1):
   s[i][j] = A[i][j] + max(s[i+1][j+1], s[i+1][j])

 return s[0][0]





#A = [[1,0,0,0],[1,2,0,0],[4,1,2,0],[2,3,1,1]]
A = [[2,0,0], [4,1,0], [1,2,7]]
print "right_number:{}".format(right_number(A, len(A)))
