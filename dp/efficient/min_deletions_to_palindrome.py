'''
 Given string 's', we need to figureout the minimum no.of deletions needed to make
 string a palindrome.
 
 eg: s = 'suresh'
counters  i    j   

   Let f(s, i, j ) denote the min no.of deletions needed make string palindrome

   1. if last and first characters are same, then 
       recurr for the f(s, i+1, j-1)
   2. else, then
       get 1 + min{f(s, i, j-1), f(s, i+1, j)}

   brute-force recurrence relation:

                      f(s, i+1, j-1)     if s[i] == s[j] , last and first character are same
    f(s, 0, |s|-1) =
                       1 + min{ f(s, i, j-1) , f(s, i+1, j)} , otherwise

   base case: if i == j then 
               return 0

   time complexicity: O(2^n)

  dynamic programming solution:
   time complexicity: O(n^2)
   space complexicity: O(n^2)
  
''' 
def min_deletions(A):
 s = [[0 for i in range(len(A)+1)] for x in range(len(A)+1)]

 # intialize first row and first column to all zero's
 for i in range(0, len(A)+1):
  s[0][i] = 0 
  s[i][0] = 0
  s[len(A)][i] = 0 

 for i in range(len(A)-1, 0, -1):
  for j in range(1, len(A)+1):
   if i == j:
    s[i][j] = 0
   elif i>j:
     s[i][j] = 0

   elif A[i-1] == A[j-1]:
     s[i][j] = s[i+1][j-1]
   else:
     s[i][j] = 1 + min(s[i][j-1], s[i+1][j])
 
 return s[1][len(A)]

 

s = raw_input()
print "min_deletions:{}".format(min_deletions(s))
