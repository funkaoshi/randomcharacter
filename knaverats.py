import itertools
import random

import mixins
import dice

# From https://www.reddit.com/r/rpg/comments/9smybh/knave_rats_my_favorite_parts_of_knave_and_maze/

class Character(object):

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)

        # Attributes
        self.STR = self.attribute()
        self.DEX = self.attribute()
        self.CON = self.attribute()
        self.INT = self.attribute()
        self.WIS = self.attribute()
        self.CHA = self.attribute()

        self.health = 4 + int(self.CON)
        self.shield, self.light_armour = self.armour()
        self.weapon_class = self.weapon()
        armour_bonus = 1 if self.light_armour else 0
        shield_bonus = 1 if self.shield else 0
        self.armour = 6 + armour_bonus + shield_bonus

        self.attack = 1 if self.weapon_class is "H" else 0
        self.skill = None  # No starting skill
        self.spell = None  # No starting spell.

        self.equipment = ', '.join(self.get_equipment())
        self.equipment_slots = 10 + int(self.STR)

        self.get_feature()

    def attribute(self):
        return random.choice(["+2", "+1", "+1", "+1", "0", "0"])

    def armour(self):
        return random.choice([
            (True, True), 
            (True, True),
            (True, True),
            (False, True),
            (False, True),
            (False, False),
        ])

    def weapon(self):
        return random.choice([
            "L", "L", "L", "L", "H", "R",
        ])

    def get_equipment(self):
        items = [
            "Animal Scent",
            "Bear Trap",
            "Bedroll",
            "Caltrops",
            "Chain (10 ft.)",
            "Chalk",
            "Chisel",
            "Crowbar",
            "Fishing Net",
            "Glass Marbles",
            "Glue",
            "Grappling Hook",
            "Grease",
            "Hacksaw",
            "Hammer",
            "Hand drill",
            "Horn",
            "Iron spikes",
            "Iron tongs",
            "Lantern and Oil",
            "Large Sack",
            "Lockpicks (3)",
            "Manacles",
            "Medicine (3)",
            "Metal file",
            "Rope (50 ft.)",
            "Steel wire",
            "Shovel",
            "Steel mirror",
            "Ten Foot Pole",
            "Tinderbox",
            "Torch",
            "Vial of Acid",
            "Vial of Poison",
            "Waterskin",
        ]

        weapons_light = [
            'Axe', 'Dagger', 'Mace', 'Short Sword', 
            'Flail', 'One-Handed Spear',
        ]

        weapons_heavy = [
            'Spear', 'Halberd', 'Long Sword', 'Warhammer', 'Zweihander'
        ]

        weapons_ranged = [
            'Bow', 'Cross Bow', 'Sling', 'Blowpipe',
        ]

        equip = ['Rations (2)']
        if self.shield:
            equip += ['Shield']
        if self.light_armour:
            equip += ['Light Armour']

        if self.weapon_class == 'L':
            weapons = weapons_light
        if self.weapon_class == 'H':
            weapons = weapons_heavy
        if self.weapon_class == 'R':
            weapons = weapons_ranged

        return equip + random.sample(items, 6) + random.sample(weapons, 2) 

    def get_feature(self):
        feature = random.choice(['fighter', 'wizard', 'specialist'])
        if feature == 'fighter':
            self.attack = "+1"
        elif feature == 'wizard':
            self.spell = self.get_spell()
        elif feature == 'specialist':
            self.skill = self.get_skills()

    def get_spell(self):
        return 'MAGIC'

    def get_skills(self):
        return random.choice([
            "Briarborn (tracking, foraging, survival)",
            "Fingersmith (Tinkering, picking locks or pockets)",
            "Roofrunner (climbing, leaping, balancing)",
            "Shadowjack (moving silently, hiding in shadows)",
        ])

    @property
    def appearance(self):
        return random.choice([
            "Aquiline",
            "Athletic",
            "Barrel-Chested",
            "Boney",
            "Brawny",
            "Brutish",
            "Bullnecked",
            "Chiseled",
            "Coltish",
            "Corpulent",
            "Craggy",
            "Delicate",
            "Furrowed",
            "Gaunt",
            "Gorgeous",
            "Grizzled",
            "Haggard",
            "Handsome",
            "Hideous",
            "Lanky",
            "Pudgy",
            "Ripped",
            "Rosy",
            "Scrawny",
            "Sinewy",
            "Slender",
            "Slumped",
            "Solid",
            "Square-Jawed",
            "Statuesque",
            "Towering",
            "Trim",
            "Weathered",
            "Willowy",
            "Wiry",
            "Wrinkled",
        ])

    @property
    def physical_detail(self):
        return random.choice([
            "Acid scars",
            "Battle scars",
            "Birthmark",
            "Braided hair",
            "Brand mark",
            "Broken nose",
            "Bronze skinned",
            "Burn scars	",
            "Bushy eyebrows",
            "Curly hair",
            "Dark skinned",
            "Dreadlocks",
            "Exotic accent",
            "Flogging scars",
            "Freckles",
            "Gold tooth",
            "Hoarse voice",
            "Huge beard",
            "Long hair",
            "Matted hair",
            "Missing ear",
            "Missing teeth",
            "Moustache",
            "Muttonchops",
            "Nine fingers",
            "Oiled hair",
            "One-eyed",
            "Pale skinned",
            "Piercings	",
            "Ritual scars",
            "Sallow skin",
            "Shaved head",
            "Sunburned",
            "Tangled hair",
            "Tattoos",
            "Topknot",
        ])

    @property
    def background(self):
        return random.choice([
           "Alchemist",
            "Beggar-prince",
            "Blackmailer",
            "Bounty-hunter",
            "Chimney sweep",
            "Coin-clipper",
            "Contortionist",
            "Counterfeiter",
            "Cultist",
            "Cutpurse",
            "Debt-collector",
            "Deserter",
            "Fence",
            "Fortuneteller",
            "Galley slave",
            "Gambler",
            "Gravedigger",
            "Headsman",
            "Hedge knight",
            "Highwayman",
            "Housebreaker",
            "Kidnapper",
            "Mad prophet",
            "Mountebank",
            "Peddler",
            "Pit-fighter",
            "Poisoner",
            "Rat-catcher",
            "Scrivener",
            "Sellsword",
            "Slave",
            "Smuggler",
            "Street performer",
            "Tattooist",
            "Urchin",
            "Usurer",
        ])

    @property
    def clothing(self):
        return random.choice([
            "Antique",
            "Battle-torn",
            "Bedraggled",
            "Blood-stained",
            "Ceremonial",
            "Dated",
            "Decaying",
            "Eccentric",
            "Elegant",
            "Embroidered",
            "Exotic",
            "Fashionable",
            "Flamboyant",
            "Food-stained",
            "Formal",
            "Frayed",
            "Frumpy",
            "Garish",
            "Grimy",
            "Haute couture",
            "Lacey",
            "Livery",
            "Mud-stained",
            "Ostentatious",
            "Oversized",
            "Patched",
            "Patterned",
            "Perfumed",
            "Practical",
            "Rumpled",
            "Sigils",
            "Singed",
            "Tasteless",
            "Undersized",
            "Wine-stained",
            "Worn out",
        ])

    @property
    def personality(self):
        return random.choice([
            "Bitter",
            "Brave",
            "Cautious",
            "Chipper",
            "Contrary",
            "Cowardly",
            "Cunning",
            "Driven",
            "Entitled",
            "Gregarious",
            "Grumpy",
            "Heartless",
            "Honor-bound",
            "Hotheaded",
            "Inquisitive",
            "Irascible",
            "Jolly",
            "Know-it-all",
            "Lazy",
            "Loyal",
            "Menacing",
            "Mopey",
            "Nervous",
            "Protective",
            "Righteous",
            "Rude",
            "Sarcastic",
            "Savage",
            "Scheming",
            "Serene",
            "Spacey",
            "Stoic",
            "Stubborn",
            "Stuck-up",
            "Suspicious",
            "Wisecracking",
        ])

    @property
    def mannerism(self):
        return random.choice([
            "Anecdotes",
            "Breathy",
            "Chuckles",
            "Clipped",
            "Cryptic",
            "Deep voice",
            "Drawl",
            "Enunciates",
            "Flowery speech",
            "Gravelly voice",
            "Highly formal",
            "Hypnotic",
            "Interrupts",
            "Laconic",
            "Laughs",
            "Long pauses",
            "Melodious",
            "Monotone",
            "Mumbles",
            "Narrates",
            "Overly casual",
            "Quaint sayings",
            "Rambles",
            "Random facts",
            "Rapid-fire",
            "Rhyming",
            "Robotic",
            "Slow speech",
            "Speechifies",
            "Squeaky",
            "Street slang",
            "Stutters",
            "Talks to self",
            "Trails off",
            "Very loud",
            "Whispers",
        ])

    def get_spell(self):
        physical_element = [
            "Animating",
            "Attracting",
            "Binding",
            "Blossoming",
            "Consuming",
            "Creeping",
            "Crushing",
            "Diminishing",
            "Dividing",
            "Duplicating",
            "Enveloping",
            "Expanding",
            "Fusing",
            "Grasping",
            "Hastening",
            "Hindering",
            "Illuminating",
            "Imprisoning",
            "Levitating",
            "Opening	",
            "Petrifying",
            "Phasing",
            "Piercing",
            "Pursuing",
            "Reflecting	",
            "Regenerating",
            "Rending",
            "Repelling",
            "Resurrecting",
            "Screaming",
            "Sealing",
            "Shapeshifting",
            "Shielding",
            "Spawning",
            "Transmuting",
            "Transporting",
        ]

        physical_effect = [
            "Acid",
            "Amber",
            "Bark",
            "Blood",
            "Bone",
            "Brine",
            "Clay ",
            "Crow",
            "Crystal",
            "Ember",
            "Flesh",
            "Fungus",
            "Glass",
            "Honey",
            "Ice",
            "Insect",
            "Wood ",
            "Lava",
            "Moss",
            "Obsidian",
            "Oil",
            "Poison",
            "Rat ",
            "Salt",
            "Sand",
            "Sap",
            "Serpent",
            "Slime",
            "Stone",
            "Tar",
            "Thorn",
            "Vine",
            "Water",
            "Wine",
            "Wood",
            "Worm",
        ]

        physical_form = [
            "Altar",
            "Armor",
            "Arrow ",
            "Beast",
            "Blade",
            "Cauldron",
            "Chain",
            "Chariot",
            "Claw",
            "Cloak",
            "Colossus",
            "Crown",
            "Elemental",
            "Eye",
            "Fountain",
            "Gate",
            "Golem",
            "Hammer",
            "Horn",
            "Key",
            "Mask",
            "Monolith",
            "Pit",
            "Prison",
            "Sentinel",
            "Servant",
            "Shield",
            "Spear",
            "Steed",
            "Swarm",
            "Tentacle",
            "Throne",
            "Torch",
            "Trap",
            "Wall",
            "Web",

        ]

        ethereal_element = [
            "Avenging",
            "Banishing",
            "Bewildering",
            "Blinding",
            "Charming",
            "Communicating",
            "Compelling",
            "Concealing",
            "Deafening",
            "Deceiving",
            "Deciphering",
            "Disguising",
            "Dispelling",
            "Emboldening",
            "Encoding",
            "Energizing",
            "Enlightening",
            "Enraging",
            "Excruciating",
            "Foreseeing",
            "Intoxicating",
            "Maddening",
            "Mesmerizing",
            "Mindreading",
            "Nullifying",
            "Paralyzing",
            "Revealing",
            "Revolting",
            "Scrying",
            "Silencing",
            "Soothing",
            "Summoning",
            "Terrifying",
            "Warding",
            "Wearying",
            "Withering",
        ]

        ethereal_effect = [
            "Ash",
            "Chaos",
            "Distortion",
            "Dream",
            "Dust",
            "Echo",
            "Ectoplasm",
            "Fire",
            "Fog",
            "Ghost",
            "Harmony",
            "Heat",
            "Light",
            "Lightning",
            "Memory",
            "Mind",
            "Mutation",
            "Negation",
            "Plague",
            "Plasma",
            "Probability",
            "Rain",
            "Rot",
            "Shadow",
            "Smoke",
            "Snow",
            "Soul",
            "Star",
            "Stasis",
            "Steam",
            "Thunder",
            "Time",
            "Void",
            "Warp",
            "Whisper",
            "Wind",
        ]

        ethereal_form = [
            "Aura",
            "Beacon",
            "Beam",
            "Blast",
            "Blob",
            "Bolt",
            "Bubble",
            "Call",
            "Cascade",
            "Circle",
            "Cloud",
            "Coil",
            "Cone ",
            "Cube",
            "Dance",
            "Disk",
            "Field",
            "Form",
            "Gaze",
            "Loop",
            "Moment",
            "Nexus",
            "Portal",
            "Pulse",
            "Pyramid",
            "Ray",
            "Shard",
            "Sphere",
            "Spray",
            "Storm",
            "Swarm",
            "Torrent",
            "Touch",
            "Vortex",
            "Wave",
            "Word",
        ]

        spell_form = [
            (physical_effect, physical_form),
            (ethereal_element, physical_form),
            (physical_effect, ethereal_form),
            (ethereal_element, ethereal_form),
            (ethereal_effect, physical_form),
            (physical_effect, physical_element),
            (ethereal_effect, ethereal_form),
            (physical_effect, ethereal_element),
            (physical_element, physical_form),
            (ethereal_effect, physical_element),
            (physical_element, ethereal_form),
            (ethereal_effect, ethereal_element),
        ]

        return ' '.join([random.choice(component) for component in random.choice(spell_form)])


