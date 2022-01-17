import pygame


class enemy:
    def __init__(self, stats: dict, texture: pygame.surface.Surface, dialogue: list[str] = []):
        self.position = stats["Position"]
        self.type = stats["Type"]
        stats.pop("Position")
        stats.pop("Type")
        self.stats = stats
        self.texture = pygame.transform.scale(texture, (100,100))
        self.dialogue = dialogue
        self.alive = True