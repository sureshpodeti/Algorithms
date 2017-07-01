'''
  Given time taken by n tasks. Find the minimum time needed to finish the tasks
  such that skipping of tasks is allowed, but can not skip two consecutive tasks.

  brute-force algorithm:
   1. Let f(A, i) denote the minimum time needed to finish the tasks from i to |A|
   2. if we consider the first element (i = 0), now the problem becomes
             A[i] + f(A, i+1)
   3. if we dont consider the first element, then we must consider the second element
      and, now the problem becomes
            A[i+1] +f(A, i+2)

   recurrence relation:
                A[i] + f(A, i+1)   ,   if we consider first element
     f(A, i) =   
                A[i+1] + f(A, i+2) , if dont consider the first element

     f(A, i) = min{A[i]+f(A, i+1),  A[i+1]+f(A, i+2)}

     base case:
          if i >= |A| -1 then
             return 0

     time complexicity: O(2^n)

   dynamic programming technique:
    time complexicity: O(n)
    space complexicity: O(n)
'''

def min_time(A):
 
 s = [0]*(len(A)+2)

 for i in range(len(A)-2, -1, -1):
   s[i] = min(A[i]+s[i+1], A[i+1]+s[i+2]) 
 
 return s[0]



#A = [10,5,7,10]
#A = [10]
#A = [10, 30]
#A = [10, 5, 2, 4, 8, 6, 7, 10]
A = [10, 5, 2, 7, 10]
#A = [10]
print "min_time:{}".format(min_time(A)) 
