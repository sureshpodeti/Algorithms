'''
 Given a matrix with all one's and zero's we need to figure out 
 max sized square submatrix, which has all ones. we should return 
 size of the square submatrix which has all ones. 

 brute-force : generate and test - will compute the answer in O(2^n)
 
 dynamic programming technique:
     
      |   |   |  |
     -----------------
      | A | B |  |
     ---------------- 
      | C | X |  |
     ----------------
      |   |   |  |

   we can form square matrix which ends X as the right-most bottom element using,
    A, B, C by increasing one unit.
    eg. square submatrix X is formed by increasing one unit of square submatrix C, length wise and
    height wise . similary for B, and A

   suppose, if we know mazimum square submatrix which ends at A, B, and C respectively as the right
   most bottom element and formed by all 1's. 
   Is it possible to get the square submatrix which ends at X as the right-mose bottom element ???
   answer is Yes, 
          Let f(X) denote the size square matrix whose right-most bottom corner ends at X and has all 1's
         f(X) = min{f(A) , f(B), f(C)} + 1 if the X value is 1 otherwise 0
    
      why this recurrence relation explained below:
      --------------
      |   -------- | 
      |  |A -------| ------
      |  |  | B    |      |
      |  ----------|-------
      ------C-------  X

     if X == 1: 
        It can sure that min length of these three(A,B,C) will make maximum square submatrix which 
        ends at X as the right-most bottom element with all 1's.


   time complexicity : O(m*n) 
    space complexicity: O(m*n)

     
'''
from sys import maxint

def square_sub_matrix(A, m, n):
 s = [[None for i in range(n)] for x in range(m)]
 
 for i in range(0, m):
  for j in range(0, n):
   if i == 0 or j ==0:
    s[i][j] = A[i][j]
   elif A[i][j] == 1:
    s[i][j] =  min(A[i][j-1], A[i-1][j-1], A[i-1][j]) + 1
   else:
    s[i][j] = 0 
 
 print s
 # get the maximum value from s
 max_value = -maxint
 for i in range(0, m):
  for j in range(0, n):
   max_value = max(max_value, s[i][j])

 return max_value



A =  [[0, 1, 1, 0, 1], 
      [1, 1, 0, 1, 0], 
      [0, 1, 1, 1, 0],
      [1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1],
      [0, 0, 0, 0, 0]
     ]
  
print "square_sub_matrix({}):{}".format(A, square_sub_matrix(A, 6, 5))
