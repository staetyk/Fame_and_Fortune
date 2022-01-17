import pygame


'''
stat: Max HP, HP Regen, Max SP, SP Regen, Damage, Attack Speed, Critical Hit, Effects Given, Armor, Accuracy, Vunerability, Buffs, Debuffs, Medicine, Sickness, XP, Position, Type
'''


class enemy:
    def __init__(self, stat: dict, texture: pygame.surface.Surface, dialogue: list[str] = []):
        self.position = stat["Position"]
        self.type = stat["Type"]
        stat.pop("Position")
        stat.pop("Type")

        stat.update({
            "HP" : stat["Max HP"],
            "SP" : stat["Max SP"],
            "Combo" : 0
        })

        self.stats = stat
        self.texture = pygame.transform.scale(texture, (100,100))
        self.dialogue = dialogue
        self.alive = True

        self.event = pygame.event.custom_type()