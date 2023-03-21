def binary_to_decimal(n, b):
    result = 0
    for d in n:
      result = b * result + int(d)
    return result

def decimal_to_binary(n, b, k):
    result = ''
    while n > 0:
        d = n % b
        result = str(d) + result
        n = n // b
    return result.zfill(k)

def solution(n, b):
    k = len(n)
    array = []
    seen = set()
    while n not in array:
        array.append(n)
        seen.add(n)
        x = binary_to_decimal(sorted(n, reverse=True), b)
        y = binary_to_decimal(sorted(n), b)
        z = decimal_to_binary(x - y, b, k)
        if z == n:
            return 1
        n = z
        if n in seen:
            return len(array) - array.index(n)
    return len(array)

