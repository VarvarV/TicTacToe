import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGTH = 640, 480
FPS = 30

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.cross_zero = 0

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size, self.cell_size), 1)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        x = cell[0]
        y = cell[1]
        if self.board[y][x] == 1:
            return None
        self.board[y][x] = 1
        if self.cross_zero == 0:
            pygame.draw.circle(screen, pygame.Color("red"),
                               (int(x * self.cell_size + self.left + self.cell_size / 2),
                                int(y * self.cell_size + self.top + self.cell_size / 2)),
                               int(self.cell_size / 2) - 4, 2)
        else:
            pygame.draw.line(screen, pygame.Color("blue"),
                               (x * self.cell_size + self.left + 2,
                                y * self.cell_size + self.top + 2),
                                (x * self.cell_size + self.left + self.cell_size - 4,
                                y * self.cell_size + self.top + self.cell_size - 4), 2)
            pygame.draw.line(screen, pygame.Color("blue"),
                             (x * self.cell_size + self.left + 2,
                              y * self.cell_size + self.top + self.cell_size - 4),
                             (x * self.cell_size + self.left + self.cell_size - 4,
                              y * self.cell_size + self.top + 2), 2)
        self.cross_zero = 1 - self.cross_zero

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


board = Board(5, 7)
board.set_view(100, 100, 50)
board.render()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    pygame.display.flip()
pygame.quit()
