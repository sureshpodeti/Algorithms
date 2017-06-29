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
'''
def is_solution(A, m, t):
 if t ==0:
  return True

 if m == 0:
  return False

 if A[m-1] > t:
  return is_solution(A, m-1, t)
 return is_solution(A, m-1, t-A[m-1]) or is_solution(A, m-1, t)



A = [3,34,4,12,5,2]
t = 9
print "is_solution:{}".format(is_solution(A, len(A), t))
