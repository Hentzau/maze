'''
1. Initialize maze - x * y
2. All walls initially blocked off. How to signify wall?
3. Start on an edge. Need edge detection.
4. Pick a direction containing an unvisited cell.
5. Move that way.
6. Add cell to list of visited cells.
7. If no unvisited cells availble, backtrack by popping the last item off the list.
8. Continue until all cells visited.
'''
import random


class MazeCell(object):
    def __init__(self, x, y, directions):
        self.coords = (x, y)
        self.directions = directions
        self.unvisited_adjacent_cells = [(x+a, y+b) for (a, b) in self.directions]
        self.picked_directions = []

    def pick_direction(self):
        direction = random.choice(self.unvisited_adjacent_cells)
        self.picked_directions.append(direction)
        return direction

    def remove_adjacent_visited_cell(self, coords):
        self.unvisited_adjacent_cells = [x for x in self.unvisited_adjacent_cells if x != coords]


class Maze(object):
    def __init__(self, max_x, max_y):
        self.maze_dict = {}

        for x in range(max_x):
            for y in range(max_y):
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                if x == 0 or x == max_x or y == 0 or y == max_y:
                    directions = [(x + direction[0], y + direction[1]) for direction in directions
                                        if 0 < direction[0] + x < max_x and 0 < direction[1] + y < max_y]

                self.maze_dict[(x, y)]=MazeCell(x, y, directions)
        # maze_container = [[MazeCell(x, y) for x in range(max_x)] for y in range(max_y)]
        self.path = []
        self.start_cell = random.choice([(0, 0), (max_x, 0), (0, max_y), (max_x, max_y)])

    def remove_cell_possibilities(self, visited_cell):
        for coords in [(visited_cell.coords[0] + direction[0], visited_cell.coords[1] + direction[1]) for direction
                        in visited_cell.directions]:
            self.maze_dict[coords].remove_adjacent_visited_cell(visited_cell.coords)

    def generate(self):
        self.path.append(self.maze_dict[self.start_cell])
        while self.path:
            current_cell = self.path[-1]
            # remove_cell_possibilities needs to go here for the first cell
            if len(current_cell.unvisited_adjacent_cells):
                direction = current_cell.pick_direction()
                self.path.append(self.maze_dict[direction])
                self.remove_cell_possibilities(self.maze_dict(direction))
            else:
                self.path.pop()


