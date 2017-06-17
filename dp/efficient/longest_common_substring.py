'''
 length of common substring:
  Given string s1, s2 , we need to return length of common substring.

   eg:
   s1 = 'geek', s2 = 'gees'
   length of common substring (s1,s2) = 3 , i.e (geek)

   algorithm for length of common substring(LCS):
       s1 = .....................
       s2 = ...............

        
'''

def lcs(s1, s2):
 s = [[0 for i in range(len(s2)+1)] for x in range(len(s1)+1)]
 
 answer = 0
 for i in range(1, len(s1)+1):
  for j in range(1, len(s2)+1):
   if s1[i-1] == s2[j-1]:
    s[i][j] = s[i-1][j-1] + 1
    answer = max(answer, s[i][j])
   else:
    s[i][j] = 0

 return answer



s1 = raw_input()
s2 = raw_input()
print "LCS({},{}):{}".format(s1, s2, lcs(s1, s2))
