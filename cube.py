import numpy as np
from random import choice

def rotate(l, direction):
    if direction == 1:
        return np.transpose(np.flip(l, axis=1))
    if direction == -1:
        return np.flip(np.transpose(l), axis=1)

def listify(l):
    return list(map(list, l))

class Cube:
    def __init__(self, size: (int, int, int)):
        self.front = np.array([["W" for _ in range(size[0])] for __ in range(size[1])])
        self.back = np.array([["Y" for _ in range(size[0])] for __ in range(size[1])])
        self.top = np.array([["G" for _ in range(size[0])] for __ in range(size[2])])
        self.bottom = np.array([["B" for _ in range(size[0])] for __ in range(size[2])])
        self.left = np.array([["O" for _ in range(size[2])] for __ in range(size[1])])
        self.right = np.array([["R" for _ in range(size[2])] for __ in range(size[1])])
        self.solved = [l for l in map(listify, (self.front, self.back, self.top, self.bottom, self.left, self.right))]
    def checkSolution(self):
        return [l for l in map(listify, (self.front, self.back, self.top, self.bottom, self.left, self.right))] == self.solved
    def print(self):
        print(np.array([self.front, self.back, self.top, self.bottom, self.left, self.right]))

    def scramble(self, moves):
        ms = []
        for i in range(moves):
            move = choice(["front","back","top","bottom","left","right"]),choice((-1,1))
            self.rotate(move[0], move[1])
            ms.append(move)
        return ms

    def rotate(self, side: str, direction: int):
        if side == "front":
            if direction == -1:
                self.front = rotate(self.front,-1)
                buffer = list(self.top[0])
                self.top[0] = self.left[:,-1]
                self.left[:,-1] = self.bottom[0]
                self.bottom[0] = np.flip(self.right[:,0])
                self.right[:,0] = buffer

            elif direction == 1:
                self.front = rotate(self.front, 1)
                buffer = list(self.top[0])
                self.top[0] = self.right[:,0]
                self.right[:,0] = np.flip(self.bottom[0])
                self.bottom[0] = self.left[:,-1]
                self.left[:,-1] = buffer

        elif side == "back":
            if direction == 1:
                self.back = rotate(self.back,-1)
                buffer = list(self.top[-1])
                self.top[-1] = self.left[:,0]
                self.left[:,0] = self.bottom[-1]
                self.bottom[-1] = np.flip(self.right[:,-1])
                self.right[:,-1] = buffer

            elif direction == -1:
                self.back = rotate(self.back, 1)
                buffer = list(self.top[-1])
                self.top[-1] = self.right[:,-1]
                self.right[:,-1] = np.flip(self.bottom[-1])
                self.bottom[-1] = self.left[:,0]
                self.left[:,0] = buffer

        elif side == "top":
            if direction == 1:
                self.top = rotate(self.top, 1)
                buffer = list(self.front[0])
                self.front[0] = self.left[0]
                self.left[0] = self.back[0]
                self.back[0] = self.right[0]
                self.right[0] = buffer

            elif direction == -1:
                self.top = rotate(self.top, -1)
                buffer = list(self.front[0])
                self.front[0] = self.right[0]
                self.right[0] = self.back[0]
                self.back[0] = self.left[0]
                self.left[0] = buffer

        elif side == "bottom":
            if direction == -1:
                self.bottom = rotate(self.bottom, -1)
                buffer = list(self.front[-1])
                self.front[-1] = self.left[-1]
                self.left[-1] = self.back[-1]
                self.back[-1] = self.right[-1]
                self.right[-1] = buffer

            elif direction == 1:
                self.bottom = rotate(self.bottom, 1)
                buffer = list(self.front[-1])
                self.front[-1] = self.right[-1]
                self.right[-1] = self.back[-1]
                self.back[-1] = self.left[-1]
                self.left[-1] = buffer

        elif side == "left":
            if direction == 1:
                self.left = rotate(self.left, 1)
                buffer = list(self.front[:,0])
                self.front[:,0] = self.bottom[:,0]
                self.bottom[:,0] = np.flip(self.back[:,-1])
                self.back[:,-1] = self.top[:,-1]
                self.top[:,-1] = np.flip(buffer)

            elif direction == -1:
                self.left = rotate(self.left, -1)
                buffer = list(self.front[:,0])
                self.front[:,0] = np.flip(self.top[:,-1])
                self.top[:,-1] = self.back[:,-1]
                self.back[:,-1] = np.flip(self.bottom[:,0])
                self.bottom[:,0] = buffer

        elif side == "right":
            if direction == -1:
                self.right = rotate(self.right, 1)
                buffer = list(self.front[:,0])
                self.front[:,0] = self.bottom[:,0]
                self.bottom[:,0] = np.flip(self.back[:,-1])
                self.back[:,-1] = self.top[:,-1]
                self.top[:,-1] = np.flip(buffer)

            elif direction == 1:
                self.right = rotate(self.right, 1)
                buffer = list(self.front[:,0])
                self.front[:,0] = np.flip(self.top[:,-1])
                self.top[:,-1] = self.back[:,-1]
                self.back[:,-1] = np.flip(self.bottom[:,0])
                self.bottom[:,0] = buffer