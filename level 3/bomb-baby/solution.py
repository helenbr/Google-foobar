def solution(x, y):
    result = 0
    M = max(int(x), int(y))
    F = min(int(x), int(y))
    while M > 1 and F > 1:
        if M < F:
          M , F = F , M
        if M %  F == 0:
            return "impossible"
        result = result + M // F
        M  = M %  F
    result = result + max(M, F) - 1
    return str(result)