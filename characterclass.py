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
The 7 character classes from Basic D&D. TODO: Add Dwarves, Elves, and Halflings
"""
CLERIC = {
    'name': 'Cleric',
    'equipment': [
        ["Cudgel", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "4 gp"],
        ["Cudgel", "Shield", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Wooden Cross", "4 gp"],
        ["Mace", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "5 gp"],
        ["Quarter-Staff", "Leather Armor", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "12 Iron Spikes", "Wooden Cross", "3 Stakes & Mallet", "Steel Mirror", "10 gp"],
        ["Chain Armor", "war Hammer", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "2 Small Sacks", "8 gp"],
        ["Chain Armor", "Shield", "Mace", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Wooden Cross", "2 Small Sacks", "8 gp"],
        ["Chain Armor", "Shield", "War Hammer", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "2 Small Sacks", "3 Stakes & Mallet", "Steel Mirror", "10 gp"],
        ["Plate Armor", "Shield", "Mace", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Wooden Cross", "10 gp"],
        ["Plate Armor", "Shield", "war Hammer", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Small Sack", "2 gp"],
        ["Plate Armor", "Quarter-Staff", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "4 gp"],
        ["Cudgel", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Scroll", "4 gp"],
        ["Plate Armor", "Shield", "Mace", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "10 gp"],
        ["Leather Armor", "Mace", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "Wooden Cross", "Scroll", "2 Flasks oil", "1 gp"],
        ["Plate Armor", "Shield", "Helmet", "war Hammer", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "50' Rope", "Silver Cross", "3 Stakes & Mallet", "Steel Mirror", "12 gp"],
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

MAGICUSER = {
    'name': "Magic-User",
    'equipment': [
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole", "4 gp"],
        ["2 Daggers", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "2 Flasks oil", "50' Rope", "7 gp"],
        ["Dagger", "Backpack", "Waterskin", "Lantern", "4 Flasks oil", "1 Week Iron Rations", "10' Pole", "7 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "50' Rope", "Vial of Holy Water", "9 gp"],
        ["Dagger", "6 Torches", "Backpack", "Waterskin", "1 Week Iron Rations", "10' Pole 5 Flasks of oil", "Silver Mirror", "Belladona", "9 gp"],
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
    ]
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
    ]
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

# Map from a given attribute to most appropriate character class
PRIME_REQUISITE = {
    'STR': FIGHTER,
    'INT': MAGICUSER,
    'WIS': CLERIC,
    'DEX': THIEF
}

