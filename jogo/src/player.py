# src/player.py
import pygame
from src.arrow import Arrow

class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))  # Cor do jogador
        self.rect = self.image.get_rect()
        self.rect.center = (30, 550)
        self.velocity = 5
        self.arrow = Arrow(self)
        self.last_checkpoint = self.rect.center  # Save-point

    def update(self, environment):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.velocity

        # Disparar a flecha
        if keys[pygame.K_SPACE]:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.arrow.shoot("left")
                self.rect.x += self.velocity
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.arrow.shoot("right")
                self.rect.x -= self.velocity

        # Verificar colisão com armadilhas
        for trap in environment.current_elements["traps"]:
            if self.rect.colliderect(trap):
                self.respawn()

        # Verificar colisão com obstáculos (impedindo o movimento)
        for obstacle in environment.current_elements["obstacles"]:
            if self.rect.colliderect(obstacle):
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.rect.x += self.velocity
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.rect.x -= self.velocity
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.rect.y += self.velocity
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.rect.y -= self.velocity

        self.arrow.update()
        
        # Verificar colisão com o piso (impedindo de cair)
        for obstacle in environment.current_elements["piso"]:
            if self.rect.colliderect(obstacle):
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.rect.x += self.velocity
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.rect.x -= self.velocity
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.rect.y += self.velocity
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.rect.y -= self.velocity

        self.arrow.update()

    def attack_boss(self, boss):
        if self.arrow.rect.colliderect(boss.rect):
            boss.take_damage(20, "fire")  # Supondo que a flecha seja de fogo

    def respawn(self):
        # Retorna o jogador para o último checkpoint
        self.rect.center = self.last_checkpoint

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.arrow.draw(screen)
