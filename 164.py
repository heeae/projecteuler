import functools

@functools.cache
def calculate(total, current, pos2, pos1):
    sumtotal = 0
    if total == current:
        return 1
    if current == 0:
        for d in range(1, 10):
            if 0 <= pos2 + pos1 + d <= 9:
                sumtotal += calculate(total, current + 1, pos1, d)
    else:
        for d in range(0, 10):
            if 0 <= pos2 + pos1 + d <= 9:
                sumtotal += calculate(total, current + 1, pos1, d)
    return sumtotal

print(calculate(18, 0, 0, 0, 0))