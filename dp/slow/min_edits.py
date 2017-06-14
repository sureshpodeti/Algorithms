'''
 Given string s1, and s2 . we have following operations each of same cost:
  1. insert
  2. remove
  3. replace
 
  we can perform above three operations on string s1 to make it string s2.
  eg:
    s1 = Geek ,  s2= Gesek
     
    Here, we should insert s into s1 to make it s2. so we need 1 operation.
    hence, answer: 1.
  
    brute  force solution:
     Let us say, f(s1, s2, m,n) denote the min #of operations perform to get s2.
     where m = |s1| , n = |s2|
   
                        f(s1, s2, m-1, n-1)         if s1[m-1] == s2[n-1]
    f(s1, s2, m, n) =

                        1 + min{ f(s1, s2, m, n-1), # insert       otherwise
                                 f(s1, s2, m-1, n), # remove
                                 f(s1, s2, m-1, n-1), # replaced
                               }

    # if the characters are not same, it means we have found one operation need, and 
     which could have been resulted from either insert, remove , or replacement.
     
    base case: if m == 0 then return n
               if n == 0 then reuturn m
     time complexicity: O(3^n)
     because in the worst case:
         T(s1, s2, m, n) = T(,, m, n-1)+ T(,,m-1, n)+ T(m-1,n-1) 
'''
def min_operations(s1, s2, m,n):
 if m ==0 :
  return n
 if n ==0:
  return m
 if s1[m-1] == s2[n-1]:
  return min_operations(s1, s2, m-1, n-1)
 else:
  return 1 + min(min_operations(s1, s2, m, n-1), min_operations(s1, s2, m-1, n), min_operations(s1, s2, m-1, n-1))


s1, s2 = raw_input().split(' ')
print "min_operations:{}".format(min_operations(s1,s2, len(s1), len(s2))) 
