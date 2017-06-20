'''
 Friends pairing problem:
 
 We have n friends, we need to sent invite to them for a evening part.
 eigther we could invite by person( only one) , or we could invite two 
 at a time.
 
 how many #of way we can invite them.


 brute-force solution:
   eg: n =1 
       A 
     {A} only one way
 
       n = 2, 
      A, B    are persons
     {A}, {B}
      {A, B}
        #of ways = 2
    
    n = 3 
     A, B ,C  are persons
    {A},{B},{C}
     {A,B}, {C}
     {A,C}, {B}
     {B,C}, {A}
     {A,B,C}
   
     from above we can write the following:
     Let f(n) represent the #no.of ways we can invite n persons

      f(n) = # of solutions where A being single + # of solutions where A being paired with some one
           = f(n-1)  + A can pair with any one of n-1 persons and at each of these pairs we have f(n-2) ways to invite them.
           = f(n-1) + (n-1)* f(n-2)

     base case would be: f(1) = 1, f(2) = 2 , f(3) = 5

    time complexicity : O(2^n)
'''
def friend_pairing(n):
 
 if n==0 or n==1 or n==2:
  return n
 return friend_pairing(n-1) + (n-1)*friend_pairing(n-2) 

n = int(raw_input())
print "#.of pairs = {}".format(friend_pairing(n))
