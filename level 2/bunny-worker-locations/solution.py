def solution(x, y):
	corner = x + y - 1
	id = corner * (corner + 1) // 2
    id = id - y + 1
    return str(id)