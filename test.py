import itertools

def foo(l):
     yield from itertools.product(*([l] * 3)) 

bebig = input()

for x in foo(bebig):
     print(''.join(x))