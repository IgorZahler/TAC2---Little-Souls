# src/arrow.py
import pygame

class Arrow:
    def __init__(self, player):
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))  # Cor vermelha para a flecha
        self.rect = self.image.get_rect()
        self.speed = 10
        self.active = False
        self.direction = None
        self.player = player

    def shoot(self, direction):
        if not self.active:  # Ativa a flecha se ela não estiver ativa
            self.active = True
            self.direction = direction
            self.rect.center = self.player.rect.center

    def update(self):
        if self.active:
            if self.direction == "left":
                self.rect.x -= self.speed
            elif self.direction == "right":
                self.rect.x += self.speed

            # Se a flecha sair da tela, desative-a
            if self.rect.right < 0 or self.rect.left > 800 or self.rect.bottom < 0 or self.rect.top > 600:
                self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, self.rect)

    def reset(self):
        self.active = False
