import functools

@functools.cache
def calculate(date,  absent, late):
    sumtotal = 0
    if absent >= 3:
        return 0
    if late > 1:
        return 0
    if date == 0:
        return 1
    sumtotal += calculate(date - 1, 0, late)
    sumtotal += calculate(date - 1, absent + 1, late)
    sumtotal += calculate(date - 1, 0, late + 1)
    
    return sumtotal

print(calculate(30, 0, 0))