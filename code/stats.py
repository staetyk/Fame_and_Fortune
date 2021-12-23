import pickle, os.path

#default stats for a character
stats = {
    "Max HP" : 10,
    "HP" : 10,
    "HP Regen" : 1,
    "Max SP" : 0,
    "SP" : 0,
    "SP Regen" : 0,
    "Damage" : 1,
    "Attack Speed" : 1,
    "Armor" : 0.1,
    "Critical Hit" : 0.25,
    "Combo" : 0,
    "Accuracy" : 0.5,
    "Vulnerability" : 0.5,
    "Scavenge" : 0.5,
    "Rarity" : 0,
    "Inventory Space" : 30,
    "Buffs" : [],
    "Debuffs" : [],
    "Effects Given" : [],
    "Medicine" : 0.2,
    "Sickness" : 1,
    "Level" : 1,
    "XP" : 0,
    "XP Earn" : 5,
    "Level Up" : 50,
    "Rings" : {
        "Race" : None,
        "Class" : None
    }
}


#equation is lambda
def change(stat: str, equation):
    global stats
    x = stats[stat]
    y = ceil(equation(x))
    stats.update({stat:y})