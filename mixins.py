import random

import characterclass
from dice import d, xdy


class BasicAttributesMixin(object):
    """
    Generates the basic attributes of a D&D character: STR, INT, DEX, CON, WIS,
    CHA. The scores are rolled using 3d6 in order.
    """

    def __init__(self, *args, **kwargs):
       self.attributes = self.roll_attribute_scores()

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

    def roll_attribute_scores(self):
        """
        Rolls the attribute scores: 3d6 in order, as one would expect.
        """
        return [(attribute, xdy(3,6)) for attribute in characterclass.ATTRIBUTES]

    def get_bonus(self, attr, val):
        """
        Return the bonus for the given attribute (the Moldvay D&D attribute
        bonuses.) Most sub-classes will override. Bonuses on attributes differ
        from edition to edition.
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

    def with_bonus(self, attr, val):
        """
        Return attribute value with bonus attached, for display.
        """
        bonus = self.get_bonus(attr, val)
        if bonus:
            return "%d (%+d)" % (val, bonus)
        return "%d" % val


class AppearenceMixin(object):
    """
    Display the appearance of the character. This is the best part of this
    generator. It's all ugly murderhobo children.
    """
    @property
    def appearance(self):
        return ', '.join(random.choice(feature)
                         for feature in characterclass.APPEARENCE)


class AscendingAcMixin(object):
    """
    Display the attack bonuses rather than a to-hit table. AC is ascending.
    The assumptions here are from LotFP.
    """

    @property
    def base_armour_class(self):
        """
        The default armour class of an unarmoured combatant is 10.
        """
        return 12

    @property
    def attack_bonus(self):
        return 2 if self.character_class == characterclass.FIGHTER else 1

    @property
    def melee_attack_bonus(self):
        bonus = self.get_bonus(*self.attributes[characterclass.STR])
        bonus += self.attack_bonus
        if bonus > 0:
            bonus = "+%d" % bonus
        return bonus

    @property
    def ranged_attack_bonus(self):
        bonus = self.get_bonus(*self.attributes[characterclass.DEX])
        bonus += self.attack_bonus
        if bonus > 0:
            bonus = "+%d" % bonus
        return bonus

    def get_ac(self):
        """
        The character's armor class based on their starting equipment.
        """
        ac = self.base_armour_class
        if "Leather Armor" in self.equipment:
            ac += 2
        elif "Chain Armor" in self.equipment:
            ac += 4
        elif "Plate Armor" in self.equipment:
            ac += 6
        if "Shield" in self.equipment:
            ac += 1
        ac += self.get_bonus(*self.attributes[characterclass.DEX])
        return ac

    def get_to_hit_table(self):
        return None


class HitDiceMixin(object):
    """
    In some OD&D games HP is re-rolled per session, so it doesn't make much
    sense to display the computed HP value. Instead we simply display the HD of
    the character, either 1 or 1+1 for Fighters.
    """
    def get_hp(self):
        # we set HP to None, which lets the template know we will display HD
        # instead.
        return None

    @property
    def hd(self):
        return "1" if self.character_class != characterclass.FIGHTER else "1+1"


class PsionicWildTalentMixin(object):
    """
    If you want to allow psionic wild talents as outlined in a blog post I
    wrote on the topic some time ago:
    """
    def __init__(self, *args, **kwargs):
        super(PsionicWildTalentMixin, self).__init__(*args, **kwargs)

        # roll for chance of psionic power
        self.wild_talent = self.get_wild_talent()

    def get_wild_talent(self):
        # TODO: what frequency do I actually want here?
        if d(6) != 1:
            return
        talent_roll = self.WIS - d(20)
        if talent_roll < 0:
            save_bonus = abs(talent_roll) / 2
            if save_bonus:
                return "+%d to saves vs. psionic attacks" % save_bonus
            else:
                return None
        else:
            return characterclass.WILD_TALENTS[talent_roll]


