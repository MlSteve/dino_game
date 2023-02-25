import sys

import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 0
        self.points = 0
        self.font = pygame.font.Font(r"assets/fonts/gamefont.ttf", 20)
        self.image = self.font.render(f"Score {self.points}", True, (83, 83, 83))
        self.rect = self.image.get_rect()
        self.surface = pygame.display.get_surface()
        self.rect.bottomleft = (self.surface.get_width()/1.5, self.surface.get_height()/10)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.step += 1
        if self.step % 10 == 0:
            self.points += 1
            self.image = self.font.render(f"Score {self.points}", True, (83, 83, 83))


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load(r"assets/images/reset.png")
        self.rect1 = self.image1.get_rect()
        self.font = pygame.font.Font(r"assets/fonts/gamefont.ttf", 20)
        self.image2 = self.font.render(f"G A M E   O V E R", True, (83, 83, 83))
        self.rect2 = self.image2.get_rect()
        self.surface = pygame.display.get_surface()
        self.rect2.center = (self.surface.get_width() / 2, self.surface.get_height() / 4)
        self.rect1.center = (self.surface.get_width() / 2, self.surface.get_height() / 2.8)

    def over(self, func):
        clock = pygame.time.Clock()
        while True:
            clock.tick(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                func()

    def draw(self, surface):
        surface.blit(self.image1, self.rect1)
        surface.blit(self.image2, self.rect2)
