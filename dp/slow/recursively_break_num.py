'''
 Given a number n, we can divide it in only three parts n/2, n/3 and n/4 (we will consider only integer part). The task is to find the maximum sum we can make by dividing number in three parts recursively and summing up them together.

 brute-force solution:
   time complexicity: O(3^n)
'''
def break_num(n):
 if n==0 or n == 1:
  return n
 
 return max(break_num(n/2)+break_num(n/3) + break_num(n/4), n)


n = int(raw_input())
print "answer:{}".format(break_num(n))
