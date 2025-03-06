import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Procedural Color Grid (Regenerates every 5 seconds)")


def generate_grid():
    return [[(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
             for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


grid = generate_grid()
REGEN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(REGEN_EVENT, 5000)
running = True
while running:
    screen.fill((0, 0, 0))

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[y][x],
                             (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == REGEN_EVENT:
            grid = generate_grid()

pygame.quit()
