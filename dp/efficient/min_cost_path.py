'''
 Min cost path: 
   Given a matrix where each cell has some interger value which represent the cost incurred
   if we visit that cell.
    
   Task is found min cost path to reach (m,n) position in the matrix from (0,0) position
   
   possible moves: one step to its right, one step down, and one step diagonally

   brute-force : generate and test
   Let f(i,j) denote the min cost path needed to reach (i,j) position from (0,0) position
   Suppose, if we have f(i-1,j), f(i-1, j-1), and f(i, j-1) , 
   Is it possible to find f(i,j) from know values ??? 
    answer: yes, we can as shown below
     f(i,j) = A[i][j]+min{f(i-1, j-1), f(i-1,j), f(i, j-1)}
     base condition :  if i<0 or j<0 then return 0
                       if i ==j and i==0 then return A[i][j]
     
   dynamic programming:
    This problem posses two important properties of dp:
       1. optimal substructure [seen from above recurrence relation]
       2. overlapping subproblems [ diagonal element  is calcuated repeated]

    psudo code :
     1. Intialize a solution matrix of as same size of matrix A , with all zero's
     2. for the first row do this, 
         for i in range(1, |s|row):
            s[0][i] = A[0][i] + s[0][i-1] 
    3. for the first column do this,
        for i in range(1, |s|colum):
            s[i][0] = A[i][0] + s[i-1][0]
    4. for rest , do this,
        for i in range(1, |s|row):
          for j in range(1, |s|colmn):
            s[i][j] = A[i][j] + min(s[i-1][j], s[i-1][j-1], s[i][j-1]) 
    5. return s[m-1][n-1]

   time complexicity of dp solution : O(m*n)
   space complexicity : O(m*n)
        
'''
from sys import maxint
def min_cost_path(A):
 s = [[0 for x in range(3)] for j in range(3)]
 
 s[0][0] = A[0][0]
 # intialize the first row
 for j in range(1, len(A)):
  s[0][j] = A[0][j] +s[0][j-1]
 
 # intialize the first column
 for j in range(1, len(A)):
  s[j][0] = A[j][0] + s[j-1][0]
  
 # fill the rest cells
 for i in range(1, len(A)):
  for j in range(1, len(A)):
   s[i][j] = A[i][j] + min(s[i-1][j], s[i-1][j-1], s[i][j-1])
 return s[len(A)-1][len(A)-1]
 
A = [ [1, 2, 3], [4, 8, 2], [1, 5, 3] ]
print "min_cost_path({}):{}".format(A, min_cost_path(A))
