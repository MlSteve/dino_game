import sys

import pygame
from sprites.road import Road

WIDTH = 700
HEIGHT = 500
FPS = 60

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Dino")
clock = pygame.time.Clock()

road = Road()
running = True

while running:
    # Частота обновления экрана/Screen refresh rate
    clock.tick(FPS)

    # События/Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Рендеринг/Rendering
    screen.fill((255, 255, 255))
    road.draw(screen)

    road.update()

    # Обновление экрана/Screen Refresh
    pygame.display.update()