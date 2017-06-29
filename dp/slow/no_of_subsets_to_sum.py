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
'''

def no_of_subsets(A, m,t):
 if t ==0:
  return 1

 if m ==0:
  return 0

 if A[m-1] > t:
  return no_of_subsets(A, m-1, t)
 return no_of_subsets(A, m-1, t-A[m-1]) + no_of_subsets(A, m-1, t)



A = [3,4,7,2,1]
t = 7
print "no_of_subsets:{}".format(no_of_subsets(A, len(A), t))
