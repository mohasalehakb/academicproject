import os
import time

class MazeSolverStack:
    def __init__(self, maze, start, end):
        self.maze = [row[:] for row in maze]  # ایجاد کپی برای تغییرات
        self.start = start
        self.end = end
        self.visited = set()

    def solve(self):
        stack = [self.start]
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # راست، پایین، چپ، بالا

        while stack:
            x, y = stack.pop()
            if (x, y) == self.end:
                self.maze[x][y] = 'E'  # علامت پایان مسیر
                self.show_maze()
                return True

            if (x, y) in self.visited:
                continue

            self.visited.add((x, y))
            self.maze[x][y] = '*'  # مسیر طی‌شده
            self.show_maze()

            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(self.maze) and 0 <= ny < len(self.maze[0]) and self.maze[nx][ny] == 0:
                    stack.append((nx, ny))

            time.sleep(0.5)  # وقفه برای مشاهده تغییرات

        return False

    def show_maze(self):
        for row in self.maze:
            print(" ".join(map(str, row)))
        print("\n" + "-" * 20)

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

    start = (0, 1)  # نقطه شروع
    end = (7, 7)  # نقطه پایان

    solver = MazeSolverStack(maz, start, end)
    if solver.solve():
        print("مسیر پیدا شد!")
    else:
        print("مسیر یافت نشد!")

if __name__ == "__main__":
    main()

# دستورات Git
os.system('git add .')
os.system('git commit -m "Auto commit"')
os.system('git push')
