class Snake:

    def __init__(self):
        self.body = [(10,10), (10,9), (10,8)]
        self.growing = False

    def move(self, next_pos):
        self.body.insert(0, next_pos)

        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def grow(self):
        self.growing = True

    def get_head(self):
        return self.body[0]

    def collision(self):
        head = self.get_head()
        return head in self.body[1:]

    def draw(self, screen):
        import pygame
        from settings import CELL_SIZE, GREEN

        for segment in self.body:
            rect = pygame.Rect(
                segment[0] * CELL_SIZE,
                segment[1] * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(screen, GREEN, rect)