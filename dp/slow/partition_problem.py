'''
 Partition problem:
   Partition problem is to determine whether a given set can be partitioned into two(only two) subsets
   such that the sum of elements in both subsets is same. both these subsets include all elements

   eg: A = [1,5,11,5]
       output: true
           {1,5,5} , {11}

       A = [1,5,3]
       output = false


     brute-force solution:
        1. As we need to partition given array into extractly two subarrays such that sum equal in both,
           and all elements must be there in both.
            A  ----> B + C
            S = sum(A)
           since, sum(B) = sum(C) = x
           2x = sum(A) = S
            x = S/2 = sum(A)/2

        2. if the sum(A) is odd, we cannot partition into two subsets such that sum equal, return False
        3. if sum is even, we have following situations:
              a. we can partition into two subsets
              b. we cannot partition eg: [1,2,5] or [12, 18]
        4. try to build a subset with sum = sum(A)/2 , we can not build using following:
               Let f(A, sum, n) denote true if we can form sum(sum(A)/2) from  the given array A. n = |A|

               f(A, sum, n ) = solution we can form considering the last one in solution  or  not considering it
                              = f(A, sum- A[n-1] , n-1) or f(A, sum, n-1)

               once we can sure we can form one subset with sum= sum(A/2), Then automatically remaining form the 
               other subset with equal sum
      
               base case: if sum == 0 then 
                             return true
                       
                         if n == 0 then
                            return False
 
                         if A[n-1] > sum  then
                            return f(A, sum, n-1)

              time complexicity: O(2^n)
                     
'''

import sys
def partition(A, s, n):

 if s == 0 :
  return True
 
 if n == 0:
  return False
 
 if A[n-1] > s:
  return partition(A, s, n-1)

 return partition(A, s-A[n-1], n-1) or partition(A, s, n-1)



def check_function(A):
 S = sum(A)
 if not S%2 == 0:
  print "Cannot partition array into two subset with equal sum"
  return
 else:
   print "partition_status:{}".format(partition(A, S/2, len(A))) 




#A = [3, 1, 5, 9, 12]
#A = [1,5,11,5]
A = [12, 18]
check_function(A)
