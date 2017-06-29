'''
 Given a number 'n', we need to decode that to possible strings

 eg: n =123
  ABC, AW, LA
   so, the output = 3

   brute-force algorithm:
    Let f(n) denote the #.of possible decodings
    f(n) = #.of solutions where we consider nth digit as sigle digit +
           #.of solutions where we consider nth digit as double digit

                 f(n/10)     if n%100 > 26
    f(n) = 
               f(n/10) + f(n/100)  if n%100 <=26

    base case:
        if n < 10 then 
           return 1

   time complexicity: O(2^n)
'''

def decode(n):
 if n < 10:
   return 1

 a = decode(n/10)
 if n%100 <= 26:
  return a + decode(n/100)

 return a


n = int(raw_input())
print "#.of decodings:{}".format(decode(n))
