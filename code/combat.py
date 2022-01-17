import pygame, stats, enemy, random


PlayerAttk = pygame.event.custom_type()
EnemyAttk = pygame.event.custom_type()

def chance(percent: float) -> bool:
    x = random.randrange(0.01, 1.01, 0.01)
    y = percent >= x
    return y


def attack(offense: dict, defense: dict):
    if chance(offense["Accuracy"]-defense["Vunerability"]):
        return (offense, defense)
    
    crit = (2 if chance(offense["Critical Hit"]) else 1)
    damage = offense["Combo"]//5*10+offense["Damage"]*crit*(1-defense["Armor"])
    
    # effects stuff; bow stuff; skill stuff

    x = min(defense["SP"], damage)
    defense["SP"] -= x
    damage -= x

    x = min(defense["HP"], damage)
    defense["HP"] -= x

    # give effects

    return (offense, defense)