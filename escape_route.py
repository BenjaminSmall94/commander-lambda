# Implements a breadth first traversal to ensure that method returns and stops looking when the shortest path is found
# Visited array represents spaces on the map; 0: unvisited, 1: visited after moving wall, 2: visited before moving wall
# Therefore if visited[i][j] <= not_move_wall than the current cell should consider moving into it
def solution(map):
    visited = [[0 for _ in range(len(map[0]))] for i in range(len(map))]
    search_queue = Queue()
    visited[0][0] = 2 - map[0][0]
    return walk(map, 0, 0, bool(1 - map[0][0]), 1, visited, search_queue)


def walk(map, row, col, not_moved_wall, distance_traveled, visited, search_queue):
    if row == len(map) - 1 and col == len(map[0]) - 1:
        return distance_traveled
    else:
        if row < len(map) - 1 and visited[row + 1][col] <= not_moved_wall and (map[row + 1][col] == 0 or not_moved_wall):
            visited[row + 1][col] = not_moved_wall + 1
            if map[row + 1][col] == 1:
                search_queue.enqueue((row + 1, col, False, distance_traveled + 1))
            else:
                search_queue.enqueue((row + 1, col, not_moved_wall, distance_traveled + 1))
        if col < len(map[0]) - 1 and visited[row][col + 1] <= not_moved_wall and (map[row][col + 1] == 0 or not_moved_wall):
            visited[row][col + 1] = not_moved_wall + 1
            if map[row][col + 1] == 1:
                search_queue.enqueue((row, col + 1, False, distance_traveled + 1))
            else:
                search_queue.enqueue((row, col + 1, not_moved_wall, distance_traveled + 1))
        if row > 0 and visited[row - 1][col] <= not_moved_wall and (map[row - 1][col] == 0 or not_moved_wall):
            visited[row - 1][col] = not_moved_wall + 1
            if map[row - 1][col] == 1:
                search_queue.enqueue((row - 1, col, False, distance_traveled + 1))
            else:
                search_queue.enqueue((row - 1, col, not_moved_wall, distance_traveled + 1))
        if col > 0 and visited[row][col - 1] <= not_moved_wall and (map[row][col - 1] == 0 or not_moved_wall):
            visited[row][col - 1] = not_moved_wall + 1
            if map[row][col - 1] == 1:
                search_queue.enqueue((row, col - 1, False, distance_traveled + 1))
            else:
                search_queue.enqueue((row, col - 1, not_moved_wall, distance_traveled + 1))
        while not search_queue.is_empty():
            next_tile = search_queue.dequeue()
            return walk(map, next_tile[0], next_tile[1], next_tile[2], next_tile[3], visited, search_queue)


# My own queue class because I am not sure if this Python environment has the collections module available for import.
# I built it for a coding challenge at my Coding Bootcamp Code Fellows. However, I can tell it will be useful here.
class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        pass

    def enqueue(self, value):
        self.size += 1
        new_node = Node(value)
        if(self.is_empty()):
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            self.size -= 1
            popped_node = self.front
            if self.front is self.rear:
                self.rear = None
            self.front = self.front.next
            popped_node.next = None
            return popped_node.value
        else:
            raise InvalidOperationError

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.front.value

    def is_empty(self):
        return self.front is None


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class TargetError(Exception):
    pass


class InvalidOperationError(Exception):
    pass


if __name__ == "__main__":
    print(solution([[0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0]]))

    print(solution([[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]))

    print(solution([[0, 0],
                    [0, 0]]))

    print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
