#_*_ coding: utf-8 _*_
'''
 Given a linear equation, we need to return the #.of possible solution.

 eg: x + 2y = 5 
    This eqn. can have (1,2), (3,1), (5,0) as solutions, so we should return 3.

  variable coefficients are taken in the program as list:
   coeff = [1,2]
   rhs = 5

   brute-force approach:
     time complexicity would be exponential.
     
     x + 2y + 2z = 5 
     
     we take z ∈ {0,1,2, ...} such that 2*z <= 5
     x + 2*y + 2*z = 5
     x + y + k = 5 , now  the problem becomes x + 2*y = k'
     problem reduced to two variable from three [optimal substructure]
    
   
    
'''
def solution(A, m, rhs):

 if rhs == 0:
  return 1

 if m == 0:
  return 0
 
 no_of_solutions = 0
 i = 0
 while A[m-1]*i <= rhs:
  no_of_solutions += solution(A, m-1, rhs-A[m-1]*i)
  i += 1
 return no_of_solutions

coeff = raw_input().split(' ')
coeff = map(int, coeff)
rhs = int(raw_input())
print "solution({}):{}".format(coeff, solution(coeff, len(coeff), rhs))
