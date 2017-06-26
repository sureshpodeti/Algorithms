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
 
    we should delete eighter first one or last character and recur for the rest:
     that's how we get 1 + min{f(s, i, j-1), f(s, i+1, j)}

   brute-force recurrence relation:

                      f(s, i+1, j-1)     if s[i] == s[j] , last and first character are same
    f(s, 0, |s|-1) =
                       1 + min{ f(s, i, j-1) , f(s, i+1, j)} , otherwise

   base case: if i == j then 
               return 0

   time complexicity: O(2^n)
   
''' 
def min_deletions(s, i, j):
 if i == j:
  return 0
 if i>j:
  return 0
 
 if s[i] == s[j]:
  return min_deletions(s, i+1, j-1)
 else:
  return 1 + min(min_deletions(s, i, j-1), min_deletions(s, i+1, j))



s = raw_input()
print "min_deletions:{}".format(min_deletions(s, 0, len(s)-1))
