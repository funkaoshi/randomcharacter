from dice import d

spells = [
    "Adhere",
"Anchor",
"Animate Object",
"Anthropomorphize",
"Arcane Eye",
"Astral Prison",
"Attract",
"Auditory Illusion",
"Babble",
"Bait Flower",
"Beast Form",
"Befuddle",
"Body Swap",
"Charm",
"Command",
"Comprehend",
"Cone of Foam",
"Control Plants",
"Control Weather",
"Cure Wounds",
"Deafen",
"Detect Magic",
"Disassemble",
"Disguise",
"Displace",
"Earthquake",
"Elasticity",
"Elemental Wall",
"Filch",
"Flare",
"Fog Cloud",
"Frenzy",
"Gate",
"Gravity Shift",
"Greed",
"Haste",
"Hatred",
"Hear Whispers",
"Hover",
"Hypnotize",
"Icy Touch",
"Identify Owner",
"Illuminate",
"Invisible Tether",
"Knock",
"Leap",
"Liquid Air",
"Magic Dampener",
"Manse",
"Marble Craze",
"Masquerade",
"Miniaturize",
"Mirror Image",
"Mirrorwalk",
"Multiarm",
"Night Sphere",
"Objectify",
"Ooze Form",
"Pacify",
"Phobia",
"Pit",
"Primal Surge",
"Push/Pull",
"Raise Dead",
"Raise Spirit",
"Read Mind",
"Repel",
"Scry",
"Sculpt Elements",
"Sense",
"Shield",
"Shroud",
"Shuffle",
"Sleep",
"Slick",
"Smoke Form",
"Sniff",
"Snuff",
"Sort",
"Spectacle",
"Spellsaw",
"Spider Climb",
"Summon Cube",
"Swarm",
"Telekinesis",
"Telepathy",
"Teleport",
"Target Lure",
"Thicket",
"Summon Idol",
"Time Control",
"True Sight",
"Upwell",
"Vision",
"Visual Illusion",
"Ward",
"Web",
"Widget",
"Wizard Mark",
"X-Ray Vision"
]

names = {
    'Male': [
        "Arwel","Bevan","Boroth","Borrid","Breagle","Breglor","Canhoreal","Emrys","Ethex","Gringle","Grinwit","Gruwid","Gruwth","Gwestin","Mannog","Melnax","Orthax","Triunein","Wenlan","Yirmeor",  
    ],
    'Female': [
        "Agune","Beatrice","Breagan","Bronwyn","Cannora","Drelil","Elgile","Esme","Griya","Henaine","Lirann","Lirathil","Lisabeth","Moralil","Morgwen","Sybil","Theune","Wenain","Ygwal","Yslen",
    ],
    'Surname': [
        "Abernathy","Addercap","Burl","Candlewick","Cormick","Crumwaller","Dunswallow","Getri","Glass","Harkness","Harper","Loomer","Malksmilk","Smythe","Sunderman","Swinney","Thatcher","Tolmen","Weaver","Wolder"
    ]
}

backgrounds = ["Alchemist","Blacksmith","Butcher","Burglar","Carpenter","Cleric","Gambler","Gravedigger","Herbalist","Hunter","Magician","Mercenary","Merchant","Miner","Outlaw","Performer","Pickpocket","Smuggler","Servant","Ranger"]

traits = {
    'physique': [
        "Athletic",
        "Brawny",
        "Flabby",
        "Lanky",
        "Rugged",
        "Scrawny",
        "Short",
        "Statuesque",
        "Stout",
        "Towering"
    ],
    'skin': ["Birthmark",
"Dark",
"Elongated",
"Pockmarked",
"Rosy",
"Round",
"Soft",
"Tanned",
"Tattooed",
"Weathered"],
    'hair': ["Bald",
"Braided",
"Curly",
"Filthy",
"Frizzy",
"Long",
"Luxurious",
"Oily",
"Wavy",
"Wispy"],
    'face': ["Bony",
"Broken",
"Chiseled",
"Elongated",
"Pale",
"Perfect",
"Rat-like",
"Sharp",
"Square",
"Sunken"],
    'speech': ["Blunt",
"Booming",
"Cryptic",
"Droning",
"Formal",
"Gravelly",
"Precise",
"Squeaky",
"Stuttering",
"Whispery"],
    'clothing': ["Antique",
"Bloody",
"Elegant",
"Filthy",
"Foreign",
"Frayed",
"Frumpy",
"Livery",
"Rancid",
"Soiled"],
    'virtue': ["Ambitious",
"Cautious",
"Courageous",
"Disciplined",
"Gregarious",
"Honorable",
"Humble",
"Merciful",
"Serene",
"Tolerant"],
    'vice': ["Aggressive",
"Bitter",
"Craven",
"Deceitful",
"Greedy",
"Lazy",
"Nervous",
"Rude",
"Vain",
"Vengeful"],
    'reputation': ["Ambitious",
"Boor",
"Dangerous",
"Entertainer",
"Honest",
"Loafer",
"Oddball",
"Repulsive",
"Respected",
"Wise"],
    'misfortune': ["Abandoned",
"Addicted",
"Blackmailed",
"Condemned",
"Cursed",
"Defrauded",
"Demoted",
"Discredited",
"Disowned",
"Exiled"]
}

expeditionary_gear = ["Air Bladder",
"Antitoxin",
"Cart (+4 slots, bulky)",
"Chain (10ft)",
"Dowsing Rod",
"Fire Oil",
"Grappling Hook",
"Large Sack",
"Large Trap",
"Lockpicks",
"Manacles",
"Pick",
"Pole (10ft)",
"Pulley",
"Repellent",
"Rope (25ft)",
"Spirit Ward",
"Spyglass",
"Tinderbox",
"Wolfsbane"]

tools_gear = [
    "Bellows",
    "Bucket",
    "Caltrops",
    "Chalk",
    "Chisel",
    "Cook Pots",
    "Crowbar",
    "Drill (Manual)",
    "Fishing Rod",
    "Glue",
    "Grease",
    "Hammer",
    "Hour Glass",
    "Metal File",
    "Nails",
    "Net",
    "Saw",
    "Sealant",
    "Shovel",
    "Tongs"
]

trinkets_gear = [
    "Bottle",
    "Card Deck",
    "Dice Set",
    "Face Paint",
    "Fake Jewels",
    "Horn",
    "Incense",
    "Instrument",
    "Lens",
    "Marbles",
    "Mirror",
    "Perfume",
    "Quill & Ink",
    "Salt Pack",
    "Small Bell",
    "Soap",
    "Sponge",
    "Tar Pot",
    "Twine",
    "Whistle"
]

class Details:
    """ Takes an empty character and adds Cairn Details."""
    def __init__(self, character):
        self.character = character
    
    def process(self):
        self.character.gender = 'Male' if d(2) < 2 else 'Female'
        self.character.name = "{0} {1}".format(names[self.character.gender][d(20) - 1], names["Surname"][d(20) - 1])
        self.character.background = backgrounds[d(20) - 1]
        self.character.age = d(20) + d(20) + 10
        for key in self.character.traits:
            self.character.traits[key] = traits[key][d(10) - 1]



class Attributes:
    def __init__(self, character):
        self.character = character
    
    def process(self):
        self.character.attributes['STR'] = d(6) + d(6) + d(6)
        self.character.attributes['DEX'] = d(6) + d(6) + d(6)
        self.character.attributes['WIL'] = d(6) + d(6) + d(6)
        self.character.hp = d(6)

class Inventory:
    def __init__(self, character):
        self.character = character

    def roll_armor(self):
        armor_roll = d(20)
        if armor_roll > 3:
            if armor_roll > 14:
                if armor_roll > 19:
                    self.character.inventory['slots'].append("Plate*")
                    self.character.armor = 3
                else:
                    self.character.inventory['slots'].append("Chain*")
                    self.character.armor = 2
            else:
                self.character.inventory['slots'].append("Brigandine*")
                self.character.armor = 1
        
    def roll_helm_shield(self):
        helm_shield_roll = d(20)
        if helm_shield_roll > 13:
            if helm_shield_roll > 16:
                if helm_shield_roll > 19:
                    self.character.inventory['slots'].append("Shield")
                    self.character.armor += 1
                    self.character.inventory['slots'].append("Helm")
                    self.character.armor += 1
                else:
                    self.character.inventory['slots'].append("Shield")
                    self.character.armor += 1
            else:
                self.character.inventory['slots'].append("Helm")
                self.character.armor += 1

    def roll_weapon(self):
        weapon_roll = d(20)
        if weapon_roll > 5:
            if weapon_roll > 14:
                if weapon_roll > 19:
                    self.character.inventory['slots'].append(["Halberd*", "War Hammer*", "Battleaxe*"][d(3) - 1])
                else:
                    self.character.inventory['slots'].append(["Bow*", "Crossbow*", "Sling"][d(3) - 1])
            else:
                self.character.inventory['slots'].append(["Sword", "Mace", "Axe"][d(3) - 1])
        else:
            self.character.inventory['slots'].append(["Dagger", "Cudgel", "Staff"][d(3) - 1])
        
    def roll_expeditionary_gear(self):
        expeditionary_roll = d(20)
        self.character.inventory['slots'].append(expeditionary_gear[expeditionary_roll - 1])

    def roll_tools(self):
        tools_roll = d(20)
        self.character.inventory['slots'].append(tools_gear[tools_roll - 1])

    def roll_trinkets(self):                
        trinkets_roll = d(20)
        self.character.inventory['slots'].append(trinkets_gear[trinkets_roll - 1])

    def roll_spellbook(self):
        spellbook_roll = d(100)
        self.character.inventory['slots'].append("Spellbook ({0})".format(spells[spellbook_roll - 1]))

    def process(self):
        self.character.inventory['money'] = "{0}gp".format(d(6) + d(6) + d(6))
        self.roll_weapon()
        self.roll_armor()
        self.roll_helm_shield()
        self.character.inventory['slots'].append("3 Days' Rations")
        self.character.inventory['slots'].append("Torch")
        self.roll_expeditionary_gear()
        self.roll_tools()
        self.roll_trinkets()
        bonus_roll = d(20)
        if bonus_roll > 5:
            if bonus_roll > 13:
                if bonus_roll > 17:
                    self.roll_spellbook()
                else:
                    self.roll_armor() if d(2) < 2 else self.roll_weapon()
            else:
                self.roll_expeditionary_gear()
        else:
            self.roll_tools() if d(2) < 2 else self.roll_trinkets()
        

class Character(object):
    """
    Builds a Cairn Character
    """
    def to_dict(self):
        attributes = vars(self)
        return attributes
        

    def __init__(self):
        self.system = 'cairn'
        self.gender = None
        self.name = ''
        self.background = ''
        self.age = None
        self.hp = 0
        self.armor = 0
        self.traits = {
            'physique': '',
            'skin': '',
            'hair': '',
            'face': '',
            'speech': '',
            'clothing': '',
            'virtue': '',
            'vice': '',
            'reputation': '',
            'misfortune': ''
        }
        self.attributes = {
            'STR': 0,
            'DEX': 0,
            'WIL': 0,
        }
        self.inventory = {
            'slots': [],
            'money': 0
        }

        processors = [Details, Attributes, Inventory]

        for processor in processors:
            processor(self).process()

