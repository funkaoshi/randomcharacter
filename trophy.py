import itertools
import random

import mixins
import dice


class Character(mixins.AppearanceMixin):

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)

        self.burden = 0
        self.ruin = 1
        self.gold = 0

        self.occupation = {}
        self.background = {}
        self.equipment = []
        self.rituals = []

        self.name = random.choice(self.NAMES)
        self.drive = random.choice(self.DRIVES)

        self.initialize_occupation()
        self.initialize_background()
        self.initialize_equipment()
        self.initialize_rituals()

    def prefixed_name(self, name):
        prefix = "an" if name[0].lower() in ['a', 'e', 'i', 'o', 'u'] else "a"
        return "{} {}".format(prefix, name)

    @property
    def a_an_background(self):
        return self.prefixed_name(self.background['name'])

    @property
    def a_an_occupation(self):
        return self.prefixed_name(self.occupation['name'])

    def initialize_occupation(self):
        name, skills = random.choice(self.OCCUPATIONS)
        self.occupation['name'] = name
        self.occupation['skills'] = skills.split(', ')

    def initialize_background(self):
        name, skill = random.choice(self.BACKGROUNDS)
        self.background['name'] = name
        self.background['skill'] = skill

    def initialize_equipment(self):
        """
        Every starts with 3 items, and 3 slots for more items. You can also
        start with weapons and armour (combat equipment) that will increase
        your burden.
        """
        self.equipment = list(random.choice(self.BACKPACKS)) + ['...', '...', '...']
        self.weapons = random.sample(self.WEAPONS, dice.d(3) - 1)
        self.armour = random.sample(self.ARMOUR, dice.d(3) - 1)
        self.burden += len(self.weapons) + len(self.armour)

    def initialize_rituals(self):
        """
        Players start play with upto 3 rituals. Each ritual you know increases
        your ruin by 1.
        """
        self.rituals = random.sample(self.RITUALS, dice.d(4) - 1)
        self.ruin += len(self.rituals)

    NAMES = [
        "Akaleh", "Desarim", "Inda", "Masero", "Osto", "Sibil", "Alina",
        "Elisio", "Kasien", "Moradi", "Parda", "Talia", "Aram", "Esfahen",
        "Kel", "Neven", "Pela", "Teodan", "Baso", "Fion", "Kiva", "Nima",
        "Rasei", "Toram", "Benah", "Foret", "Lora", "Obeha", "Revel", "Valen",
        "Daian", "Ifori", "Mahera", "Orlen", "Sareh", "Vero"
    ]

    DRIVES = [
        "acquire Dread Forel's rebel fleet",
        "acquire the Gleaming Cache before it's too late",
        "arm the resistance against Lord Haffir's tyranny",
        "attend Countess Shima's Forbidden Festival",
        "become part of the Swirling Court",
        "become the only patron of Ansem, the Wistful",
        "break the geas placed by the Witch of Nevask",
        "break the siege on your sibling's fortress",
        "bribe the dean into expelling your insolent colleagues",
        "bribe the justiciars so they'll erase your crimes",
        "bribe the seneschal into leaving you alone",
        "bring freedom to Tirollis",
        "buy the only potion that can stop Mistral's death",
        "buy the orphanage where you were mistreated",
        "buy your brother's freedom from Barsul Prison",
        "buy your membership to the Golden Order",
        "commission a glorious statue of your deity",
        "destroy the works of Ajino, the Debauched Painter",
        "earn the respect of the Governor of Fort Duhrin",
        "earn the right to your family's name",
        "escape your awful family ties in Deverain",
        "establish an estate in the Levasti countryside",
        "establish an inn at the Velanti crossroads",
        "finance an expedition into the Blossoming Sea",
        "find the artifact that proves the king's true nature",
        "find the last piece of the Centennial Puzzle",
        "find the resting ground of the Morning Knight",
        "free the serfs of Bandung Prefecture",
        "give your ailing sibling the care they need",
        "give your betrothed the present they crave",
        "have your mother's name inscribed in the Azure Archives",
        "hire 100 chanters to perform the ritual that will bring forth The Scion",
        "hire a rescue team to retrieve your son from the Endless Canyon",
        "humiliate the Chancellor of Yogyakarta Lyceaum",
        "locate the jewel that haunts Eriol's dreams",
        "pay the magus that can lift Garalum's curse",
        "pay the toll of the Emerald Bridge",
        "pay your father's debt to Bright-Teeth Assyrio",
        "publish your discoveries from ancient Kalduhr",
        "rebuild Hisham's Fountain",
        "renovate your crumbling estate",
        "repay your debt to the Chieftan of Ubud",
        "restore the lost glory of the Caliginous Grove",
        "restore the name of your scandal-stricken family",
        "restore the Temple of Tanahlot",
        "resurrect the Cult of Derawan",
        "retire in comfort in the Rose District of Ambaret",
        "retrieve the lost banner of the Nameless Legion",
        "seek a cure for your ailing mother in Muckling",
        "seize control of the Free Borough of Khamal",
        "send your partner's meddlesome child to the Concealed College",
        "take Cyrus' place at the Earthen Council",
        "take revenge upon the Sultan of Borobudor",
        "win the auction for Princess Ylliria's weapon collection",
        "win the heart of the heir apparent of Naganeh",
    ]

    OCCUPATIONS = [
        ("Antiquarian", "artifacts, myths, obfuscation"),
        ("Artist", "expression, observation, symbols"),
        ("Assassin", "stealth, murder, misdirection"),
        ("Bodyguard", "protection, speed, vigilance"),
        ("Child", "innocence, wonder, smallness"),
        ("Farmhand", "pests, plants, weather"),
        ("Geomancer", "construction, omens, rituals"),
        ("Goatherd", "beasts, climbing, alertness"),
        ("Guide", "traveling, foraging, lore"),
        ("Hedge", "curses, improvisation, spirits"),
        ("Historian", "translation, research, engineering"),
        ("Knight", "combat, fortitude, athletics"),
        ("Laborer", "brawling, construction, hauling"),
        ("Leech", "forensics, herbs, surgery"),
        ("Lockpick", "acrobatics, security, surprise"),
        ("Magician", "performance, rituals, trickery"),
        ("Marksman", "sharpshooting, surveillance, tracking"),
        ("Merchant", "convincing, appraisal, focus"),
        ("Messenger", "wrestling, navigation, evasion"),
        ("Miner", "appraisal, paths, stone"),
        ("Oracle", "gods, rituals, trances"),
        ("Ox", "destruction, persistence, strength"),
        ("Ranger", "beasts, hunting, traps"),
        ("Royal", "appraisal, bribery, command"),
        ("Scavenger", "appraisal, foraging, escape"),
        ("Sellsword", "athletics, defense, weapons"),
        ("Shaman", "spirits, animals, rituals"),
        ("Smith", "maintenance, repair, crafting"),
        ("Smuggler", "dexterity, spontaneity, stealth"),
        ("Sorcerer", "alchemy, rituals, symbols"),
        ("Spider", "pests, stealth, traps"),
        ("Spouse-to-Be", "charm, innocence, curiosity"),
        ("Spy", "silence, poison, impersonation"),
        ("Trickster", "deception, escaping, legerdemain"),
        ("Witch", "homes, paths, rituals"),
        ("Woodcutter", "craft, construction, weapons"),
    ]

    BACKGROUNDS = [
        ("Abandoned Veteran", "warfare"),
        ("Banished Dancer", "grace"),
        ("Bankrupted Merchant", "haggling"),
        ("Byronic Hero", "brooding"),
        ("Cured Beastbitten", "transformation"),
        ("Defrocked Priest", "omens"),
        ("Discredited Academic", "disputation"),
        ("Disgraced Courtesan", "flattery"),
        ("Disgraced Preacher", "lies"),
        ("Disinherited Noble", "appraisal"),
        ("Enlivened Manikin", "artifice"),
        ("Escaped Cultist", "deception"),
        ("Expelled Apprentice", "lore"),
        ("Forlorn Romantic", "despair"),
        ("Frightened Runaway", "escaping"),
        ("Fugitive Servant", "evasion"),
        ("Grief-Stricken Poet", "words"),
        ("Grounded Sailor", "ropes"),
        ("Humiliated Gladiator", "dueling"),
        ("Impeached Official", "lying"),
        ("Indebted Butcher", "slaughter"),
        ("Injured Sculptor", "stone"),
        ("Lost Child", "hiding"),
        ("Lured Innocent", "following"),
        ("Penniless Scholar", "history"),
        ("Reformed Thug", "intimidation"),
        ("Retired Soldier", "tactics"),
        ("Runaway Kingsguard", "tracking"),
        ("Stouthearted Quester", "determination"),
        ("Unheeded Prophet", "omens"),
    ]

    BACKPACKS = [
        ("Fishing net, woven of silver", "Bottles, lead (6)", "Magnet"),
        ("Bag of hard candies (12)", "Skinning knife", "Winterwolf pelt"),
        ("Chalk, 3 colors (12 uses)", "Crowbar", "Heirloom compass"),
        ("Troll blood (heals 1 Ruin)", "Jar of glowworms (3)", "Vermin repellent (3 uses)"),
        ("Glass marbles (30)", "Pot of tar (6 uses)", "Scroll tube (mystery scroll)"),
        ("Food for your pet goat", "Skeleton key (1 use)", "Wooden toy unicorn"),
        ("Cage of rats (3)", "Flute", "Pot of honey (6 uses)"),
        ("Twine (300')", "Wind chimes", "Wooden mask, monstrous"),
        ("Bottle of fine wine", "Signet ring & wax", "Whistle"),
        ("Bear trap", "Musk, bear & deer (6 uses)", "Soap (6 uses)"),
        ("Journal & black/invisible inks", "Grease (6 uses)", "Dice (6 normal, 3 trick)"),
        ("Grappling hook", "Rope (120')", "Spyglass"),
        ("Iron spikes (12)", "Mallet", "Tent, two-person"),
        ("Bag of fool's gold (6 pieces)", "Torches, 3 hrs (6)", "Pickaxe"),
        ("Chain (24')", "Manacles", "Wooden labyrinth game"),
        ("Candles, 2 hrs dim (12)", "Mirror, small steel", "Perfume (6 uses)"),
        ("Ashes of your grandmother", "Book, blasphemous", "Shovel"),
        ("Hourglass, 10 min. markers", "Numbing herbs (3 uses)", "Sewing kit")
    ]

    RITUALS = [
        "Army - create three illusory copies of yourself that mimic your actions exactly",
        "Aura - creatures or objects under otherworldly influence glow faintly",
        "Beacon - nearby invisible beings or hidden objects shine with a fiery glow",
        "Bewitch - if given a gift, a person or animal will follow a simple command",
        "Bind - hold a person or animal in place",
        "Bolt - throw a crackling arc of heat and energy",
        "Bottle - force a spirit into an object",
        "Burrow - move through the ground",
        "Channel - allow a spirit to act through you",
        "Circle - anyone within a small ring of salt is unable to inflict or suffer violence",
        "Darkness - a living shadow snuffs out all natural and magical light nearby",
        "Drain - remove water from a person or animal",
        "Enliven - give flesh and breath to a human effigy",
        "Float - hold your breath to gently levitate",
        "Gale - conjure and guide a mighty wind",
        "Germinate - compel plants to furious growth",
        "Glamour - appear more charming and attractive",
        "Gleam - a luminous spirit is bound to an object to project torch-like light",
        "Guide - conjure a golden thread to follow",
        "Hasten - time in a small area moves at twice normal speed",
        "Hold - a warding sigil placed on a door prevents passage for a short time",
        "Hollow - push a spirit from its own body",
        "Hospitality - maintain peace while you share food & drink",
        "Inhabit - possess a person or animal",
        "Kindle - produce fire from oneself",
        "Knock - open nearby normal and sorcerous locks",
        "Mask - cover your face and stay still to remove yourself from others' senses",
        "Medium - surface thoughts of nearby creatures enter and overwhelm a target",
        "Messenger - send a message via a woodlands creature",
        "Mirage - create an illusion",
        "Mirror - take on the form of a known person or animal",
        "Numb - educe sensation within a body",
        "Obscure - hide a person or object from spirits",
        "Parse - divine the true meaning of any word, writing, sound, sign, or symbol",
        "Project - observe a remote location in spirit form",
        "Repel - push away animals or people with spritual force",
        "Rewind - slightly push a person or animal back in time",
        "Scent - use your olfactory sense to navigate in complete darkness",
        "Silence - deafen all nearby for a few minutes",
        "Sleep - send a person or animal into a deep slumber",
        "Slow - time in a small area moves at half normal speed",
        "Smite - strike a being or object with a spiritual weapon",
        "Summon - draw a known spirit or person to you",
        "Swarm - trade favors with a colony of vermin",
        "Switch - touch to swap bodies with another",
        "Tadpole - place a frog in a mouth to convert lungs to gills, or gills to lungs",
        "Unfall - temporarily reverse gravity in a small area",
        "Unravel - pull the threads of a ritual to uncast it, and recast it somewhere else",
        "Voice - alter your voice or make it appear to come from somewhere nearby",
        "Wail - produce a disorientating sound",
        "Ward - stay concentrating to protect a small area",
        "Web - produce enough webbing to cover a creature or reach something nearby",
        "Wither - reduce flora to ash and rot",
        "Yoke - at your command, a spectral bull will drag something roughly your weight",
    ]

    WEAPONS = [
        "Sword", "Axe", "Mace", "Dagger", "Club", "Whip", "Rapier", "Spear",
        "Staff", "Two-handed sword", "Maul", "Great Axe", "Long Bow",
        "Crossbow", "Sling"
    ]

    ARMOUR = [
        "Breast Plate", "Chainmail Shirt", "Gauntlets", "Helmet", "Shield"
    ]
