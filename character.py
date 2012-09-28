import copy
import operator
import random

import characterclass
from dice import d, xdy


class Character(object):
    """
    D&D characters are structurely quite similar. Common aspects of character
    creation are managed here. Subclasses for the different systems handle
    differences between the editions.
    """
    
    def __init__(self):
        self.attributes = [(attribute, xdy(3,6))
                           for attribute in characterclass.ATTRIBUTES]
        self.character_class = self.get_character_class()
        self.equipment = self.character_class['equipment'][xdy(3,6)-3]        
        self.hp = self.get_hp()
        if self.hp < 0:
            self.hp = 1
        self.ac = self.get_ac()
        self.thac9 = self.get_thac9()
        self.saves = self.get_saves()
        self.languages = self.get_languages()
        self.spell = self.get_spell()
        self.notes = self.get_notes()
        
        # attribute map to ease display in template
        self.attr = dict((attr, self.with_bonus(attr, value))
                          for attr, value in self.attributes)
                          
    @property
    def system(self):
        raise NotImplementedError()
        
    @property
    def playable_classes(self):
        return 4
        
    @property
    def num_first_level_spells(self):
        return 12
        
    @property
    def hit_die(self):
        """
        Get the character's hit die.
        """
        return self.character_class['hitdice']        

    def get_character_class(self):
        """
        We determine character class based on your prime attribute.
        """
        prime_attribute, _ = sorted(self.attributes[:self.playable_classes],
                                    key=operator.itemgetter(1))[-1]
        return characterclass.PRIME_REQUISITE[prime_attribute]

    def get_hp(self):
        """
        Determine HP based on hit dice and CON modifiers. Note: this value may
        be negative and that is handled by the caller.
        """
        return d(self.hit_die) + self.get_bonus(*self.attributes[characterclass.CON])

    def get_ac(self):
        """
        The character's armor class based on their starting equipment.
        """
        if "Leather Armor" in self.equipment:
            ac = 7
        elif "Chain Armor" in self.equipment:
            ac = 5
        elif "Plate Armor" in self.equipment:
            ac = 3
        else: # no armor
            ac = 9
        if "Shield" in self.equipment:
            ac = ac - 1
        return ac

    def get_thac9(self):
        """
        To Hit AC 9 is 10 by default.
        """
        return 10

    def get_saves(self):
        """
        The character's saving throw tables. We proxy to the CharacterClass
        tables.
        """
        return self.character_class['saves']

    def get_languages(self):
        """
        For each bonus point for inteligence, a character knows an additional
        language, beyond Common and their alignment language.
        """
        bonus = self.get_bonus(*self.attributes[characterclass.INT])
        if bonus < 0:
            bonus = 0
        return random.sample(characterclass.LANGUAGES, bonus)

    def get_spell(self):
        """
        Magic-Users and Elves begin with a single first level spell.
        """
        if self.character_class.has_key('spells'):
            spells = self.character_class['spells'][:self.num_first_level_spells]
            return random.choice(spells)
        return None

    def get_notes(self):
        """
        Are there any additional notes about the character?
        """
        return []

    def get_bonus(self, attr, val):
        """
        Return the bonus for the given attribute. Subclassses will override. 
        Bonuses on attributes differ from edition to edition.
        """
        raise NotImplementedError()

    def with_bonus(self, attr, val):
        """
        Return attribute value with bonus attached, for display.
        """
        bonus = self.get_bonus(attr, val)
        if bonus:
            return "%d (%+d)" % (val, bonus)
        return "%d" % val

        
class BasicCharacter(Character):
    """
    Models a Moldvay/Mentzer basic D&D character.
    """

    @property
    def system(self):
        return "Basic"

    def get_ac(self):
        """
        In Basic D&D DEX improves your AC.
        """
        ac = super(BasicCharacter, self).get_ac()
        ac = ac - self.get_bonus(*self.attributes[characterclass.DEX])
        return ac

    def get_saves(self):
        """
        Your magic based saves are effected by your WIS.
        """
        saves = copy.copy(self.character_class['saves'])
        wisdom_bonus = self.get_bonus(*self.attributes[characterclass.WIS])
        for save in ['magic', 'stone', 'wands']:
            saves[save] = saves[save] - wisdom_bonus
        return saves

    def get_thac9(self):
        """
        In Basic D&D your strength improves your to hit.
        """
        thac9 = super(BasicCharacter,self).get_thac9()
        str_bonus = self.get_bonus(*self.attributes[characterclass.STR])
        return thac9 - str_bonus

    def get_bonus(self, attr, val):
        """
        Return the Moldav D&D attribute bonuses.
        """
        if val <= 3:
            bonus = -3
        elif 4 <= val <= 5:
            bonus = -2
        elif 6 <= val <= 8:
            bonus = -1
        elif 9 <= val <= 12:
            bonus = 0
        elif 13 <= val <= 15:
            bonus = 1
        elif 16 <= val <= 17:
            bonus = 2
        else:
            bonus = 3
        return bonus        


class GreyhawkCharacter(Character):
    """
    Generate a Little Brown Books + Supplement I: Greyhawk character. Greyhawk 
    introduced the Thief class, changed the hit dice per class, and led the 
    way to AD&D. As far as I can tell its mechanically similar to Basic D&D 
    save for the old-style attribute modifiers.
    """

    @property
    def system(self):
        return "Greyhawk"

    def get_ac(self):
        """
        In Greyhawk fighters get a Dex bonus to their AC.
        """
        ac = super(GreyhawkCharacter, self).get_ac()
        if self.character_class == characterclass.FIGHTER:
            bonus = self.attributes[characterclass.DEX][1] - 14
            ac = ac - bonus
        return ac

    def get_notes(self):
        """
        Store information about a characters strength bonuses.
        """
        # TODO: This does way more work than it should
        strength = self.attributes[characterclass.STR][1]
        if self.character_class == characterclass.FIGHTER and strength == 18:
            self.exceptional = d(100)
        hit, dmg = self.get_greyhawk_str(strength)
        if hit:
            self.thac9 = self.thac9 - hit
        notes = []
        if hasattr(self, 'exceptional'):
            notes.append("The character has an exceptional strength of %d." % self.exceptional)
        if dmg:
            notes.append("The character gets a %+d to damage rolls." % dmg)
        return notes

    def get_bonus(self, attr, val):
        """
        Return the Greyhawk D&D attribute bonuses.
        """
        if attr == 'STR':
            # Note: there multiple values here, and there is exceptional
            # strenth for fighters: damn it. We handle this elsewhere for now.
            # TODO: This whole method seems stupid.
            hit, _ = self.get_greyhawk_str(val)
            return hit
        elif attr == 'INT':
            # Bonus to languages
            if val > 10:
                return val - 10
        elif attr == 'CON':
            # Bonus to HP
            if val <= 6:
                return -1
            elif val == 15:
                return 1
            elif val >= 16:
                return val - 15
        elif attr == 'DEX':
            # missile damage
            if val <= 8:
                return -1
            elif val >= 13:
                return 1
        elif attr == 'CHA':
            # loyalty bonus
            if val <= 4:
                return -2
            elif val <= 6:
                return -1
            elif 13 <= val <= 15:
                return 1
            elif 16 <= val <= 17:
                return 2
            elif val >= 18:
                return 4
        return 0

    def get_greyhawk_str(self, val):
        """
        Greyhawk Strength has varying bonuses, and exceptional strength.
        """
        if val <= 4:
            return -2, -1
        elif val <= 5:
            return -1, 0
        elif 13 <= val <= 15:
            return 1, 0
        elif val == 16:
            return 1, 1
        elif val == 17:
            return 2, 2
        elif val == 18:
            if not hasattr(self, 'exceptional'):
                return 2, 3
            if 0 <= self.exceptional <= 50:
                return 2, 3
            elif 51 <= self.exceptional <= 75:
                return 3, 3
            elif 76 <= self.exceptional <= 90:
                return 3, 4
            elif 91 <= self.exceptional <= 99:
                return 3, 5
            elif self.exceptional == 100:
                return 4, 6
        return 0, 0 


class LBBCharacter(Character):
    """
    Models an Original D&D character. (1974 Little Brown Books.)
    """

    @property
    def system(self):
        return "Little Brown Books"
        
    @property
    def playable_classes(self):
        """
        The thief isn't a playable class in the original D&D books.
        """
        return 3
        
    @property
    def num_first_level_spells(self):
        """
        4 spells in Basic D&D don't exist in Original D&D, so we trim them
        when making spell selection.
        """
        return 8       

    @property
    def hit_die(self):
        """
        In LLB D&D all characters have the same hit die (d6).
        """
        return 6

    def get_hp(self):
        """
        Determine HP based on hit dice and CON modifiers. Figters have an 
        additional hit point at first level.
        """
        hp = super(LBBCharacter, self).get_hp()
        if self.character_class == characterclass.FIGHTER:
            hp = hp + 1
        return hp

    def get_bonus(self, attr, val):
        """
        Return the Original D&D attribute bonuses.
        """
        if attr == 'INT':
            # Bonus to languages
            if val > 10:
                return val - 10
        elif attr == 'CON':
            # Bonus to HP
            if val <= 6:
                return -1
            elif val >= 15:
                return 1
        elif attr == 'DEX':
            # missile damage
            if val <= 8:
                return -1
            elif val >= 13:
                return 1
        elif attr == 'CHA':
            # loyalty bonus
            if val <= 4:
                return -2
            elif val <= 6:
                return -1
            elif 13 <= val <= 15:
                return 1
            elif 16 <= val <= 17:
                return 2
            elif val >= 18:
                return 4
        return 0