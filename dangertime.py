"""
Automate the character creation for Evan's adventure game, Danger time:
http://gamepieces.blogspot.ca/2013/09/character-generators-for-weird-dark-ages.html
"""

import itertools
import random

import mixins
import dice


class Character(mixins.BasicAttributesMixin, mixins.AppearenceMixin):

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)

        self.hd = 1
        self.background, self.equipment = self.get_background()

    def get_background(self):
        backgrounds = [
            ("Poulticer", "mortar and pestle, dagger, mystery potion (you know what it doesn't do), oil flask, chalk"),
            ("Slaughterer", "heavy cleaver, half-chain, a string of fine sausage, twine"),
            ("Fungus Picker", "two different kinds of mushrooms, club, sling, rabbuck-hide gloves, lamp, oil flask"),
            ("Pickler", "pickle cask with delicious pickles, spice-rack, trident, wading boots"),
            ("Charcoal Burner", "Iron-banded broom, knife, sooty rags, mastic, crampons"),
            ("Purloiner", "hammer and spike, off-hand daggers, 50' rope, clothes with hidden pockets, a golden ring (stolen)"),
            ("Hunter", "crossbow OR bow, quiver, skinning-knife, leather jack, axe, brace of smoked frog"),
            ("Noble", "sword and shield and full chain OR pistolet and powderhorn and chain shirt, off-hand dagger, map to 'inheritance', a fine cape and mantle, laudanum OR signet ring"),
            ("Mendicant", "begging bowl, smart pet, reed flute, staff OR club"),
            ("Scribe", "mace, robes, runestones, oil-lamp, lard-pot, vellum, brush and ink"),
            ("Porter", "fists, club, auroch-hide armour, a porter's basket"),
            ("Timberfeller", "great-axe, knife, raspberry aquavit, sling, 50' rope"),
            ("Plumber", "gluepot, throwing hammer, weather-proof overalls"),
            ("Hayseed", "axe OR pitchfork OR threshing flail, dirk, harmonium OR great-kazoo, chewing weed, three torches"),
            ("House-guard", "shield, spear, misericorde, half-chain, club, 50' rope"),
            ("Fisher", "fishing pole and hook, gutting knife, 2 throwing spears, eel-hide armour, 3 torches, a smoked eel"),
            ("Barber", "bonesaw, steggar, clamps, bloody rags, leechjar OR pendulum"),
            ("Scroll-Runner", "running shoes, jerky, 50' rope, emberhorn, dagger, news-scroll, farseeing glass"),
            ("Paramour", "woodblock erotica OR book of poems, sword, perfume (as lamp-oil), locket OR prophylactics, bow and quiver"),
            ("Guild-Partisan", "great-weapon, mancatcher, dagger, hauberk with party armband, guild news-scroll, a set of trade tools (dyer, tanner, weaver, napier, builder, etc.)"),
            ("Bondsman", "waraxe OR crossbow and quiver and club, mail shirt, shield, saexe, gift-ring"),
            ("Apiarist", "chainmail, goggles, club, bellows, smokebomb, honeycomb"),
            ("Sailor", "axe OR cat, off-hand marlinspike, scrimshaw, shield OR leather armour, lodestone"),
            ("Bellman", "hookspear, chainmail shirt, shield, handbell, truncheon, 3 torches"),
            ("Smith", "warhammer OR sword, off-hand hammer, chainmail OR leather armour and shield, anvil, crucible"),
            ("Janissary", "harquebus, powderhorn, chainmail shirt, sword, shield, contract"),
            ("Seer", "silver dagger, cage of finches, brazier"),
            ("Ursar", "mancatcher, 20' chain, club, hide armour, hand drum"),
            ("Merchant", "fine clothes, guilder's chain, mace OR axe, a servant with a bale of trade goods"),
            ("Wolfs-head", "waraxe, caltrops, leather armour, crossbow, quiver, writ of blood price"),
            ("Therapist", "flail, shield, pendulum, meditation cushion, oil-lamp, oil-pot"),
            ("Skald", "harp OR scroll of epic poetry, off-hand dagger, sword OR bow and quiver, collection plate"),
            ("Drover", "studded leather, whip, club, brand, firehorn, heavy gloves, throwing axe"),
            ("Judicial Functionary", "great-weapon, leather jack, hooded cloak, hanging rope OR tongs, manacles and keys"),
            ("Wildling", "fists, moss and furs, 'lucky' stone, shillelagh"),
            ("Mercenary", "great-weapon OR waraxe and shield, dirk, ringed leathers, bow and quiver, totem"),
        ]
        background, equipment = random.choice(backgrounds)
        equipment = equipment.split(', ')

        bonus_equipment, silver = random.choice([
            (["fists", "a half-empty bottle", "a turnip"], lambda: dice.d(6)),
            (["nullwater", "a white conch"], lambda: dice.xdy(3, 6)),
            (["3 flasks of oil", "a hammer", "iron spikes"], lambda: 0),
            (["quill and ink", "incense"], lambda: 0),
            (["a hex scroll", "a pine sprig"], lambda: dice.d(6) * 10),
            (["sword and scabbard OR waraxe OR warhammer"], lambda: 0),
        ])
        equipment += bonus_equipment
        equipment.append("%d SP" % silver())

        # process the equipment list down to a finite list of stuff
        final_equipment = []
        for e in equipment:
            items = random.choice(e.split(' OR ')).split(' and ')
            final_equipment.append(items)

        return background, ", ".join(list(itertools.chain(*final_equipment)))
