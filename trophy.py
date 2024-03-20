import random

import mixins
import dice


class Character(mixins.AppearanceMixin):

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)

        self.burden = 1
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
        "Akaleh", "Alina", "Aram", "Baso", "Benah", "Daian", "Desarim",
        "Elisio", "Esfahen", "Fion", "Foret ", "Ifori", "Inda", "Kasien",
        "Kel", "Kiva", "Lora", "Mahera", "Masero", "Moradi", "Neven", "Nima",
        "Obeha", "Orlen", "Osto", "Parda", "Pela", "Rasei", "Revel", "Sareh",
        "Sibil", "Talia", "Teodan", "Toram", "Valen", "Vero"
    ]

    DRIVES = [
        "acquire the Gleaming Cache before it is too late",
        "arm the resistance against Lord Haffir's tyranny",
        "attend Countess Shima's Forbidden Festival",
        "become part of the Swirling Court",
        "become the only patron of Ansem the Wistful",
        "break the geas placed by the Witch of Nevask",
        "break the siege on your sibling's fortress",
        "bribe the justiciars so they erase your crimes",
        "bring freedom to Tirollis",
        "buy the orphanage where you were mistreated",
        "buy your brother's freedom from Barsul Prison",
        "commission a glorious statue of your deity",
        "destroy the work of Ajino the Debauched Painter",
        "earn the respect of the Governor of Fort Duhrin",
        "earn the right to your family's name",
        "establish an estate in the Levasti countryside",
        "finance an expedition into the Blossoming Sea",
        "find the artifact that proves the king's true nature",
        "find the resting ground of the Morning Knight",
        "free the kindly followers of the Piper",
        "give your betrothed the present they crave",
        "inscribe your mother's name in the Azure Archives",
        "locate the jewel that haunts Eriol's dreams",
        "pay the toll of the Emerald Bridge",
        "pay your father's debt to Bright-Teeth Assyrio",
        "publish your discoveries from ancient Kalduhr",
        "rebuild Hisham's Fountain",
        "repay your losses to the Southern Pass Company",
        "restore the lost glory of the Caliginous Grove",
        "restore the Temple of Tanahlot",
        "resurrect the Cult of Derawan",
        "retire in comfort in the Rose District of Ambaret",
        "retrieve the lost banner of the Nameless Legion",
        "seize absolute control of Kormoran's Wheel",
        "take Cyrus' place at the Earthen Council",
        "win the heart of the heir apparent of Naganeh",
    ]

    OCCUPATIONS = [
        ("Antiquarian", "artifacts, myths, obfuscation"),
        ("Artificer", "alchemy, invention, traps"),
        ("Astrologer", "darkness, stars, symbols"),
        ("Blacksmith", "endurance, metal, weapons"),
        ("Bodyguard", "protection, speed, vigilance"),
        ("Chain", "commands, elements, rituals"),
        ("Champion", "commands, ferocity, presence"),
        ("Cook", "food, improvisation, poisons"),
        ("Demonologist", "demons, negotiation, trickery"),
        ("Geomancer ", "construction, paths, patterns"),
        ("Guide", "foraging, hunting, paths"),
        ("Hedge", "improvisation, rituals, spirits"),
        ("Herbalist", "perception, plants, remedies"),
        ("Intercessor", "charm, persistence, rituals"),
        ("Lamb", "innocence, sacrifice, rituals"),
        ("Lancer", "balance, coordination, precision"),
        ("Leech", "blood, deduction, surgery"),
        ("Lockpick", "acrobatics, security, silence"),
        ("Magician", "performance, rituals, trickery"),
        ("Medium", "spirits, vigilance, willpower"),
        ("Merchant", "bribery, focus, persuasion"),
        ("Naturalist", "beasts, plants, silence"),
        ("Nest", "coordination, rituals, vermin"),
        ("Oracle", "interpretation, rituals, trances"),
        ("Ox", "destruction, persistence, strength"),
        ("Poet", "passion, persuasion, rituals"),
        ("Ranger", "beasts, hunting, traps"),
        ("Sellsword", "athletics, defense, surprise"),
        ("Smuggler", "dexterity, spontaneity, stealth"),
        ("Snake", "charm, trickery, performance"),
        ("Sorcerer", "alchemy, rituals, symbols"),
        ("Spider", "surprise, traps, vermin"),
        ("Vessel", "attraction, rituals, surrender"),
        ("Witch", "homes, plants, rituals"),
        ("Woodcutter", "beasts, strength, trails"),
        ("Zealot", "interrogation, rituals, strength"),
    ]

    BACKGROUNDS = [
        ("Abandoned Squire", "aiding"),
        ("Banished Dancer", "grace"),
        ("Cured Beastbitten", "transformation"),
        ("Defrocked Priest", "omens"),
        ("Devoted Widow", "patience"),
        ("Disgraced Courtesan", "flattery"),
        ("Disinherited Noble", "appraisal"),
        ("Emboldened Ratcatcher", "lairs"),
        ("Enlightened Miner", "paths"),
        ("Errant Knight", "dueling"),
        ("Escaped Cultist", "deception"),
        ("Expelled Apprentice", "lore"),
        ("Failed Pilgrim", "saints"),
        ("Flockless Shepherd", "soothing"),
        ("Grounded Sailor", "ropes"),
        ("Hapless Peddler", "trading"),
        ("Heretical Inquisitor", "secrets"),
        ("Impeached Official", "lies"),
        ("Imprecise Barber", "injury"),
        ("Injured Whaler", "hunting"),
        ("Liberated Prisoner", "deals"),
        ("Lost Child", "hiding"),
        ("Lured Innocent", "temptation"),
        ("Opportunistic Graverobber", "death"),
        ("Oppressed Laborer", "rebellion"),
        ("Orphaned Manikin", "mimicry"),
        ("Plagued Farmer", "corruption"),
        ("Reckless Moneylender", "ambition"),
        ("Reformed Thug", "intimidation"),
        ("Retired Soldier", "tactics"),
        ("Runaway Kingsguard", "tracking"),
        ("Traitorous Cupbearer", "betrayal"),
        ("Uninspired Artisan", "crafting"),
        ("Unmasked Faeborn", "illusions"),
        ("Usurped Royal", "commands"),
        ("Wandering Refugee", "disguise"),
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
        "Army - create illusory copies of yourself that mimic your actions",
        "Ashes - burn something irreplaceable to turn a creature or object to dust",
        "Aura - ascertain a creature's emotional state, truthfulness, and true form",
        "Beacon - nearby hidden creatures or objects shine with a fiery glow",
        "Beast - take a form halfway between human and animal",
        "Bewitch - a creature will follow a simple command if given a gift",
        "Bind - hold a creature in place for as long as you stay motionless",
        "Blink - a creature you touch teleports to a spot you can see",
        "Blur - touch a creature to blur their form, making their details and boundaries hard to determine",
        "Bolt - throw a crackling arc of heat and energy",
        "Bottle - force a spirit into an object",
        "Brimstone - grow scorching hot to the touch",
        "Burrow - move through the ground",
        "Carve - alter a creature or object via sorcerous subtraction",
        "Channel - allow a spirit to act through you",
        "Circle - a creature within a ring of salt cannot inflict or suffer violence",
        "Clay - use your hands to rearrange and reshape inanimate material",
        "Clock - time in a small area moves at an unnaturally fast or slow speed",
        "Compel - force a creature to perform a non-lethal task, or free a creature from a prior Compel",
        "Crucible - heat a metallic object to melting",
        "Darkness - a living shadow snuffs out all nearby light",
        "Dazzle - distract and confuse nearby creatures with colorful moving lights",
        "Doom - make a creature feel a sense of impending doom",
        "Door - draw a door on a solid barrier to create a portal through it",
        "Drain - remove all water from a creature",
        "Dryad - stay still to transform into a tree and communicate with other trees",
        "Elegy - appear as deceased",
        "Emote - heighten or dampen the current emotions of all in your presence",
        "Endure - touch a creature to allow them to withstand temperature extremes",
        "Enliven - give flesh and breath to an effigy",
        "Entangle - cause plants to twist and grasp, holding or slowing a creature",
        "Ether - a touched creature or object becomes spectral and intangible",
        "Fantasy - observe and alter the dreams of a known creature",
        "Fault - strike the weakest point of an object with phantasmal force",
        "Feather - reduce the density of an object",
        "Feral - increase the size, temper, and monstrosity of a creature you touch",
        "Float - hold your breath to gently levitate",
        "Flow - shape and command bodies of water",
        "Fountain - a forceful spring of water bursts forth from a location you touch",
        "Future - an object disappears, then reappears a short time later in exactly the same spot",
        "Gale - conjure and guide a mighty wind",
        "Gardener - consume a plant to absorb some of its memories",
        "Germinate - compel plants to furious growth",
        "Ghoul - animate a dead body",
        "Glamour - appear more charming and attractive",
        "Gleam - a luminous spirit is bound to an object to project light",
        "Guide - conjure a thread to follow",
        "Hand - concentrate to mentally move a small object you can see",
        "Haunt - summon a spirit to torment a creature",
        "Hold - a sigil prevents passage through a space for a short time",
        "Hollow - push a spirit from a body",
        "Hospitality - maintain peace while you share food and drink",
        "Immolate - engulf your body in flame",
        "Inhabit - possess a creature",
        "Inscribe - create or alter a written or carved message",
        "Kindle - produce fire from yourself",
        "Knock - open nearby portal that is shut",
        "Leviathan - draw forth a creature of the deep",
        "Liar - contact a spirit who can answer any question, but only falsely",
        "Lift - temporarily reverse gravity in a small area",
        "Martyr - touch a creature to transfer their Conditions to you",
        "Mask - cover your face to remove yourself from others' senses",
        "Maze - the surrounding environment warps into a labyrinth with you at the center",
        "Medium - surface thoughts of nearby creatures enter and overwhelm a target",
        "Messenger - send a message via a creature",
        "Mirage - create an illusion that is obviously fake only on close inspection",
        "Mirror - take on the form of a known creature",
        "Nightwalk - move untraceably through darkness",
        "Numb - reduce sensation within a creature",
        "Obscure - hide a creature or object from the view of one other creature",
        "Orchard - conjure a few dozen apples, some poisonous",
        "Parse - divine the meaning of any word, writing, sound, sign, or symbol",
        "Provoke - force an opponent to make a choice: freeze, fight, or flee",
        "Rebirth - force a known spirit to be reborn in a new body",
        "Repel - push away a creature with spiritual force",
        "Rewind - slightly push a creature back in time",
        "Rubber - the body of a touched creature becomes elastic and can stretch beyond normal limits",
        "Rustle - an illusory sound of your choosing appears to come from somewhere nearby",
        "Scale - double or halve the size of an object you touch",
        "Scent - navigate a space by smell alone, or follow the scent trail of a known creature",
        "Scramble - touch a creature to make them forget their known rituals until the next sunrise",
        "Scry - observe a location in spirit form",
        "Sever - you can detach and reattach a body part, and still control it while removed",
        "Shell - your skin grows a tough outer layer which acts as armor",
        "Shroud - as long as they remain motionless, a group of creatures are hidden from others' senses",
        "Silence - deafen all nearby for a short amount of time",
        "Siphon - detect and extract poison from food, water, or a creature",
        "Sleep - send a creature into a deep slumber",
        "Smite - strike with a spiritual weapon",
        "Spark - touch to revive a newly dead creature, a second touch-even accidental-kills instantly",
        "Statue - touch a creature, object, or surface to turn it to stone",
        "Steed - summon a spectral mount which can walk on air and water",
        "Summon - draw a known creature to you",
        "Swarm - trade favors with a colony of vermin",
        "Switch - touch to swap bodies with another",
        "Tadpole - keep your own mouth closed to allow a creature to breathe, regardless of environment",
        "Tripwire - a predefined illusory scene is triggered by an event of your choosing",
        "Unravel - pull the threads of a Ritual to uncast it, and recast it somewhere else",
        "Vapor - a noxious cloud fills a small area",
        "Voice - alter your voice or make it come from somewhere nearby",
        "Void - remain silent to prevent the casting of any Ritual in your presence",
        "Wail - produce a disorienting sound",
        "Wall - create a dense wall of fire, ice, stone, thorns, or water",
        "Ward - stay concentrating to protect a small area",
        "Web - produce webbing to cover a creature or reach something nearby",
        "Wither - reduce plants to ash and rot",
        "Writhe - transform sticks and branches into serpents which follow your command",
        "Yoke - apply the strength of a spectral bull to a situation",
    ]

    ARMOUR = [
        "Sturdy helmet",
        "Leather gambeson",
        "Ringmail shirt",
        "Studded gauntlets",
        "Full plate",
        "Ornate cuirass",
        "Wooden shield",
        "Amulet of protection",
        "Fae-crafted chainmail",
        "Stiff wool cloak",
        "Polished scalemail",
        "Rusty steel shield",
    ]

    WEAPONS = [
        "Simple shortsword ",
        "Hefty cudgel",
        "Gnarled staff ",
        "Hunting spear",
        "Masterwork longsword",
        "Bolt of arcane energy",
        "Twin-bladed battleaxe",
        "Knight's lance ",
        "Crushing warhammer",
        "Heavy crossbow",
        "Barbed whip",
        "Throwing hatchet ",
        "Set of throwing knives ",
        "Small but vicious dog",
        "Assassin's blowgun ",
        "Curved ritual knife",
        "Weighted net",
        "Hooked sickle sword",
        "Dueling sabre",
        "Thief catcher's bolas",
        "Guardian's halberd",
        "Spiked morningstar ",
        "Sharpened pitchfork",
        "Jagged sawtooth blade",
    ]
