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
     
'''
from sys import maxint
def min_cost_path(A, m,n):
 if m<0 or n<0:
  return maxint 
 if m==n and m==0:
  return A[m][n]
 return A[m][n]+ min(min_cost_path(A, m-1, n), min_cost_path(A, m-1, n-1), min_cost_path(A, m, n-1))


A = [ [1, 2, 3], [4, 8, 2], [1, 5, 3] ]
inp = raw_input().split(' ')
m,n = map(int, inp)
print "min_cost_path({}):{}".format(A, min_cost_path(A, m, n))
