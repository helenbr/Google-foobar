from itertools import permutations
import math

def shortest_path(graph, start):
    n = len(graph)
    distances = [float("inf")] * n
    distances[start] = 0
    for i in range(n):
        for current_vertex in range(n):
          for neighbor in range(n):
              weight = graph[current_vertex][neighbor]
              new_distance = distances[current_vertex] + weight
              if new_distance < distances[neighbor]:
                  distances[neighbor] = new_distance
    return distances

def negative_cycle(distances):
    n = len(distances)
    distance = distances[0]
    for u in range(n):
        for v in range(n):
            weight = distances[u][v]
            if distance[u] + weight < distance[v]:
                return True
    return False

def get_time(perm, distances):
    time = 0
    time = time + distances[0][perm[0]]
    time = time + distances[perm[-1]][len(distances) - 1]
    for i in range(1, len(perm)):
        time = time + distances[perm[i - 1]][perm[i]]
    return time

def solution(times, times_limit):
    n = len(times)
    bunnies = [i for i in range(1, n - 1)]
    distances = []
    for node in range(len(times)):
        distances.append(shortest_path(times, node))
    if negative_cycle(distances):
        result = [i for i in range(n - 2)]
        return result
    for i in range(n - 2, 0, -1):
        for perm in permutations(bunnies, i):
            time = get_time(perm, distances)
            if time <= times_limit:
                return [x - 1 for x in sorted(perm)]

    return []