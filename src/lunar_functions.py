
def ladd(a, b):
    """
    ladd(int a, int b) => int
    conducts lunar addition on a and b
    """
    astr = str(a)[::-1]
    bstr = str(b)[::-1]
    retstr = ""
    if len(astr) < len(bstr):
        smaller = astr
        bigger = bstr
    else:
        smaller = bstr
        bigger = astr
    i = 0
    while i < len(smaller):
        if smaller[i] < bigger[i]:
            retstr = bigger[i] + retstr
        else:
            retstr = smaller[i] + retstr
        i += 1
    retstr = bigger[i:] + retstr
    return int(retstr)


def lsum(*nums):
    """
    lsum(int a, int b, ...) => int
    obtains the lunar sum of input values
    """
    total = nums[0]
    for num in nums[1:]:
        total = ladd(total, num)
    return total


def lmul(a, b):
    """
    lmul(int a , int b) => int
    conducts lunar multiplication on a and b
    """
    astr = str(a)[::-1]
    bstr = str(b)[::-1]
    retstr = ""
    i = 0
    vals = []
    while i < len(bstr):
        current_val = ""
        for val in astr:
            if val > bstr[i]:
                current_val += bstr[i]
            else:
                current_val += val
        vals.append(current_val[::-1] + ("0" * i))
        i += 1
    retstr = str(lsum(*[int(x) for x in vals]))
    return int(retstr)


def lpow(a, b):
    """
    lpow(int a, int b) => int
    raises a to the lunar power of b
    """
    acc = a
    for val in range(b - 1):
        acc = lmul(acc, a)
    return acc
