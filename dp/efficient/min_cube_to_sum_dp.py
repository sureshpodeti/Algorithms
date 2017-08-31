
from sys import maxint


def min_squares(n):
 if n<=3:
  return n

 table = [0]*(n+1)

 for i in range(n+1):
  table[i] = i

 for i in range(8, n+1):
  x = 1
  while x**3<=i:
   table[i] = min(table[i], 1+table[i-x**3])
   x += 1

 return table[n]





n = int(raw_input())
print "min squares:{}".format(min_squares(n))
