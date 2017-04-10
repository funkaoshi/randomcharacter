import itertools
import math
import random

import mixins
import dice


class Speed(object):
    NORMAL = "normal"



class Character(object):

    def __init__(self, *args, **kwargs):
        # super(Character, self).__init__(*args, **kwargs)

        # Step 0 - Base
        self.speed = Speed.NORMAL
        self.defence = 10
        self.allegiance = 0
        self.languages = ['Low Speech']
        self.gear = ['a Functional Outfit', 'a Standard Weapon']
        self.gp = dice.d(20)

        # Step 1 - Calling
        self.calling_name = random.choice(self.CALLINGS.keys())
        self.calling = self.CALLINGS[self.calling_name]

        self.hearts = self.calling.HEARTS
        self.attack_bonus = self.calling.AB

        # Step 2 - Species
        self.species = random.choice(self.SPECIES)

        # Step 3 - Origin
        self.homeland = random.choice(self.HOMELAND)
        self.homeland_name = self.homeland[0]
        self.languages.append(random.choice(self.homeland[1]))

        # Step 4 - Trait
        self.traits = self.calling.TRAITS
        self.traits[random.choice(self.TRAITS)] += 1
        self.traits[random.choice(self.TRAITS)] += 1
        self.traits[random.choice(self.TRAITS)] -= 1

        # Step 5 - Quirk


    TRAITS = [
        'Might',
        'Deftness',
        'Grit',
        'Insight',
        'Aura',
    ]

    class Factotum(object):
        AB = 0
        HEARTS = 2
        TRAITS = {
            'Might': 7,
            'Deftness': 9,
            'Grit': 8,
            'Insight': 9,
            'Aura': 9,
        }
        INT = 3

    class Sneak(object):
        AB = 0
        HEARTS = 2
        TRAITS = {
            'Might': 7,
            'Deftness': 10,
            'Grit': 7,
            'Insight': 10,
            'Aura': 8,
        }
        INT = 3

    class Champion(object):
        AB = 1
        HEARTS = 3
        TRAITS = {
            'Might': 9,
            'Deftness': 9,
            'Grit': 9,
            'Insight': 8,
            'Aura': 7,
        }
        INT = 3

    class BattlePrincess(object):
        AB = 1
        HEARTS = 3
        TRAITS = {
            'Might': 8,
            'Deftness': 8,
            'Grit': 9,
            'Insight': 7,
            'Aura': 10,
        }
        INT = 3

    class MurderPrincess(object):
        AB = 1
        HEARTS = 3
        TRAITS = {
            'Might': 8,
            'Deftness': 7,
            'Grit': 10,
            'Insight': 8,
            'Aura': 9,
        }
        INT = 3

    class Sage(object):
        AB = 0
        HEARTS = 2
        TRAITS = {
            'Might': 6,
            'Deftness': 8,
            'Grit': 8,
            'Insight': 10,
            'Aura': 8,
        }
        INT = 3

    class Heretic(object):
        AB = 0
        HEARTS = 2
        TRAITS = {
            'Might': 7,
            'Deftness': 7,
            'Grit': 10,
            'Insight': 7,
            'Aura': 9,
        }
        INT = 3

    class Fairy(object):
        AB = 1
        HEARTS = 3
        TRAITS = {
            'Might': 9,
            'Deftness': 9,
            'Grit': 9,
            'Insight': 8,
            'Aura': 7,
        }
        INT = 3

        ORIGINS = ['Petal Sprite', 'Imp', 'Pixie', 'Little Ghost']

    class Immortal(object):
        AB = 1
        HEARTS = 3
        TRAITS = {
            'Might': 9,
            'Deftness': 9,
            'Grit': 9,
            'Insight': 8,
            'Aura': 7,
        }
        INT = 3

        ORIGINS = ['The Celestial', 'Forgotten Legend', 'Elemental Weapon', 'Sealed Overlord']

    class Obake(object):
        AB = 1
        HEARTS = 3
        TRAITS = {
            'Might': 10,
            'Deftness': 8,
            'Grit': 7,
            'Insight': 9,
            'Aura': 8,
        }
        INT = 3

        ORIGINS = ['Blue Water Wanderer', 'Still Winds Dweller', 'Spirit Hunter', 'Part-Time Courier']

    class WarMechanoid(object):
        AB = 1
        HEARTS = 3
        TRAITS = {
            'Might': 9,
            'Deftness': 9,
            'Grit': 9,
            'Insight': 9,
            'Aura': 5,
        }
        INT = 3

        ORIGINS = ['You are a robot?']

    CALLINGS = {
        'Factotum': Factotum,
        'Sneak': Sneak,
        'Champion': Champion,
        # 'Raider': Raider,
        'Battle Princess': BattlePrincess,
        'Murder Princess': MurderPrincess,
        'Sage': Sage,
        'Heretic': Heretic,
        'Fairy': Fairy,
        'Immortal': Immortal,
        'Obake': Obake,
        'War-Mechanoid': WarMechanoid
    }

    SPECIES = [
        'Human',
        'Human (Dimensional Stray)',
        'Chib',
        'Tenebrate',
        'Elf',
        'Rai-Neko',
        'Promethean',
        'Bruun',
        'Goblin',
        'Dwarf',
        'Bio-Mechanoid',
    ]

    HOMELAND = [
        ('Wistful Dark', ['High Akenian', 'Dark Tongue', 'Dream Call']),
        ('Blazing Garden', ['Bright Speech', 'Fade Song', 'Hoshi-Ban']),
        ('Twilight Meridian', ['Fade Song', 'Gleysian Code', 'Dark Tongue']),
        ('Buried Kingdoms', ['Under Warble', 'Creator Script', 'High Akenian']),
    ]



