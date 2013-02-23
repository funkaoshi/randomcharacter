import copy
import operator
import random

import characterclass
from dice import d, xdy

def _is_halfling(INT, CON, DEX, STR):
    return STR > 11 and DEX >= 9 and CON >= 9, characterclass.HALFLING

def _is_elf(INT, CON, DEX, STR):
    return INT > 11 and STR >= 9, characterclass.ELF

def _is_dwarf(INT, CON, DEX, STR):
    return CON > 11 and STR >= 9, characterclass.DWARF


class Character(object):
    """
    D&D characters are structurally quite similar. Common aspects of character
    creation are managed here. Subclasses for the different systems handle
    differences between the editions.
    """

    def __init__(self, classname=None, testing=False):
        self.attributes = [(attribute, xdy(3,6))
                           for attribute in characterclass.ATTRIBUTES]
        self.character_class = self.get_character_class(classname)
        if testing:
            return
        self.equipment = self.get_equipment()
        self.hp = self.get_hp()
        if self.hp < 1:
            self.hp = 1
        self.ac = self.get_ac()
        self.thac9 = self.get_thac9()
        self.saves = self.get_saves()
        self.languages = self.get_languages()
        self.spell = self.get_spell()
        self.appearance = self.get_appearance()
        self.notes = self.get_notes()

        # attribute map to ease display in template
        self.attr = dict((attr, self.with_bonus(attr, value))
                          for attr, value in self.attributes)
    @property
    def STR(self): return self.attributes[characterclass.STR][1]

    @property
    def INT(self): return self.attributes[characterclass.INT][1]

    @property
    def DEX(self): return self.attributes[characterclass.DEX][1]

    @property
    def CON(self): return self.attributes[characterclass.CON][1]

    @property
    def WIS(self): return self.attributes[characterclass.WIS][1]

    @property
    def CHA(self): return self.attributes[characterclass.CHA][1]


    def to_dict(self):
        """
        We use vars to convert the object to a dictionary, and then replace
        the character_class attribute with it's name.
        """
        attributes = vars(self)
        attributes["class"] = attributes["character_class"]["name"]
        del attributes["character_class"]
        attributes["system"] = self.system
        return attributes

    @property
    def system(self):
        raise NotImplementedError()

    @property
    def thieves(self):
        return True

    @property
    def demihumans(self):
        return True

    @property
    def num_first_level_spells(self):
        return 12

    @property
    def hit_die(self):
        """
        Get the character's hit die.
        """
        return self.character_class['hitdice']

    @property
    def max_ac(self):
        """
        The max AC to display in to-hit table.
        """
        return -1

    @property
    def max_to_hit(self):
        """
        The max value to display in to-hit table.
        """
        return 9 - self.max_ac + 1

    def get_character_class(self, classname=None):
        """
        We determine character class based on your prime attribute.
        """
        if classname:
            return characterclass.CLASS_BY_NAME[classname]
        if self.demihumans and d(100) < 50:
            # sorted attributes (excluding charisma)
            attributes = sorted(self.attributes[:5], reverse=True,
                                key=operator.itemgetter(1))
            if not (self.thieves and 'DEX' == attributes[0][0] and d(100) < 80):
                # We randomly test because there is overlap in what could
                # succeed and we want each to be equally likely in the long
                # run.
                tests = [_is_dwarf, _is_halfling, _is_elf]
                random.shuffle(tests)
                for t in tests:
                    result, c = t(self.INT, self.CON, self.DEX, self.STR)
                    if result:
                        return c
        # You're playing a human!
        index = 4 if self.thieves else 3
        prime_attribute, _ = sorted(self.attributes[:index],
                                    reverse=True, key=operator.itemgetter(1))[0]
        return characterclass.PRIME_REQUISITE[prime_attribute]

    def get_equipment(self):
        return self.character_class['equipment'][xdy(3,6)-3]

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
        For each bonus point for intelligence, a character knows an additional
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

    def get_appearance(self):
        return ', '.join(random.choice(feature)
                         for _, feature in characterclass.APPEARENCE.iteritems())

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
        Return the Moldvay D&D attribute bonuses.
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


class HolmesCharacter(Character):
    """
    Models a Holmes Basic Edition D&D Character. Holmes is much closer to
    original D&D than Moldvay/Cook.
    """

    @property
    def system(self):
        return "Holmes"

    def get_bonus(self, attr, val):
        """
        Return the Holmes' D&D attribute bonuses.
        """
        if attr == 'INT':
            # Bonus to languages
            if val > 10:
                return val - 10
        elif attr == 'CON':
            # Bonus to HP
            if val <= 6:
                return -1
            elif val == 15:
                return 1
            elif val > 15:
                return val - 15
        elif attr == 'DEX':
            # missile damage
            if val <= 8:
                return -1
            elif val >= 13:
                return 1
        return 0


class LBBCharacter(Character):
    """
    Models an Original D&D character. (1974 Little Brown Books.)
    """

    @property
    def system(self):
        return "Original (Little Brown Books)"

    @property
    def thieves(self):
        """
        The thief isn't a playable class in the original D&D books.
        """
        return False

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

    @property
    def max_ac(self):
        """
        In Original D&D Plate and Shield provides the absolute maximum
        armour bonus.
        """
        return 2

    def get_hp(self):
        """
        Determine HP based on hit dice and CON modifiers. Fighters have an
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


class PahvelornCharacter(LBBCharacter):
    """
    Models characters from the OD&D game Pahvelorn. (Essentially 1974 D&D.)
    More info here: http://untimately.blogspot.ca/p/pahvelorn.html.
    """

    def __init__(self, *args, **kwargs):
        super(LBBCharacter, self).__init__(*args, **kwargs)
        # Pahvelorn uses the re-roll your HP per session rule, so it doesn't
        # make sense to display a HP amount. We will display HD instead.
        self.hp = None
        self.hd = "1" if self.character_class != characterclass.FIGHTER else "1+1"

    @property
    def system(self):
        return "Pahvelorn / Original"

    @property
    def thieves(self):
        """
        Pahvelorn includes the Greyhawk Thief as a playable character,
        but this is the only addition from Greyhawk in Pahvelorn. The Thief's
        hit dice is 6, just like all the other characters.
        """
        return True

    @property
    def demihumans(self):
        """
        Player's can't play demihumans in Pahvelorn.
        """
        return False

    @property
    def retainer(self):
        """
        Players start with a random retainer.
        """
        return random.choice(characterclass.RETAINERS)

    def get_thac9(self):
        """
        In Pahvelorn characters all begin at different combat ranks,
        as per this post:
          http://untimately.blogspot.ca/2012/11/adjusted-attack-ranks.html
        """
        return {
            'Fighter': 7,
            'Cleric': 9,
            'Thief': 9,
            'Magic-User': 11,
        }[self.character_class['name']]

    def get_spell(self):
        """
        Players start with a basic spell book, and one random spell book. We
        tack on grimoires to the equipment list, instead of calling out a
        single spell.
        """
        if self.character_class.has_key('spells'):
            self.grimoires = [
                characterclass.STARTING_GRIMOIRE,
                random.choice(characterclass.GRIMOIRES),
            ]
        return None


class CarcosaCharacter(LBBCharacter):
    """
    Models a OD&D Character from Carcosa.
    """

    @property
    def system(self):
        return "Carcosa / Original"

    def get_character_class(self, classname):
        figher_score = max(self.CON, self.STR, self.DEX)
        if self.INT > figher_score or figher_score < 9:
            return characterclass.SORCERER
        return characterclass.FIGHTER

    def get_appearance(self):
        colour = random.choice([
            "Black", "Blue", "Bone", "Brown", "Dolm", "Green", "Jale",
            "Orange", "Purple", "Red", "Ulfire", "White", "Yellow"])
        sex = random.choice(['Man', 'Woman'])
        return "%s %s" % (colour, sex)

    def get_ac(self):
        """
        All armour for starting characters is no better or worse than leather.
        """
        return 5

    def get_equipment(self):
        """
        We generate a more Gonzo list of starting equipment.
        """
        self.equipment = [random.choice(characterclass.GONZO_ARMOUR),
                          random.choice(characterclass.GONZO_WEAPONS)]
        self.equipment += random.sample(characterclass.GONZO_GEAR, xdy(3,3))
        return self.equipment

    def get_languages(self): return []

