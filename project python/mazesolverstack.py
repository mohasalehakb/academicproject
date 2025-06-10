import os
#######################################################################################################################

class MazeSolverStack:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.stack = [start]
        self.visited = set()
        self.parent = {}
        self.moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def solve(self):
        while self.stack:
            x, y = self.stack.pop()
            if (x, y) in self.visited:
                continue
            self.visited.add((x, y))

            if (x, y) == self.end:
                break

            for dx, dy in self.moves:
                nx, ny = x + dx, y + dy
                if (0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]) and
                    self.maze[nx][ny] != 1 and (nx, ny) not in self.visited):
                    self.stack.append((nx, ny))
                    self.parent[(nx, ny)] = (x, y)

        cur = self.end
        while cur != self.start:
            if cur not in self.parent:
                return
            if cur != self.end:
                x, y = cur
                self.maze[x][y] = '*'
            cur = self.parent[cur]

    def print_maze(self):
        for i, row in enumerate(self.maze):
            line = ""
            for j, val in enumerate(row):
                if (i, j) == self.start:
                    line += "s "
                elif (i, j) == self.end:
                    line += "e "
                else:
                    line += str(val) + " "
            print(line.strip())


def main():
    maz = [
        [0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0]
    ]

    start = (0, 0)
    end = (7, 7)
    solver = MazeSolverStack(maz, start, end)
    solver.solve()
    solver.print_maze()

if __name__ == "__main__":
    main()


#######################################################################################################################
os.system('git add .')
os.system('git commit -m "Auto commit"')
os.system('git push')
