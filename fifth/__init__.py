from dice import d
from fifth.backgrounds import Background
from fifth.race import Race
from fifth.processor import CharacterProcessor


class Attributes(CharacterProcessor):
    """ Takes an empty character and adds D&D attributes. """

    def roll_attribute(self):
        """ 4d6 drop the lowest """
        return sum(sorted(d(6) for _ in xrange(4))[1:])

    def process(self):
        # add attribute scores to the character
        self.character.attributes = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        self.character.scores = dict((a, self.roll_attribute())
                                     for a in self.character.attributes)



class Bonuses(CharacterProcessor):
    def get_bonus(self, score):
        """ returns D&D next ability score bonuses """
        return int(-5 + score / 2)

    def process(self):
        """ Compute bonuses based on ability scores. """
        self.character.bonuses = dict((a, self.get_bonus(s))
                                      for a, s in self.character.scores.iteritems())


class Skills(CharacterProcessor):
    DEFAULT = [
        ('Acrobatics', 'DEX'),
        ('Animal Handling', 'WIS'),
        ('Arcana', 'INT'),
        ('Athletics', 'STR'),
        ('Deception', 'CHA'),
        ('History', 'INT'),
        ('Intimidation', 'CHA'),
        ('Medicine', 'WIS'),
        ('Nature', 'INT'),
        ('Perception', 'WIS'),
        ('Performance', 'CHA'),
        ('Persuasion', 'CHA'),
        ('Religion', 'INT'),
        ('Search', 'INT'),
        ('Sense Motive', 'WIS'),
        ('Sleight of Hand', 'DEX'),
        ('Stealth', 'DEX'),
        ('Survival', 'WIS'),
    ]

    def process(self):
        """ Calculates the characters skill scores. """

        self.character.skills = []
        for skill, attribute in Skills.DEFAULT:
            score = self.character.bonuses[attribute]
            if skill in self.character.skill_proficiencies:
                score += self.character.profiency_bonus
            self.character.skills.append((skill, score))


class Character(object):
    """
    Builds a 5th Edition D&D Character
    """
    def __init__(self):
        self.system = '5e'
        self.class_name = ''
        self.hp = 0
        self.profiency_bonus = 2 # first level
        self.features = set()
        self.proficiencies = set()
        self.skill_proficiencies = set()
        self.tool_proficiencies = set()
        self.languages = set()
        self.equipment = []

        processors = [Attributes, Race, Bonuses, Background, Skills]

        for processor in processors:
            processor(self).process()
