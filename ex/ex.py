import os

class MazeSolverStack:
    def __init__(self, maze):
        self.maze = maze
        self.start = (0, 1)
        self.end = (7, 7)

    def move_maz(self, x, y):
        if self.maze[x][y] == 0:
            self.maze[x][y] = '*'  # نشان‌گذاری مسیر طی‌شده

    def start_max(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if i == 0 or i == 7 or j == 0 or j == 7:
                    if (i, j) != self.end:
                        self.move_maz(i, j)

def main():
    maz = [
        [0,0,0,0,0,0,1,1],
        [1,1,1,0,1,1,1,1],
        [1,1,1,0,0,0,1,1],
        [1,0,0,0,1,1,1,1],
        [1,0,1,0,1,1,1,1],
        [1,0,1,0,0,0,1,1],
        [1,0,1,1,1,0,1,1],
        [1,1,1,1,1,0,0,0]
    ]

    solver = MazeSolverStack(maz)
    solver.start_max()

    # نمایش هزار‌تو
    for row in maz:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()

# دستورات Git
os.system('git add .')
os.system('git commit -m "Auto commit"')
os.system('git push')
