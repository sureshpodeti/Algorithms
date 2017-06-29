# _*_ coding: utf-8 _*_
'''
 Given a number 'n', and sum 's'. we need to figure out
 the no.of numbers of 'n' digits where sum of digits in it
 equal to given sum 's'

 brute-force algorithm:
  n = 2, sum = 5
  possible solution are: {50} , {41}, {32}, {23}, {14}
  output : 5

  Let f(n, sum) denote the #.of such nuumbers
   f(n, sum) = f(n-1, sum-i) Ɐ i ∈ {0, 1, ..., 9}
'''

def solutions(n, s):
 if s< 0:
  return 0

 if s == 0 and n==1:
  return 0
 
 if n == 1 and s>9:
  return 0

 if n == 1 and s>=1 and s<10:
  return 1

 count = 0

 for i in range(0, 10):
  count += solutions(n-1, s-i)

 return count

 

n = int(raw_input())
s = int(raw_input())
print "#.of solutions:{}".format(solutions(n,s))
