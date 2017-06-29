'''
 Given a weight array 'A'. we need to figureout
  no.of subsets of elements in 'A' will sum up to weight't'


 psudo code:
  brute-force algorithm:
   1. Let f(A, m, t) (where m =|A|) denote no_of solutions 
   2. we can pick any element from the A and check if 
       how many solutions it forms, or how many solutions
       include this element in solution subset

       eg: A =[3,4,7,2,1], t = 7
           possible solutions are:
             1. {3,4}
             2. {7}
             3. {2,1,4}
 
       so, we can write:
        total_no_of solutions = solutions where '4' included +
                            solutions where '4' do not include

    time complexicity: O(2^n)

  dynamic programming approach:
   time complexicity: O(m*t) 
'''

def no_of_subsets(A, m,t):
 s = [[0 for i in range(t+1)] for x in range(m+1)]

 #intialize matrix for column (i=0) with all 1's
 for i in range(m+1):
  s[i][0] = 1

 # intialize matrix for row(i=0) with all 0's
 for i in range(1, t+1):
  s[0][i] = 0

 # fill rest of the solution matrix
 for i in range(1, m+1):
  for j in range(1, t+1):
   if A[i-1] > j:
    s[i][j] = s[i-1][j]
   else:
    s[i][j] = s[i-1][j-A[i-1]] + s[i-1][j]

 return s[m][t]
 if t ==0:
  return 1

 if m ==0:
  return 0

 if A[m-1] > t:
  return no_of_subsets(A, m-1, t)
 return no_of_subsets(A, m-1, t-A[m-1]) + no_of_subsets(A, m-1, t)



#A = [3,4,7,2,1]
#t = 7
A = [3,34,4,12,5,2]
t = 9
print "no_of_subsets:{}".format(no_of_subsets(A, len(A), t))
