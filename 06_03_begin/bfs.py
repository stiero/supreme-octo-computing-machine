"""
Python Data Structures - A Game-Based Approach
BFS maze solver.
Robin Andrews - https://compucademy.net/
The queue contains positions as (row, column) tuples. Predecessors are kept in a dictionary.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from queue_ll import Queue


def bfs(maze, start, goal):
    
    # Initialise    
    q = Queue()
    q.enqueue(start)
    predecessors = {start: None}
    
    # Iteration
    while not q.is_empty():
        current_step = q.dequeue()
        #print(predecessors)
        
        # Terminate here
        if current_step == goal:
            print(predecessors)

            return get_path(predecessors, start, goal)
        
        # Discover neighbours
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_step[0] + row_offset, current_step[1] + col_offset)
            #print(neighbour)
            
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors.keys():
                q.enqueue(neighbour)
                predecessors[neighbour] = current_step
    

if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None
