''' 
  Longest common subsequence:
  **************************
   Applications:
     1. DNA subsequencing, generally DNA contains of 4 modules like AGHT for example. suppose if we found another new DNA 
        and want to see the similarity between both we should find the longest common subsequence in both . The degree of 
        similarity is equal to length of longest common subsquence.
    2. In linux system diff command used to get the differences between two files. eg: diff filename1.py filename2.py
       will give the difference between two files data wise. here each line in the file treated as the complex character in a string 
  **************************
  eg: s1 = 'ABCDGH'
      s2 = 'AEDFHR'
      lcs(s1, s2) = 3 i.e 'ADH'
 
     Brute for algorithm:
     Generate all possible subsequences in each string and match and find the longest subsequence.
     suppose s1 = 'abc' , we can generate 2^n = 2^3 = 8 subsequneces as shown below:
      {}, {a}, {b}, {c}, {a, b}, {a,c}, {b,c}, {a,b,c}
     Like  this generate all the possible subsequences for both s1 and s2 and find the longest subsequence
     Time complexicity would be O(2^n)
     
   Brute force recursive implimenation:
    Let s1, s2 be the strings such that |s1| = m , |s2| = n
    case-1 : suppose we have same last character in both the strings i.e s1[m-1] == s2[n-1], then this
            character should be present in the longest common subsquence
            f (s1[0...m-1], s2[0..n-1]) = 1 + f(s1[0..m-2], s2[0..n-2])
   case-2: if the last characters are not same then
            f (s1[0...m-1], s2[0..n-1]) = max{f(s1[0..m-1], s2[0..n-2]) , f(s1[0..m-2], s2[0..n-1])}
   base condition would be:
         if m == 0 or n==0 then return 0 
  
'''

def lcs(s1, s2, m, n):
 if m<=0 or n<=0:
  return 0
 if s1[m-1] == s2[n-1]:
  return 1 + lcs(s1, s2, m-1, n-1)
 else:
  return max(lcs(s1, s2, m, n-1), lcs(s1, s2, m-1, n))


s1 = raw_input()
s2 = raw_input()
print "lcs({}, {}):{}".format(s1, s2, lcs(s1, s2, len(s1),len(s2)))
