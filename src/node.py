class Node:

    id = -1
    pai = None
    profundidade = None
    value = 0
    x = 0
    y = 0

    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y