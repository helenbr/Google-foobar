def solution(n):
    array = [0] * (n + 1)
    array[0] = 1
    for brick in range(1, n+1):
        for height in range(n, brick-1, -1):
            array[height] = array[height] + array[height - brick]
    result = array[-1] - 1
    return result