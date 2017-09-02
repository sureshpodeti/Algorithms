

def possible_decodings(n):
    if d.has_key(n):
        return d[n]
    
    last_two = n%100

    if last_two == 0:
        d[n] = 0
    elif last_two %10 == 0 and last_two>20:
        d[n] = 0
    elif last_two %10 == 0:
        d[n] = possible_decodings(n/100)
    elif last_two>=1 and last_two<10:
        d[n] = possible_decodings(n/10)
    elif last_two <= 26:
        d[n] = possible_decodings(n/10) + possible_decodings(n/100)
    else:
        d[n] = possible_decodings(n/10)
    
    return d[n]


d = {0:0, 1:1,2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:2, 12:2, 13:2, 14:2, 15:2, 16:2, 17:2, 18:2, 19:2, 20:1, 21:2, 22:2, 23:2, 24:2, 25:2, 26:2}
while True:
    n = raw_input()
    if n == '0':
        break
    print str(possible_decodings(int(n)))
