# src/environment.py
import pygame

class Environment:
    def __init__(self):
        self.current_biome = 0
        self.biomes = [self.create_forest(), self.create_desert(), self.create_ice()]
        self.current_elements = self.biomes[self.current_biome]

    def create_forest(self):
        # Elementos do bioma floresta
        piso = [
            pygame.Rect(0,580,900,40) #piso do mapa
        ]
        obstacles = [
            pygame.Rect(200, 560, 100, 20),  # Tronco caído
            pygame.Rect(400, 550, 50, 50),   # Arbusto
        ]
        traps = [
            pygame.Rect(350, 560, 30, 30),  # Armadilha de espinhos
        ]
        return {"background": (34, 139, 34), "obstacles": obstacles, "traps": traps, "piso": piso}

    def create_desert(self):
        # Elementos do bioma deserto
        obstacles = [
            pygame.Rect(100, 560, 120, 20),  # Duna de areia
            pygame.Rect(450, 550, 60, 60),   # Cacto
        ]
        traps = [
            pygame.Rect(300, 560, 30, 30),  # Armadilha de areia movediça
        ]
        piso = [
            pygame.Rect(0,580,900,40) #piso do mapa
        ]
        return {"background": (210, 180, 140), "obstacles": obstacles, "traps": traps, "piso": piso}

    def create_ice(self):
        # Elementos do bioma gelo
        obstacles = [
            pygame.Rect(150, 560, 100, 20),  # Bloco de gelo
            pygame.Rect(500, 550, 70, 70),   # Estalagmite
        ]
        traps = [
            pygame.Rect(250, 560, 30, 30),  # Armadilha de gelo quebradiço
        ]
        piso = [
            pygame.Rect(0,580,900,40) #piso do mapa
        ]
        return {"background": (173, 216, 230), "obstacles": obstacles, "traps": traps, "piso": piso}

    def change_biome(self):
        # Altera o bioma após derrotar um boss
        self.current_biome = (self.current_biome + 1) % len(self.biomes)
        self.current_elements = self.biomes[self.current_biome]

    def update(self):
        # Atualiza os elementos do cenário
        pass

    def draw(self, screen):
        # Desenha o fundo do bioma
        screen.fill(self.current_elements["background"])

        # Desenha os obstáculos
        for obstacle in self.current_elements["obstacles"]:
            pygame.draw.rect(screen, (150, 69, 19), obstacle)  # Obstáculos marrons

        # Desenha as armadilhas
        for trap in self.current_elements["traps"]:
            pygame.draw.rect(screen, (255, 0, 0), trap)  # Armadilhas vermelhas

        # Desenha o piso do mapa
        for trap in self.current_elements["piso"]:
            pygame.draw.rect(screen, (128, 128, 128), trap)  # piso cinza

