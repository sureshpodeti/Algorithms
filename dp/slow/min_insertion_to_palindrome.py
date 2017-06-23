

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
def min_insertions(st, l, h):
 if l > h:
  return maxint
 
 if l == h:
  return 0
 
 if l == h-1:
  if st[l] == st[h]:
   return 0
  else:
   return 1
 
 if st[l] == st[h]:
  return min_insertions(st, l+1, h-1)
 else:
  return 1 + min(min_insertions(st, l, h-1), min_insertions(st, l+1, h))



st = raw_input()
print "min_insertions:{}".format(min_insertions(st, 0, len(st)-1))
