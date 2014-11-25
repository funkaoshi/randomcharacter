import random

from processor import CharacterProcessor

class Race(CharacterProcessor):
    def process(self):
        """ Pick the character's race, randomly. """
        self.character.race = random.choice(['Dwarf', 'Elf', 'Halfling', 'Human'])
        if self.character.race == 'Dwarf':
            self.character.scores['CON'] += 2
            self.character.speed = 25
            self.character.proficiencies.union(['battleaxe', 'handaxe', 'throwing hammer', 'warhammer'])
            self.character.tool_proficiencies.union(random.choice(["smith's tools", "brewer's supplies", "mason's tools"]))
            self.character.languages.add("Dwarvish")
            self.character.race = random.choice(['Hill Dwarf', 'Mountain Dwarf'])
            if self.character.race == 'Hill Dwarf':
                self.character.scores['WIS'] += 1
                self.character.hp += 1
            else:
                self.character.scores['STR'] += 2
                self.character.proficiencies.union(['light armour', 'medium armour'])
        elif self.character.race == 'Elf':
            self.character.scores['DEX'] += 2
            self.character.speed = 30
            self.character.proficiencies.union('Perception')
            self.character.languages.add('Elvish')
            self.character.race = random.choice(['High Elf', 'Wood Elf'])
        elif self.character.race == 'Halfling':
            self.character.scores['DEX'] += 2
            self.character.speed = 25
            self.character.proficiencies.add('Perception')
            self.character.languages.add('Halfling')
        else:
            for a in self.character.attributes:
                self.character.scores[a] += 1
            self.character.speed = 30
