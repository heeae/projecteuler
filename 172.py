import functools

def countDigit(input):
    # y = [0] * 10
    # for x in input:
    #     y[int(x)] += 1
    #     if y[int(x)] >= 3:
    #         return False
    return True

@functools.cache
def calculate(total, current, num0, num1, num2, num3, num4, num5, num6, num7, num8, num9):
    sumtotal = 0
    if total == current:
        return 1
    if current > 0:
        if num0 < 3:
            sumtotal += calculate(total, current + 1, num0 + 1, num1, num2, num3, num4, num5, num6, num7, num8, num9)
    if num1 < 3:
        sumtotal += calculate(total, current + 1, num0, num1 + 1, num2, num3, num4, num5, num6, num7, num8, num9)
    if num2 < 3:
        sumtotal += calculate(total, current + 1, num0, num1, num2 + 1, num3, num4, num5, num6, num7, num8, num9)
    if num3 < 3:
        sumtotal += calculate(total, current + 1, num0, num1, num2, num3 + 1, num4, num5, num6, num7, num8, num9)
    if num4 < 3:
        sumtotal += calculate(total, current + 1, num0, num1, num2, num3, num4 + 1, num5, num6, num7, num8, num9)
    if num5 < 3:
        sumtotal += calculate(total, current + 1, num0, num1, num2, num3, num4, num5 + 1, num6, num7, num8, num9)
    if num6 < 3:
        sumtotal += calculate(total, current + 1, num0, num1, num2, num3, num4, num5, num6 + 1, num7, num8, num9)
    if num7 < 3:
        sumtotal += calculate(total, current + 1, num0, num1, num2, num3, num4, num5, num6, num7 + 1, num8, num9)
    if num8 < 3:
        sumtotal += calculate(total, current + 1, num0, num1, num2, num3, num4, num5, num6, num7, num8 + 1, num9)
    if num9 < 3:
        sumtotal += calculate(total, current + 1, num0, num1, num2, num3, num4, num5, num6, num7, num8, num9 + 1)
    
    return sumtotal

print(calculate(18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))