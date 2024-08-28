# src/boss.py
import pygame
import random

class Boss:
    def __init__(self, name, health, position, weaknesses):
        self.name = name
        self.health = health
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], 100, 100)
        self.weaknesses = weaknesses
        self.current_pattern = 0
        self.attack_patterns = self.create_attack_patterns()
        self.is_alive = True
        self.attack_timer = 0  # Timer para controlar os ataques

    def create_attack_patterns(self):
        # Defina padrões de ataque mais diversificados
        patterns = [
            {"type": "melee", "damage": 20, "interval": 2000, "duration": 500},
            {"type": "range", "damage": 10, "interval": 1500, "duration": 1000},
            {"type": "area", "damage": 15, "interval": 2500, "duration": 1500},
        ]
        return patterns

    def take_damage(self, damage, element):
        if element in self.weaknesses:
            self.health -= damage * 2
        else:
            self.health -= damage

        if self.health <= 0:
            self.die()

    def die(self):
        self.is_alive = False
        print(f"{self.name} foi derrotado!")

    def update(self, player):
        if not self.is_alive:
            return

        self.attack_timer += pygame.time.get_ticks()
        pattern = self.attack_patterns[self.current_pattern]

        if self.attack_timer >= pattern["interval"]:
            self.attack(player, pattern)
            self.attack_timer = 0
            self.current_pattern = (self.current_pattern + 1) % len(self.attack_patterns)

    def attack(self, player, pattern):
        if pattern["type"] == "melee":
            if self.rect.colliderect(player.rect):
                player.respawn()

        elif pattern["type"] == "range":
            # Lógica para ataque à distância
            projectile = pygame.Rect(self.rect.centerx, self.rect.centery, 10, 10)
            # pygame.draw.rect(self.rect, (0, 255, 0), projectile)  # Desenha um projétil
            if projectile.colliderect(player.rect):
                player.respawn()

        elif pattern["type"] == "area":
            # Lógica para ataque em área
            area = pygame.Rect(self.rect.x - 50, self.rect.y - 50, 200, 200)
            # pygame.draw.rect(self.rect, (255, 0, 0), area)  # Desenha a área de ataque
            if area.colliderect(player.rect):
                player.respawn()

    def draw(self, screen):
        if self.is_alive:
            pygame.draw.rect(screen, (255, 0, 0), self.rect)
