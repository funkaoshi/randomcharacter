import copy
import operator
import random

import characterclass
from mixins import BasicAttributesMixin, AppearenceMixin, AscendingAcMixin, HitDiceMixin, PsionicWildTalentMixin
from dice import d, xdy


def _is_halfling(INT, CON, DEX, STR):
    return STR > 11 and DEX >= 9 and CON >= 9, characterclass.HALFLING

def _is_elf(INT, CON, DEX, STR):
    return INT > 11 and STR >= 9, characterclass.ELF

def _is_dwarf(INT, CON, DEX, STR):
    return CON > 11 and STR >= 9, characterclass.DWARF


class Character(BasicAttributesMixin, AppearenceMixin):
    """
    D&D characters are structurally quite similar. Common aspects of character
    creation are managed here. Subclasses for the different systems handle
    differences between the editions.
    """

    def __init__(self, *args, **kwargs):
        classname = kwargs.pop('classname')
        testing = kwargs.pop('testing', False)

        super(Character, self).__init__(*args, **kwargs)

        self.character_class = self.get_character_class(classname)
        self.class_name = self.character_class['name']
        self.personality = self.get_personality()
        if testing:
            return
        self.equipment = self.get_equipment()
        self.hp = self.get_hp()
        if self.hp is not None and self.hp < 1:
            self.hp = 1
        self.ac = self.get_ac()
        self.thac9 = self.get_thac9()
        self.to_hit = self.get_to_hit_table()
        self.saves = self.get_saves()
        self.languages = self.get_languages()
        self.spell = self.get_spell()
        self.notes = self.get_notes()
        self.skills = self.get_skills()

    def to_dict(self):
        """
        We use vars to convert the object to a dictionary, and then replace
        the character_class attribute with it's name.
        """
        attributes = vars(self)
        attributes["class"] = attributes["class_name"]
        del attributes["character_class"]
        del attributes["class_name"]
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
        return 0

    @property
    def max_to_hit(self):
        """
        The max value to display in to-hit table.
        """
        return 9 - self.max_ac + 1

    @property
    def save_name_table(self):
        return characterclass.SAVES

    @property
    def saves_with_names(self):
        return dict((s, (self.save_name_table[s], v))
                    for s, v in self.saves.iteritems())

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

    def get_to_hit_table(self):
        """
        Generate the to-hit table.
        """
        acs = range(9, self.max_ac - 1, -1)
        rolls = range(self.thac9, self.thac9 + self.max_to_hit)
        return [(ac, roll) for ac, roll in zip(acs, rolls)]

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
            return [random.choice(spells)]
        return None

    def get_personality(self):
        return ', '.join(random.sample(characterclass.PERSONALITY, 2))

    def get_notes(self):
        """
        Are there any additional notes about the character?
        """
        return []

    def get_skills(self):
        """
        Return any character skills, like thief abilities.
        """
        return None


class BasicCharacter(Character):
    """
    Models a Moldvay/Mentzer basic D&D character.
    """

    @property
    def system(self):
        return "Basic D&D"

    def get_ac(self):
        """
        In Basic D&D DEX improves your AC.
        """
        ac = super(BasicCharacter, self).get_ac()
        ac = ac - self.get_bonus(*self.attributes[characterclass.DEX])
        return ac

    def get_thac9(self):
        """
        In Basic D&D your strength improves your to hit.
        """
        thac9 = super(BasicCharacter,self).get_thac9()
        str_bonus = self.get_bonus(*self.attributes[characterclass.STR])
        return thac9 - str_bonus

    def get_saves(self):
        """
        Your magic based saves are effected by your WIS.
        """
        saves = copy.copy(self.character_class['saves'])
        wisdom_bonus = self.get_bonus(*self.attributes[characterclass.WIS])
        for save in ['magic', 'stone', 'wands']:
            saves[save] = saves[save] - wisdom_bonus
        return saves


class LotFPCharacter(AscendingAcMixin, Character):

    @property
    def system(self):
        return "Beta LotFP"

    @property
    def save_name_table(self):
        return characterclass.LOTFP['saves']

    def get_hp(self):
        """
        LotFP characters have a minimum number of HP.
        """
        hp = super(LotFPCharacter, self).get_hp()
        hp = max(hp, characterclass.LOTFP['min_hp'][self.character_class['name']])
        return hp

    def get_saves(self):
        """
        Your magic based saves are effected by your INT, other saves by your
        WIS.
        """
        saves = copy.copy(self.character_class['saves'])
        wis_bonus = self.get_bonus(*self.attributes[characterclass.WIS])
        int_bonus = self.get_bonus(*self.attributes[characterclass.WIS])
        saves['magic'] = saves['magic'] - int_bonus
        for save in ['wands', 'poison', 'stone', 'breath']:
            saves[save] = saves[save] - wis_bonus
        return saves

    def get_spell(self):
        """
        Magic-Users and Elves begin with a single first level spell and 3 random
        spells in their spell book.
        """
        if self.character_class.has_key('spells'):
            return ['Read Magic'] + random.sample(characterclass.LOTFP['spells'], 3)
        elif self.character_class == characterclass.CLERIC:
            return ['One clerical spell a day']
        return None

    def get_skills(self):
        skills = dict((s, x) for s, x in characterclass.LOTFP['skills'])
        if self.character_class == characterclass.THIEF:
            self.class_name = 'Specialist'
            for s in random.choice(characterclass.LOTFP['specialist_builds']):
                skills[s] = skills[s] + 1
        elif self.character_class == characterclass.DWARF:
            skills['Architeure'] = 3
        elif self.character_class == characterclass.ELF:
            skills['Search'] = 2
        elif self.character_class == characterclass.HALFLING:
            skills['Bushcraft'] = 3
            skills['Stealth'] = 5
        str_bonus = self.get_bonus(*self.attributes[characterclass.STR])
        skills['Open Doors'] = max(skills['Open Doors'] + str_bonus, 0)
        self.sneak_attack = skills.pop('Sneak Attack')
        skills = [(s, v) for s, v in skills.iteritems()]
        return skills


class HolmesCharacter(Character):
    """
    Models a Holmes Basic Edition D&D Character. Holmes is much closer to
    original D&D than Moldvay/Cook.
    """

    @property
    def system(self):
        return "Holmes D&D"

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
        return "Original (Little Brown Books) D&D"

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


class ApollyonCharacter(AscendingAcMixin, HitDiceMixin, LBBCharacter):
    """
    Models characters from Gus L's OD&D game Apollyon. More information on
    his blog: http://dungeonofsigns.blogspot.ca/search/label/HMS%20Apollyon
    """

    @property
    def system(self):
        return "Apollyon / Original D&D"

    def get_bonus(self, attr, val):
        """
        On the Apollyon bonuses are simplified.
        """
        if val >= 15:
            return 1
        if val <= 6:
            return -1
        return 0

    @property
    def thieves(self):
        return True

    @property
    def attack_bonus(self):
        return 2 if self.character_class == characterclass.FIGHTER else 0


class PahvelornCharacter(HitDiceMixin, LBBCharacter):
    """
    Models characters from the OD&D game Pahvelorn. (Essentially 1974 D&D.)
    More info here: http://untimately.blogspot.ca/p/pahvelorn.html.
    """

    @property
    def system(self):
        return "Pahvelorn / Original D&D"

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


class CarcosaBase(object):
    @property
    def appearance(self):
        colour = random.choice([
            "Black", "Blue", "Bone", "Brown", "Dolm", "Green", "Jale",
            "Orange", "Purple", "Red", "Ulfire", "White", "Yellow"])
        sex = random.choice(['Man', 'Woman'])
        return "%s %s" % (colour, sex)

    def get_character_class(self, classname):
        figher_score = max(self.CON, self.STR, self.DEX)
        if self.INT > figher_score or figher_score < 9:
            return characterclass.SORCERER
        return characterclass.FIGHTER

    def get_equipment(self):
        """
        We generate a more Gonzo list of starting equipment.
        """
        weapon = "%s %s" % (random.choice(characterclass.GONZO.METERIAL),
                            random.choice(characterclass.GONZO.WEAPONS))
        self.equipment = [random.choice(characterclass.GONZO.ARMOUR), weapon]
        self.equipment += random.sample(characterclass.GONZO.GEAR, 2)
        self.equipment += random.sample(characterclass.GONZO.STRANGE, 1)
        self.equipment += ["%s GP" % xdy(3,6)]
        return self.equipment

    def get_languages(self): return []


class CarcosaCharacter(CarcosaBase, LBBCharacter):
    @property
    def system(self):
        return "Carcosa / Original D&D"


class MastersOfCarcosaCharacter(CarcosaBase,
                                AscendingAcMixin,
                                HitDiceMixin,
                                PsionicWildTalentMixin,
                                LBBCharacter):
    """
    Characters for my Carcosa game.
    """

    def __init__(self, *args, **kwargs):
        super(MastersOfCarcosaCharacter, self).__init__(*args, **kwargs)

    @property
    def system(self):
        return "Masters of Carcosa"

    def get_bonus(self, attr, val):
        return 0

    def get_ac(self):
        return 15


class DelvingDeeperCharacter(LBBCharacter):
    """
    Models a Delving Deeper (OD&D clone) character.
    """

    @property
    def system(self):
        return "Delving Deeper"

    def get_hp(self):
        """
        Determine HP based on hit dice and CON modifiers. Fighters have an
        additional 2 hit points at first level.
        """
        hp = super(LBBCharacter, self).get_hp()
        if self.character_class == characterclass.FIGHTER:
            hp = hp + 1
        return hp

    def get_bonus(self, attr, val):
        """
        Bonuses are similar to LLB, but even less pronounced. Also there is
        bonus damage for high strength.
        """
        if attr == 'STR':
            # bonus to damage
            if val >= 15:
                return 1
        elif attr == 'INT':
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
            if val <= 6:
                return -1
            elif val >= 15:
                return 1
        elif attr == 'CHA':
            # loyalty bonus
            if val <= 3:
                return -2
            elif val <= 5:
                return -1
            elif 13 <= val <= 15:
                return 1
            elif 16 <= val <= 17:
                return 2
            elif val >= 18:
                return 4
        return 0


