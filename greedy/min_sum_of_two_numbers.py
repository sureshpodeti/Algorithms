'''
 Minimum sum of two numbers formed from digits of an array:
   Given an array of digits(values are from 0 to 9), find the minimum possible sum of 
   two numbers formed from digits of the array. All digits of given array must be used
   to form the two numbers.

   Greedy approach:
     for simplicity we assume array is sorted( sorting takes O(n*log(n))
    
        A < B < C < D
        solution:
          {AB}, {CD}
          {AC}, {BD}
          {AD}, {BC}

          AB+CD = (10*A+B)+(10*C+D) = 10*(A+C) + (B+D) = X 
          AC+BD = (10*A+C)+(10*B+D) = 10*(A+B) + (C+D) = Y
          AD+BC = (10*A+D)+(10*B+C) = 10*(A+B) + (D+C) = Z
  
          return min(X, Y, Z), so the answer is Y or Z

  
    so, the idea is to construct two numbers using alternate numbers like
           A, B, C ,D
        AC, and BD

   here, in constructing the number we are greedily choosing .
                 
'''

def min_sum(A):

 first_num = second_num = 0
 i, j  = len(A)-1, len(A)-2
 
 count = 0
 while i>=0 or j>=0:
  if i>=0:
   first_num += 10**count*A[i]
   i += -2
 
  if j>=0:
   second_num += 10**count*A[j]
   j += -2
  
  count += 1
  
 return first_num+second_num

A = [1,2,3,4]
#A = [2,3, 4,5,6,8]
A = [0,3,4,5,7]
print "min_sum:{}".format(min_sum(A))
