def narcissistic(n):
    pows = [_i**n for _i in range(10)]
    res = pows[1:]
    for _i in range(n-1):
        res=[s+pows[d]for s in res for d in range(10)]
    lower = 10**(n-1)
    return [k+lower for k,v in enumerate(res) if k+lower == v]
print (narcissistic(1))
print (narcissistic(2))
print (narcissistic(3))
print (narcissistic(4))
print (narcissistic(5))
print (narcissistic(6))
print (narcissistic(7))
print (narcissistic(8))
print (narcissistic(9))
print (narcissistic(10))
 
import re
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
