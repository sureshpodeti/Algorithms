

'''
 Minimum insertions to make string palindrome:
   Given a string 's' we need to figureout minimum no.of insertions needed to make string palindrome.
    we can insert character at any location.


    brute-force solution:
     Let f(s, l, h) gives the minimum #of insertions needed to make palindrome
     1. if the last characters are same, then we need to figureout the minimum insertions in 
       s[1, h-1], i.e f(s, l, h-1)
     2. else, suppose we know the minimum character needed to make string s[0.. h-1] (except last character)
         then we can say 1 + f(s, 0, h-1) will give us the minimum insertion for total string
     3. and, we have picked s[0....h-1] but we have equal chance for picking s[1..h],
            so f(s, 1, h)

   time complexicity: O(2^n)
     
'''
from sys import maxint
def min_insertions(A):

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


st = raw_input()
print "min_insertions:{}".format(min_insertions(st))
