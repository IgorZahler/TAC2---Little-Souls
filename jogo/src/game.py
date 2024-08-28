# src/game.py
import pygame
from src.player import Player
from src.environment import Environment
from src.boss import Boss
from src.main_menu import MainMenu

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = "menu"  # Estado inicial como menu
        self.main_menu = MainMenu(screen)
        self.player = None
        self.environment = None
        self.boss = None

    def start_new_game(self):
        self.player = Player()
        self.environment = Environment()
        self.boss = self.create_boss()
        self.state = "playing"

    def create_boss(self):
        boss_data = [
            {"name": "Forest Guardian", "health": 100, "position": (580, 480), "weaknesses": ["fire"]},
            {"name": "Desert Pharaoh", "health": 120, "position": (500, 480), "weaknesses": ["ice"]},
            {"name": "Ice King", "health": 150, "position": (500, 480), "weaknesses": ["fire"]},
        ]
        return Boss(**boss_data[self.environment.current_biome])

    def update(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if self.state == "menu":
            action = self.main_menu.update(events)
            if action == "start_game":
                self.start_new_game()
            elif action == "load_game":
                self.load_game()  # Implementar a lógica de carregar o jogo posteriormente
            elif action == "exit":
                pygame.quit()
                exit()
        elif self.state == "playing":
            self.player.update(self.environment)
            self.environment.update()
            self.boss.update(self.player)  # Passando o jogador para o boss

            keys = pygame.key.get_pressed()
            if keys[pygame.K_b]:
                self.boss.take_damage(100, "fire")
                if not self.boss.is_alive:
                    self.environment.change_biome()
                    self.boss = self.create_boss()

    def draw(self):
        if self.state == "menu":
            self.main_menu.draw()
        elif self.state == "playing":
            self.screen.fill((0, 0, 0))
            self.environment.draw(self.screen)
            self.player.draw(self.screen)
            self.boss.draw(self.screen)
