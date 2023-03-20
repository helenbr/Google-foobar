def solution(x):
    decoded = []
    for i in range(len(x)):
        if 'a' <= x[i] <= 'z':
            decoded.append(chr(2*ord('a') + 25 - ord(x[i])))
        else:
            decoded.append(x[i])
    return ''.join(decoded)