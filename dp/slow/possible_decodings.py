'''
Let n be the input integer
Let f(n) returns the no.of possible decondings
if n ==0, then return 0
if n = 1...10, then return 1
if n>= 10 and n<=26, then return 2
last_two = n%100
if last_two <= 10 or last_two > 26, then return 1 + f(n/100)
else, return f(n/10) + f(n/100)
'''

def possible_decodings(n):
    if n == 0:
        return 0
    if n<=10:
        return 1
    if n == 20:
        return 1
    if n>=10 and n<=26:
        return 2
    last_two = n%100
    if last_two <= 10 or last_two > 26:
        return possible_decodings(n/10)
    else:
        return possible_decodings(n/10) + possible_decodings(n/100)


while True:
    n = int(raw_input())
    if n == 0:
        break
    print possible_decodings(n)
