'''
 Given a weight array 'A', we need to figure out
  Is there a way to make given weight 't' by 
  picking one or more weights from the array 'A'


 psudo code:
  brute-force algorithm:
   1. Let f(A, m,t) (where m = |A|) denote true/false
       if we have atlease one solution
   2. we can pick any element from the A and check if 
       it forms atleast one solution, then we say that
        we have a solution
   3. if we can not form atleast one solution by picking
      last element in A, we cannot say surely we dont have
      any solution, but we can say if any of the rest elements
      forms atleast one solution we have solution otherwise not


   time complexicity: O(2^n)

  dynamic programming: 
   time complexicity: O(m*t)
   space complexicity: O(m*t)
'''
def is_solution(A, m, t):

 s = [[0 for i in range(t+1)] for x in range(m+1)]

 #intialize matrix for colum(i=0) with all 1's
 for i in range(m+1):
  s[i][0] =1

 #intialize matrix for row (i=0) with all 0's
 for i in range(1, t+1):
  s[0][i] = 0

 # fill rest of the solution matrix
 for i in range(1, m+1):
  for j in range(1, t+1):
   if A[i-1] > j:
    s[i][j] = s[i-1][j]
   else:
    s[i][j] = s[i-1][j-A[i-1]] or s[i-1][j]


 return s[m][t] ==1


A = [3,34,4,12,5,2]
t = 9
print "is_solution:{}".format(is_solution(A, len(A), t))
