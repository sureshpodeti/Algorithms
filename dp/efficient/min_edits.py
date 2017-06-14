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
     
   Dynamic programing technique:
     better understanding demonstration:
       ---------
       |G|e|e|k|
       ---------
               i
       ---------
       |G|e|s|k|
       ---------
              j

       we come from the last index, we check if last character in both are same if yes means 
       no edit was made to s1 in making last character.
       
        now, the problem looks:
       -------
       |G|e|e|
       -------
             i
       -------
       |G|e|s|
       -------
            j
      Now, last characters are different, question: what operation could have resulted in different 
      characters?? 
     it means we must have done any of the operation:
        we could have done : insertion 's' into s1 
       -----
       |G|e|
       -----
           i
       -------
       |G|e|s|
       -------
            j
  
        we could have done: replacement
       ------
       |G|e|e
       ------
            i
       -------
       |G|e|s|
       -------
            j
        
       we could have done: remove
        
       --------
       |G|e|s|x
       --------
              i
       -------
       |G|e|s|
       -------
            j

      any of these operation must have taken place, thats why we are getting different last characters as mentioned.
      hence, if last characters are differnent
        f(s1,s2,m,n) = 1 + min{f(s1,s2,m-1,n), f(s1,s2,m,n-1), f(s1,s2,m-1,n-1)} , for insertion, remove,and replacement
        
      





  
'''
def min_operations(s1, s2, m,n):
 s = [[0 for i in range(n+1)] for x in range(m+1)]
 for i in range(m+1):
  for j in range(n+1):
   if i == 0:
     s[i][j] = j
   elif j == 0:
     s[i][j] = i
   elif s1[i-1] == s2[j-1]:
     s[i][j] = s[i-1][j-1]
   else:
     s[i][j] = 1 + min(s[i][j-1], s[i-1][j-1], s[i-1][j])

 return s[m][n]

s1, s2 = raw_input().split(' ')
print "min_operations:{}".format(min_operations(s1,s2, len(s1), len(s2))) 
