'''
 Given a number n, we can divide it in only three parts n/2, n/3 and n/4 (we will consider only integer part). The task is to find the maximum sum we can make by dividing number in three parts recursively and summing up them together.

 dynamic programming  solution:
   time complexicity: O(n)
   space complexicity: O(n)
'''

def break_num(n):
 s = [0]*(n+1)
 s[1] = 1

 for i in range(2, n+1):
  s[i] = max(s[i/2]+s[i/3]+s[i/4], i)
  
 return s[n]
 

n = int(raw_input())
print "answer:{}".format(break_num(n))
