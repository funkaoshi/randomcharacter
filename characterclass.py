"""
Attributes and general information about the D&D Character Classes.
"""


"""
The traditional 6 attributes, in order.
"""
ATTRIBUTES = ['STR', 'INT', 'WIS', 'DEX', 'CON', 'CHA']


"""
Indexes into ATTRIBUTES
"""
STR, INT, WIS, DEX, CON, CHA = range(6)


"""
20 example languages from Moldvay.
"""
LANGUAGES = [
    'Bugbear', 'Doppleganger', 'Dragon', 'Dwarvish', 'Elvish', 'Gargoyle',
    'Gnoll', 'Gnome', 'Goblin', 'Halfling', 'Harpy', 'Hobgoblin', 'Kobold',
    'Lizard Man','Medusa', 'Minotaur', 'Ogre', 'Orc', 'Pixie', 'Human Dialect'
]


"""
The 5 traditional D&D saving throws.
"""
SAVES = {
    'poison': 'Death Ray or Poison',
    'wands': 'Magical Wands',
    'stone': 'Paralysis or Turn to Stone',
    'breath': 'Dragon Breath',
    'magic': 'Rods, Staves, or Spells'
}


"""
The 7 character classes from Basic D&D. Equipment lists from Brendan's post
on the topic.
"""

CLERIC = {
    'name': 'Cleric',
    'equipment': [
        ["Cudgel", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "4 gp"],
        ["Cudgel", "Shield", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Wooden Cross", "4 gp"],
        ["Mace", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "5 gp"],
        ["Quarter-Staff", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "12 Iron Spikes", "Wooden Cross", "3 Stakes & Mallet", "Steel Mirror", "10 gp"],
        ["Chain Armor", "War Hammer", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "2 Small Sacks", "8 gp"],
        ["Chain Armor", "Shield", "Mace", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Wooden Cross", "2 Small Sacks", "8 gp"],
        ["Chain Armor", "Shield", "War Hammer", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "2 Small Sacks", "3 Stakes & Mallet", "Steel Mirror", "10 gp"],
        ["Plate Armor", "Shield", "Mace", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Wooden Cross", "10 gp"],
        ["Plate Armor", "Shield", "War Hammer", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Small Sack", "2 gp"],
        ["Plate Armor", "Quarter-Staff", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "4 gp"],
        ["Cudgel", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Scroll", "4 gp"],
        ["Plate Armor", "Shield", "Mace", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "10 gp"],
        ["Leather Armor", "Mace", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Scroll", "2 Flasks oil", "1 gp"],
        ["Plate Armor", "Shield", "Helmet", "War Hammer", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "3 Stakes & Mallet", "Steel Mirror", "12 gp"],
        ["Chain Armor", "War Hammer", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Scroll", "10 gp"],
        ["Plate Armor", "Shield", "Helmet", "Mace", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "Vial Holy Water", "12 Iron Spikes", "3 Stakes & Mallet", "Small Sack", "10 gp"]
    ],
    'hitdice': 6,
    'saves': {
        'poison': 11, 'wands': 12, 'stone': 14, 'breath': 16, 'magic': 15
    },
    'turn': [
        ('Skeleton', 7), ('Zombie', 9), ('Ghoul', 11), ('Wight', 'N')
    ],
}

FIGHTER = {
    'name': "Fighter",
    'equipment': [
        ["Spear", "Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "3 gp"],
        ["Cudgel", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "1 gp"],
        ["Leather Armor", "Morning Star", "Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "3 gp"],
        ["Leather Armor", "Battle axe", "Hand axe", "Dagger", "Sling", "Pouch With 20 Sling Bullets", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "7 gp"],
        ["Chain Armor", "Spear", "Dagger", "Sling", "Pouch With 20 Sling Bullets", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "11 gp"],
        ["Chain Armor", "Shield", "Sword", "Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "4 gp"],
        ["Chain Armor", "Spear", "Light Crossbow", "Case With 30 Quarrels", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "11 gp"],
        ["Plate Armor", "Shield", "Sword", "Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "4 gp"],
        ["Plate Armor", "Two-Handed Sword", "3 Daggers", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "2 Flasks oil", "9 gp"],
        ["Plate Armor", "Shield", "Sword", "Light Crossbow", "Case With 30 Quarrels", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "2 gp"],
        ["Plate Armor", "Flail", "Dagger", "35 Short bow", "Quiver of 20 Arrows", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Small Sack", "10 gp"],
        ["Plate Armor", "Shield", "Sword", "Light Crossbow", "Case With 30 Quarrels", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "5 gp"],
        ["Plate Armor", "Helmet", "2 Battle Axes", "Dagger", "Light Crossbow", "Case With 30 Quarrels", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "5 Flasks oil", "15 gp"],
        ["Plate Armor", "Two-Handed Sword", "Dagger", "Short bow", "Quiver of 20 Arrows", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "2 Small Sacks", "15 gp"],
        ["Plate Armor", "Halberd", "Dagger", "Long bow", "Quiver of 20 Arrows", "2 Silver Tipped Arrows", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "10 gp"],
        ["Plate Armor", "Shield", "Helmet", "Sword", "2 Daggers", "Light Crossbow", "Case With 30 Quarrels", "4 Silver Tipped Quarrels", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "9 gp"]
    ],
    'hitdice': 8,
    'saves': {
        'poison': 12, 'wands': 13, 'stone': 14, 'breath': 15, 'magic': 16
    }
}

# For Carcosa we have the Sorcerer variant of a fighter.
SORCERER = {
    'name': "Sorcerer",
    'equipment': FIGHTER['equipment'],
    'hitdice': 8,
    'saves': {
        'poison': 12, 'wands': 13, 'stone': 13, 'breath': 15, 'magic': 14
    }
}

MAGICUSER = {
    'name': "Magic-User",
    'equipment': [
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "4 gp"],
        ["2 Daggers", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "2 Flasks oil", "50' Rope", "7 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "7 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Vial of Holy Water", "9 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "5 Flasks of oil", "Silver Mirror", "Belladona", "9 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "2 Vials Holy Water", "4 gp"],
        ["3 Daggers", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "Vial of Holy Water", "16 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "2 Vials Holy Water", "24 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "67 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "77 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "Scroll", "10' Pole", "4 gp"],
        ["2 Daggers", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "Scroll", "50' Rope", "11 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "Scroll", "10' Pole", "7 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "Scroll", "50' Rope", "17 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "Scroll", "10' Pole", "27 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "Scroll", "50' Rope", "37 gp"]
    ],
    'hitdice': 4,
    'saves': {
        'poison': 13, 'wands': 14, 'stone': 13, 'breath': 16, 'magic': 15
    },
    'spells': [
        # Original 8 D&D Spells
        'Detect Magic', 'Hold Portal', 'Read Magic', 'Read Languages',
        'Protection from Evil', 'Light', 'Charm Person', 'Sleep',
        # Basic D&D added 4 new Spells
        'Floating Disc', 'Magic Missile', 'Shield', 'Ventriloquism'
    ],
}

THIEF = {
    'name': "Thief",
    'equipment': [
        ["Cudgel", "Sling", "Pouch With 20 Sling Bullets", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "4 gp"],
        ["Cudgel", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "1 gp"],
        ["Cudgel", "Dagger", "Sling", "Pouch With 20 Sling Bullets", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "6 gp"],
        ["Sword", "Dagger", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "9 gp"],
        ["Cudgel", "Light Crossbow", "Case With 30 Quarrels", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "6 gp"],
        ["Sword", "Light Crossbow", "Case of 30 Quarrels", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "7 gp"],
        ["Sword", "2 Daggers", "35 Short bow", "Quiver of 20 Arrows", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "1 gp"],
        ["Sword", "Dagger", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "32 gp"],
        ["Sword", "Light Crossbow", "Case of 30 Quarrels", "2 Silver Tipped Quarrels", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "10 gp"],
        ["Sword", "Dagger", "Short bow", "Quiver of 20 Arrows", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "17 gp"],
        ["Sword", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "65 gp"],
        ["Sword", "Light Crossbow", "Case of 30 Quarrels", "6 Silver Tipped Quarrels", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "20 gp"],
        ["Sword", "Short bow", "Quiver of 20 Arrows", "6 Silver Tipped Arrows", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "20 gp"],
        ["Sword", "4 Daggers", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "98 gp"],
        ["Sword", "Light Crossbow", "Case of 30 Quarrels", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "80 gp"],
        ["Sword", "3 Daggers", "Short bow", "Quiver of 20 Arrows", "8 Silver Tipped Arrows", "Leather Armor", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "31 gp"]
    ],
    'hitdice': 4,
    'saves': {
        'poison': 13, 'wands': 14, 'stone': 13, 'breath': 16, 'magic': 15
    },
    'skills': [
        ('Open Locks', '15%'),
        ('Find Traps', '10%'),
        ('Remove Traps', '10%'),
        ('Climb Walls', '87%'),
        ('Move Silently', '20%'),
        ('Hide in Shadows', '10%'),
        ('Pick Pockets', '20%'),
        ('Hear Noise', '1-2')
    ],
}

DWARF = {
    'name': 'Dwarf',
    'hitdice': 8,
    'saves': {
        'poison': 10, 'wands': 11, 'stone': 12, 'breath': 13, 'magic': 14
    },
    'equipment': FIGHTER['equipment']
}

ELF = {
    'name': 'Elf',
    'hitdice': 6,
    'saves': {
        'poison': 12, 'wands': 13, 'stone': 13, 'breath': 15, 'magic': 15
    },
    'equipment': MAGICUSER['equipment'],
    'spells': MAGICUSER['spells']
}

HALFLING = {
    'name': 'Halfling',
    'hitdice': 6,
    'saves': {
        'poison': 10, 'wands': 11, 'stone': 12, 'breath': 13, 'magic': 14
    },
    'equipment': FIGHTER['equipment']
}


"""
In Pahvelorn characters start with a random retainer.
"""
RETAINERS = [
    'Bodyguard (leather, dagger, d4: 1 sword, 2 mace, 3 battle axe, 4 spear)',
    'Torchbearer (dagger, 6 torches)',
    'Porter (dagger, backpack, 3 small sacks, 1 large sack)',
    'Squire (dagger)',
    'Mercenary (leather, sword, dagger, light crossbow, case with 30 quarrels)',
    'Shieldbearer (leather, shield, dagger)',
    'Servant (dagger)',
    'Dog (spiked collar, leash)',
]


"""
In Pahvelorn characters begin with one spell book, and must hunt for others.
"""
STARTING_GRIMOIRE = ('Arcana Metaphysica, anonymous', [
        'Read Magic (1)',
        'Dispel Magic (3)',
        'Remove Curse (4)',
        'Anti-Magic Shell (6)',
    ]
)

GRIMOIRES = [
    ('The Hidden Knowledge, attributed to Cochyla the Younger', [
		'Detect Magic (1)',
		'Detect Evil (1)',
		'Locate Object (2)',
		'ESP (2)',
		'Clairvoyance (3)',
		'Clairaudience (3)',
		'Wizard Eye (4)',
    ]),
    ('Realms Seen and Unseen, attributed to the Fifth Council', [
		'Light (1)',
		'Detect Invisibility (2)',
		'Invisibility (2)',
		'Continual Light (2)',
		'Invisibility, 10\' Radius (3)',
		'Infravision (3)',
    ]),
    ('The Organ of the Inner Moon, attributed to Sezius Elfblood', [
		'Charm Person (1)',
		'Sleep (1)',
		'Hold Person (3)',
		'Confusion (4)',
		'Charm Monster (4)',
		'Feeblemind (5)',
		'Geas (6)',
    ]),
    ('Mastering Gates, attributed to Marlow Shadow-Walker', [
		'Hold Portal (1)',
		'Wizard Lock (2)',
		'Knock (2)',
		'Pass-Wall (5)',
    ]),
    ('Codex of the Cloud-Masters, anonymous', [
		'Levitate (2)',
		'Fly (3)',
		'Protection from Normal Missiles (3)',
		'Telekinesis (5)',
    ]),
    ('Illusio, anonymous', [
		'Phantasmal Forces (2)',
		'Hallucinatory Terrain (4)',
		'Massmorph (4)',
		'Projected Image (6)',
    ]),
    ('On Essence, attributed to Caleia', [
		'Polymorph Self (4)',
		'Polymorph Others (4)',
		'Transmute Rock-Mud (5)',
		'Growth of Animals (5)',
		'Stone-Flesh (6)',
    ]),
    ('Arbatel of Flame', [
		'Fire Ball (3)',
		'Lightning Bolt (3)',
		'Disintegrate (6)',
    ]),
    ('Songs of Three Winters, attributed to Taymar the Wise', [
		'Slow Spell (3)',
		'Haste Spell (3)',
    ]),
    ('Arcana Necromantica, anonymous', [
		'Animate Dead (5)',
		'Magic Jar (5)',
		'Reincarnation (6)',
		'Death Spell (6)',
    ]),
    ('Conjurations & Banishments (fragments), anonymous', [
		'Protection from Evil (1)',
		'Protection from Evil, 10\' Radius (3)',
		'Conjure Elemental (5)',
		'Contact Higher Plane (5)',
		'Invisible Stalker (6)',
    ]),
    ('The Roads Between the Stars (fragments), anonymous', [
		'Dimension Door (4)',
		'Teleport (5)',
    ]),
]


"""
Additional information for Lamentations of the Flame Princess characters.
"""
LOTFP = {
    'skills': [
        ('Architecture', 1),
        ('Bushcraft', 1),
        ('Climb', 1),
        ('Languages', 1),
        ('Open Doors', 1),
        ('Search', 1),
        ('Sleight of Hand', 1),
        ('Sneak Attack', 0),
        ('Stealth', 1),
        ('Tinker', 1),
    ],
    'specialist_builds': [
        ['Stealth', 'Stealth', 'Sneak Attack', 'Sneak Attack'],
        ['Search', 'Search', 'Tinker', 'Tinker'],
        ['Climb', 'Climb', 'Open Doors', 'Search'],
        ['Stealth', 'Climb', 'Search', 'Sneak Attack'],
        ['Sneak Attack', 'Sneak Attack', 'Sneak Attack', 'Stealth'],
        ['Search', 'Search', 'Search', 'Search'],
        ['Tinker', 'Tinker', 'Tinker', 'Tinker'],
        ['Architecture', 'Languages', 'Open Doors', 'Tinker'],
    ],
    'spells': [
        # Read Magic and ...
        'Bookspeak', 'Charm Person', 'Comprehend Languages', 'Detect Magic',
        'Enlarge', 'Faerie Fire', 'Feather Fall', 'Floating Disc',
        'Hold Portal', 'Identify', 'Light', 'Magic Aura', 'Magic Missile',
        'Mending', 'Message', 'Shield', 'Sleep', 'Spider Climb',
        'Unseen Servant'
    ],
    'hitdice': {
        'Cleric': 6,
        'Fighter': 8,
        'Magic-User': 6,
        'Thief': 6,
        'Dwarf': 10,
        'Elf': 6,
        'Halfling': 6
    },
    'lotfp_saves': {
        'Cleric': {'poison': 11, 'wands': 12, 'stone': 14, 'breath': 16, 'magic': 15,},
        'Fighter': {'poison': 12, 'wands': 13, 'stone': 14, 'breath': 15, 'magic': 16},
        'Magic-User': {'poison': 13, 'wands': 13, 'stone': 13, 'breath': 16, 'magic': 14},
        'Thief': {'poison': 16, 'wands': 14, 'stone': 14, 'breath': 15, 'magic': 14},
        'Dwarf': {'poison': 8, 'wands': 9, 'stone': 10, 'breath': 13, 'magic': 12},
        'Elf': {'poison': 12, 'wands': 13, 'stone': 13, 'breath': 15, 'magic': 15},
        'Halfling': {'poison': 8, 'wands': 9, 'stone': 10, 'breath': 13, 'magic': 12}
    },
    'min_hp': {
        'Cleric': 4,
        'Fighter': 8,
        'Magic-User': 3,
        'Thief': 4,
        'Dwarf': 6,
        'Elf': 4,
        'Halfling': 4
    },
    'saves': {
        'poison': 'Poison',
        'wands': 'Magical Devices',
        'stone': 'Paralyzation',
        'breath': 'Breath Weapon',
        'magic': 'Magic'
    },
    'equipment': {
        'Thief': [
            ["Specialist Tools", "Dagger", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "1 day's Rations", "1 Cp"],
            ["Specialist Tools", "Short Sword", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Specialist Tools", "Short Sword", "Garotte", "Spear", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Specialist Tools", "Dagger", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Specialist Tools", "Short Sword", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "1 sp 11 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "2 Daggers", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Specialist Tools", "Short Sword", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Quiver - 4 Arrows", "1 day's Rations", "1 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Quiver - 14 Arrows", "1 day's Rations", "1 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Quiver - 20 Arrows", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "2 Daggers", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Quiver - 20 Arrows", "2 day's Rations", "Steel Mirror", "1 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "Dagger", "Garotte", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 16 Arrows", "Steel Mirror", "Scroll Case: Local map and Kingdom map", "2 day's Rations", "4 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "Dagger", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 16 Arrows", "Steel Mirror", "Scroll Case: Local map", "Holy Water", "2 day's Rations", "4 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "Dagger", "Garotte", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "100' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 20 Arrows", "Steel Mirror", "Scroll Case: Local map", "Holy Water", "2 day's Rations", "4 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "Dagger", "Garotte", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "100' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 20 Arrows", "Steel Mirror", "Scroll Case: Local map and Kingdom map", "Holy Water", "2 day's Rations", "4 Cp"],
            ["Leather Armor", "Specialist Tools", "Standard Sword", "Dagger", "Garotte", "Whip", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "100' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 20 Arrows", "Steel Mirror", "Scroll Case: Local map and Kingdom map", "Holy Water", "2 day's Rations", "4 Cp"],
        ],
        'Cleric': [
            ["Spear", "Shield", "Rapier", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Wooden Cross", "3 Cp"],
            ["Spear", "Shield", "Mace", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Wooden Cross"],
            ["Spear", "Shield", "Dagger", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Wooden Cross"],
            ["Mace", "Shield", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Wooden Cross"],
            ["Mace", "Shield", "Spear", "Dagger", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Wooden Cross"],
            ["Spear", "Shield", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Short bow", "Quiver With 10 Arrows", "Wooden Cross"],
            ["Spear", "Dagger", "Shield", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Short bow", "Quiver With 20 Arrows", "Wooden Cross"],
            ["Spear", "Shield", "Mace", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Short bow", "Quiver With 10 Arrows", "Wooden Cross"],
            ["Spear", "Dagger", "Shield", "Mace", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Short bow", "Quiver With 20 Arrows", "Wooden Cross"],
            ["Spear", "Shield", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Wooden Cross"],
            ["Spear", "Shield", "2 Daggers", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Wooden Cross"],
            ["Spear", "Shield", "Chain Armor", "Mace", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Wooden Cross"],
            ["Spear", "Shield", "Chain Armor", "Mace", "Short Sword", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Wooden Cross"],
            ["Spear", "Shield", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Shortbow", "Quiver With 20 Arrows ", "Wooden Cross"],
            ["Spear", "Polearm", "Shield", "Short Sword", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Wooden Cross"],
            ["Spear", "Mace", "Shield", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Shortbow", "Quiver With 20 Arrows ", "Wooden Cross"],
        ],
        'Fighter': [
            ["Spear", "Shield", "Rapier", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "4 Cp"],
            ["Spear", "Shield", "Standard Sword", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "1 Cp"],
            ["Spear", "Shield", "Dagger", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "1 Cp"],
            ["Standard Sword", "Shield", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "1 Cp"],
            ["Standard Sword", "Shield", "Spear", "Dagger", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "1 Cp"],
            ["Spear", "Shield", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Short bow", "Quiver With 10 Arrows", "1 Cp"],
            ["Spear", "Dagger", "Shield", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Short bow", "Quiver With 20 Arrows", "1 Cp"],
            ["Spear", "Shield", "Standard Sword", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Short bow", "Quiver With 10 Arrows", "1 Cp"],
            ["Spear", "Dagger", "Shield", "Standard Sword", "Leather Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Short bow", "Quiver With 20 Arrows", "1 Cp"],
            ["Spear", "Shield", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "1 Cp"],
            ["Spear", "Shield", "2 Daggers", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "1 Cp"],
            ["Spear", "Shield", "Chain Armor", "Standard Sword", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "1 Cp"],
            ["Spear", "Shield", "Chain Armor", "Standard Sword", "Short Sword", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "1 Cp"],
            ["Spear", "Shield", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Shortbow", "Quiver With 20 Arrows ", "1 Cp"],
            ["Spear", "Polearm", "Shield", "Short Sword", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "1 Cp"],
            ["Spear", "Standard Sword", "Shield", "Chain Armor", "day of Rations", "Sack", "3 Torches", "Soap", "Chalk", "Tinderbox", "50' Rope", "Backpack", "Iron Spike", "Shortbow", "Quiver With 20 Arrows ", "1 Cp"],
        ],
        'Magic-User': [
            ["Short Sword", "Garotte", "Spear", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Dagger", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Short Sword", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "1 sp 11 Cp"],
            ["Leather Armor", "Standard Sword", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Standard Sword", "2 Daggers", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Short Sword", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Quiver - 4 Arrows", "1 day's Rations", "1 Cp"],
            ["Leather Armor", "Standard Sword", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Quiver - 14 Arrows", "1 day's Rations", "1 Cp"],
            ["Leather Armor", "Standard Sword", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Quiver - 20 Arrows", "1 day's Rations", "Steel Mirror", "11 Cp"],
            ["Leather Armor", "Standard Sword", "2 Daggers", "Garotte", "Chalk", "Soap", "3 Torches", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Quiver - 20 Arrows", "2 day's Rations", "Steel Mirror", "1 Cp"],
            ["Leather Armor", "Standard Sword", "Dagger", "Garotte", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 16 Arrows", "Steel Mirror", "Scroll Case: Local map and Kingdom map", "2 day's Rations", "4 Cp"],
            ["Leather Armor", "Standard Sword", "Dagger", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "50' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 16 Arrows", "Steel Mirror", "Scroll Case: Local map", "Holy Water", "2 day's Rations", "4 Cp"],
            ["Leather Armor", "Standard Sword", "Dagger", "Garotte", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "100' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 20 Arrows", "Steel Mirror", "Scroll Case: Local map", "Holy Water", "2 day's Rations", "4 Cp"],
            ["Leather Armor", "Standard Sword", "Dagger", "Garotte", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "100' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 20 Arrows", "Steel Mirror", "Scroll Case: Local map and Kingdom map", "Holy Water", "2 day's Rations", "4 Cp"],
            ["Leather Armor", "Standard Sword", "Dagger", "Garotte", "Whip", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "100' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 20 Arrows", "Steel Mirror", "Scroll Case: Local map and Kingdom map", "Holy Water", "2 day's Rations", "4 Cp"],
            ["Leather Armor", "Standard Sword", "Dagger", "Garotte", "Whip", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "100' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 20 Arrows", "Steel Mirror", "Scroll Case: Local map and Kingdom map", "Holy Water", "2 day's Rations", "10 sp", "4 Cp"],
            ["Leather Armor", "Standard Sword", "Dagger", "Garotte", "Whip", "Chalk", "Soap", "Backpack", "Sack", "Tinderbox", "100' Rope", "Shortbow", "Lamp With 4 Flasks oil", "Quiver - 20 Arrows", "Steel Mirror", "Scroll Case: Local map and Kingdom map", "Holy Water", "2 day's Rations", "20 sp", "4 Cp"],
        ],
    }
}

LOTFP['equipment']['Elf'] = LOTFP['equipment']['Magic-User']
LOTFP['equipment']['Dwarf'] = LOTFP['equipment']['Fighter']
LOTFP['equipment']['Halfling'] = LOTFP['equipment']['Fighter']


APPEARENCE = [
    ['Male', 'Female'],
    ['Child', 'Youth', 'Adult', 'Mature', 'Old', 'Decrepit'],
    ['Messy Clothing', 'Scant Clothing', 'Immaculate Clothing',
     'Formal Attire', 'Threadbare Clothing', 'Elaborate Attire', 'Drab Clothing',
     'in Uniform'],
    ['Missing Limb', 'Obese', 'Scrawny', 'Muscular', 'Bald', 'Hairy', 'Tall',
     'Short', 'Ugly']
]


PERSONALITY = [
    'Accusative', 'Active', 'Adventurous', 'Affable', 'Aggressive',
    'Agreeable', 'Aimless', 'Aloof', 'Altruistic', 'Analytical', 'Angry',
    'Animated', 'Annoying', 'Anxious', 'Apathetic', 'Apologetic',
    'Apprehensive', 'Argumentative', 'Arrogant', 'Articulate', 'Attentive',
    'Bigoted', 'Bitter', 'Blustering', 'Boastful', 'Bookish', 'Bossy',
    'Braggart', 'Brash', 'Brave', 'Bullying', 'Callous', 'Calm', 'Candid',
    'Cantankerous', 'Capricious', 'Careful', 'Careless', 'Caring', 'Casual',
    'Catty', 'Cautious', 'Cavalier', 'Charming', 'Chaste', 'Chauvinistic',
    'Cheeky', 'Cheerful', 'Childish', 'Chivalrous', 'Clueless', 'Clumsy',
    'Cocky', 'Comforting', 'Communicative', 'Complacent', 'Condescending',
    'Confident', 'Conformist', 'Confused', 'Conscientious', 'Conservative',
    'Contentious', 'Contrary', 'Contumely', 'Conventional', 'Cooperative',
    'Courageous', 'Courteous', 'Cowardly', 'Coy', 'Crabby', 'Cranky',
    'Critical', 'Cruel', 'Cultured', 'Curious', 'Cynical', 'Daring',
    'Deceitful', 'Deceptive', 'Defensive', 'Defiant', 'Deliberate', 'Deluded',
    'Depraved', 'Discreet', 'Discreet', 'Dishonest', 'Disingenuous',
    'Disloyal', 'Disrespectful', 'Distant', 'Distracted', 'Distraught',
    'Docile', 'Doleful', 'Dominating', 'Dramatic', 'Drunkard', 'Dull',
    'Earthy', 'Eccentric', 'Elitist', 'Emotional', 'Energetic', 'Enigmatic',
    'Enthusiastic', 'Epicurean', 'Excited', 'Expressive', 'Extroverted',
    'Faithful', 'Fanatical', 'Fastidious', 'Fatalistic', 'Fearful', 'Fearless',
    'Feral', 'Fierce', 'Feisty', 'Flamboyant', 'Flippant', 'Flirtatious',
    'Foolhardy', 'Foppish', 'Forgiving', 'Friendly', 'Frightened', 'Frivolous',
    'Frustrated', 'Funny', 'Furtive', 'Generous', 'Genial', 'Gentle', 'Gloomy',
    'Goofy', 'Gossip', 'Graceful', 'Gracious', 'Grave', 'Gregarious',
    'Grouchy', 'Groveling', 'Gruff', 'Gullible', 'Happy', 'Harsh', 'Hateful',
    'Helpful', 'Honest', 'Hopeful', 'Hostile', 'Humble', 'Humorless',
    'Humorous', 'Idealistic', 'Idiosyncratic', 'Imaginative', 'Imitative',
    'Impatient', 'Impetuous', 'Implacable', 'Impractical', 'Impulsive',
    'Inattentive', 'Incoherent', 'Indifferent', 'Indiscreet', 'Individualist',
    'Indolent', 'Indomitable', 'Industrious', 'Inexorable', 'Inexpressive',
    'Insecure', 'Insensitive', 'Instructive', 'Intolerant', 'Intransigent',
    'Introverted', 'Irreligious', 'Irresponsible', 'Irreverent', 'Irritable',
    'Jealous', 'Jocular', 'Joking', 'Jolly', 'Joyous', 'Judgmental', 'Jumpy',
    'Kind', 'Know-it-all', 'Languid', 'Lazy', 'Lethargic', 'Lewd', 'Liar',
    'Likable', 'Lippy', 'Listless', 'Loquacious', 'Loving', 'Loyal', 'Lust',
    'Madcap', 'Magnanimous', 'Malicious', 'Maudlin', 'Mean', 'Meddlesome',
    'Melancholy', 'Melodramatic', 'Merciless', 'Merry', 'Meticulous',
    'Mischievous', 'Miscreant', 'Miserly', 'Modest', 'Moody', 'Moralistic',
    'Morbid', 'Morose', 'Mournful', 'Mousy', 'Mouthy', 'Mysterious', 'Naive',
    'Narrow-minded', 'Needy', 'Nefarious', 'Nervous', 'Nettlesome', 'Neurotic',
    'Noble', 'Nonchalant', 'Nurturing', 'Obdurate', 'Obedient', 'Oblivious',
    'Obnoxious', 'Obsequious', 'Obsessive', 'Obstinate', 'Obtuse', 'Odd',
    'Ornery', 'Optimistic', 'Organized', 'Ostentatious', 'Outgoing',
    'Overbearing', 'Paranoid', 'Passionate', 'Pathological', 'Patient',
    'Peaceful', 'Pensive', 'Pertinacious', 'Pessimistic', 'Philanderer',
    'Philosophical', 'Phony', 'Pious', 'Playful', 'Pleasant', 'Poised',
    'Polite', 'Pompous', 'Pondering', 'Pontificating', 'Practical',
    'Prejudiced', 'Pretentious', 'Preoccupied', 'Promiscuous', 'Proper',
    'Proselytizing', 'Proud', 'Prudent', 'Prudish', 'Prying', 'Puerile',
    'Pugnacious', 'Quiet', 'Quirky', 'Racist', 'Rascal', 'Rash', 'Realistic',
    'Rebellious', 'Reckless', 'Refined', 'Repellent', 'Reserved', 'Respectful',
    'Responsible', 'Restless', 'Reticent', 'Reverent', 'Rigid', 'Risk-taking',
    'Rude', 'Sadistic', 'Sarcastic', 'Sardonic', 'Sassy', 'Savage', 'Scared',
    'Scolding', 'Secretive', 'Self-effacing', 'Selfish', 'Selfless', 'Senile',
    'Sensible', 'Sensitive', 'Sensual', 'Sentimental', 'Serene', 'Serious',
    'Servile', 'Sexist', 'Sexual', 'Shallow', 'Shameful', 'Shameless',
    'Shifty', 'Shrewd', 'Shy', 'Sincere', 'Slanderous', 'Sly', 'Smug',
    'Snobbish', 'Sober', 'Sociable', 'Solemn', 'Solicitous', 'Solitary',
    'Solitary', 'Sophisticated', 'Spendthrift', 'Spiteful', 'Stern', 'Stingy',
    'Stoic', 'Stubborn', 'Submissive', 'Sultry', 'Superstitious', 'Surly',
    'Suspicious', 'Sybarite', 'Sycophantic', 'Sympathetic', 'Taciturn',
    'Tactful', 'Tawdry', 'Teetotaler', 'Temperamental', 'Tempestuous',
    'Thorough', 'Thrifty', 'Timid', 'Tolerant', 'Transparent', 'Treacherous',
    'Troublemaker', 'Trusting', 'Truthful', 'Uncommitted', 'Understanding',
    'Unfriendly', 'Unhinged', 'Uninhibited', 'Unpredictable', 'Unruly',
    'Unsupportive', 'Vague', 'Vain', 'Vapid', 'Vengeful', 'Vigilant',
    'Violent', 'Vivacious', 'Vulgar', 'Wanton', 'Wasteful', 'Weary',
    'Whimsical', 'Whiny', 'Wicked', 'Wisecracking', 'Wistful', 'Witty',
    'Zealous'
]


class GONZO:
    """
    Information we use when making Carcosa characters.
    """

    METERIAL = ["Obsidian", "Insect Carapace", "Insect Mandible",
                "Wood", "Space Alien Ceramic", "Giant Tooth",
                "Bone", "Bronze", "Iron"]
    WEAPONS = ['Battle-Axe', 'Trident', 'Sword', 'War-Hammer', 'Spear',
               'Scythe', 'Staff']
    ARMOUR = ['Boiled Dinosaur Leather Armour', 'Mail of Ceramic Discs',
              'Copper Scale Armour', 'Bone Scale Mail', 'Horn Scale Mail',
              'Tooth Scale Mail', 'Carved Wooden Armour', 'Dinosaur Scale Armour',
              'Giant Insect Chitin Plates', 'Bright Orange Breast Plate',
              'Bright Purple Breast Plate', 'Bamboo Mail', 'Rattan Armour',
              'Giant Centipede Carapace', 'Beetle Horn Mail']
    GEAR = ["Water Skin", "50' of Rope", "5 Torches", "2 Daggers",
            "2 Wooden Stakes", "Backpack", "Whip", "Fur Top", "Horned Helmet",
            "Grappling Hook"]
    STRANGE = [
        "Incomprehensible Book of Snake-Men Rituals",
        "Broken Space Alien Laser Pistol",
        "Dehydrated Tentacles",
        "Painted Bones",
        "Fermented Bug Juice",
        "5 Dead Snakes",
        "Space Alien Key Card",
        "Powder that turns 10 cubic feet of liquid to gel",
        "A power cell to ... something",
        "A map printed on skin",
        "A glowing Jale necklace",
        "A small potted plant that talks to your dreams",
        "A compass that points to the nearest alien",
        "A box that makes an occasional ticking sound that speeds up around certain craters",
        "A three-gallon jug that's neutrally buoyant in air",
        "Goggles that make dolm, jale and ulfire look gray",
        "A three inches tall dinosaur",
        "A book of lead sheets embossed with pictures of all the spiders in the world and then some",
        "A tiny bit of quivering red pudding in a vial",
        "A 30' rope made from the dried intestines of you tribe's enemies",
        "A zinc canteen in the shape of a turtle",
        "A package of pink salt crystals",
        "A large dried squid",
        "A cask of red liqour",
        "A large meat and lentil pastry",
        "Black smoked goggles",
        "10' of rusted iron chain, with manacles (50% you have the key)",
        "A clay flask of crushed beetle paste sunscreen",
        "1D8 shrunken heads",
    ]

WILD_TALENTS = [
    "Know Direction - The character knows which way is North.",
    "Far Hearing - For one turn the character hears all sounds within 50' as if they were being whispered directly into their ear. The character may choose what sounds to focus on.",
    "Far Seeing - For one turn the character may view a scene up to 50' away as if they were right there. They may see through walls and other obstacles, but not through lead.",
    "Thought Projection - The character may communicate a brief message mentally with a creature up to 50' away. The target understands the character, even if they share no common language.",
    "Object Projection - The character may teleport a small object in their possession up to 50' away.",
    "Telekinetic Grasp - For one turn the character may manipulate small objects from up to 50' away.",
    "Spark - The character may ignite any flammable object within 50' of them. (The 'heat' this power generates is no greater than that of a candle.)",
    "Levitate - For 1 turn, the character can float above the ground (up to 10').",
    "Minor ESP: For 1 turn the character may read the mind of another creature. (The character understand the creature even if they share no common language.)",
    "Cell Adjustment - The character regains up to 1d3 lost hit points. (This increases to 1d6 at level 3, 1d8 at level 6, 1d10 at level 9 and 1d12 at level 12.) The character may make a Save vs. Poison to cure themselves of any non-magical disease.",
    "'Invisiblity': For 1 turn the character can completely hide his presence from up to one sentient creature per level. The target may make a Save vs. Magic to resist the character's power.",
    "Id Insituation: All sentient characters, friend or foe, within 25' of the character feel an uncontrollable urge to eat, murder or fornicate.",
    "Psychic Distress: All sentient characters, friend or foe, within 25' of the character are immobilized for 1 turn.",
    "Minor Mind Control: For 1 turn, the character may manipulate the target into doing whatever the character wants. The target will have no memory of any events that transpire while under this mind control. The target my make a Save vs. Magic to resist the mind control.",
    "Minor Precognition: The character may re-roll any saving throw.",
    "Psionic Defence - Once per day per level, the character may make a Save vs. Magic to avoid the effects of any psionic power that targets them. (This is in addition to any saving throws the power may allow for.)",
    "Psionic Immunity: The character can not be the target of any psionic power.",
    "The Haitian: no character within 10' of the character, friend or foe, may use their psionic powers. The character also gains Psionic Immunity.",
]

# Map from a given attribute to most appropriate character class
PRIME_REQUISITE = {
    'STR': FIGHTER,
    'INT': MAGICUSER,
    'WIS': CLERIC,
    'DEX': THIEF
}

CLASSES = [FIGHTER, MAGICUSER, CLERIC, THIEF, DWARF, ELF, HALFLING]
VALID_CLASS_NAMES = [c['name'].lower().replace('-', '') for c in CLASSES]
CLASS_BY_NAME = dict(zip(VALID_CLASS_NAMES, CLASSES))
