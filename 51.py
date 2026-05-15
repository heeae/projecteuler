import sys
import math

primelist = {}

with open("prime.txt", "rt") as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        if(int(line) < 1000000):
            primelist[int(line)] = True
        
print("built the list")
primelist = list(primelist.keys())


def p51():
	patterns = ['{0}{1}{3}{3}{3}{2}', '{0}{3}{1}{3}{3}{2}',
				'{0}{3}{3}{1}{3}{2}', '{0}{3}{3}{3}{1}{2}',
				'{3}{0}{1}{3}{3}{2}', '{3}{0}{3}{1}{3}{2}',
				'{3}{0}{3}{3}{1}{2}', '{3}{3}{0}{1}{3}{2}',
				'{3}{3}{0}{3}{1}{2}', '{3}{3}{3}{0}{1}{2}']
	res = 10 ** 6  # Just in case there were multiple families (there aren't)
	for pattern in patterns:
		for A in range(10):
			if pattern[1] == '0' and A == 0:
				continue
			for B in range(10):
				for C in [1, 3, 7, 9]:
					tmin = 1 if pattern[1] == '3' else 0
					non_primes = tmin
					pmin = int(pattern.format(A, B, C, tmin))
					for t in range(tmin, 10):
						p = int(pattern.format(A, B, C, t))
						if not p in primelist:
							non_primes += 1
							if non_primes > 2:
								break
					if non_primes == 2:
						res = min(res, pmin)
	return res

print(p51())