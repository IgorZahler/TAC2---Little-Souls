# src/puzzle.py
import pygame

class Puzzle:
    def __init__(self, puzzle_type, solution):
        self.puzzle_type = puzzle_type
        self.solution = solution
        self.is_solved = False
        self.user_input = []

    def update(self, events):
        if not self.is_solved:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    self.user_input.append(event.unicode)
                    if "".join(self.user_input) == self.solution:
                        self.is_solved = True
                        print("Puzzle resolvido!")
                        break
                    elif not "".join(self.user_input).startswith(self.solution):
                        self.user_input = []

    def draw(self, screen):
        if not self.is_solved:
            pygame.draw.rect(screen, (0, 0, 255), (300, 100, 200, 100))
            font = pygame.font.Font(None, 36)
            text = font.render("Resolva o puzzle", True, (255, 255, 255))
            screen.blit(text, (320, 220))
