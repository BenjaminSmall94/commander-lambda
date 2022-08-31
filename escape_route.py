def solution(map):
    path_distance = [1]
    min_distance = [max(len(map), len(map[0])) ** 2]
    visited = [[False for _ in range(len(map[0]))] for i in range(len(map))]
    walk(map, 0, 0, False, path_distance, min_distance, visited)
    return min_distance[0]


def walk(map, row, col, moved_wall, path_distance, min_distance, visited):
    if row == len(map) - 1 and col == len(map[0]) - 1:
        if path_distance[0] < min_distance[0]:
            min_distance[0] = path_distance[0]
    else:
        if row < len(map) - 1 and not visited[row + 1][col] and (map[row + 1][col] == 0 or not moved_wall):
            path_distance[0] += 1
            visited[row + 1][col] = True
            if map[row + 1][col] == 1:
                walk(map, row + 1, col, True, path_distance, min_distance, visited)
            else:
                walk(map, row + 1, col, moved_wall, path_distance, min_distance, visited)
            visited[row + 1][col] = False
            path_distance[0] -= 1
        if col < len(map[0]) - 1 and not visited[row][col + 1] and (map[row][col + 1] == 0 or not moved_wall):
            path_distance[0] += 1
            visited[row][col + 1] = True
            if map[row][col + 1] == 1:
                walk(map, row, col + 1, True, path_distance, min_distance, visited)
            else:
                walk(map, row, col + 1, moved_wall, path_distance, min_distance, visited)
            visited[row][col + 1] = False
            path_distance[0] -= 1
        if row > 0 and not visited[row - 1][col] and (map[row - 1][col] == 0 or not moved_wall):
            path_distance[0] += 1
            visited[row - 1][col] = True
            if map[row - 1][col] == 1:
                walk(map, row - 1, col, True, path_distance, min_distance, visited)
            else:
                walk(map, row - 1, col, moved_wall, path_distance, min_distance, visited)
            visited[row - 1][col] = False
            path_distance[0] -= 1
        if col > 0 and not visited[row][col - 1] and (map[row][col - 1] == 0 or not moved_wall):
            path_distance[0] += 1
            visited[row][col - 1] = True
            if map[row][col - 1] == 1:
                walk(map, row, col - 1, True, path_distance, min_distance, visited)
            else:
                walk(map, row, col - 1, moved_wall, path_distance, min_distance, visited)
            visited[row][col - 1] = False
            path_distance[0] -= 1


print(solution([[0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0]]))

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))