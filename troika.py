import itertools
import random

import mixins
import dice


class Character(mixins.AppearanceMixin):

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)

        # Attributes
        self.skill = dice.d(3) + 3
        self.stamina = dice.xdy(2, 6) + 12
        self.luck = dice.d(6) + 6
        self.appearance = self.get_appearance()

        # Pick a Background
        background = random.choice(self.BACKGROUNDS)

        self.background = background['name'][3:]
        self.description = background['description']
        self.special = background['special']

        # Pick one of the "ORs" for possessions when picking equipment
        self.equipment = [
            random.choice(equipment.split(' OR '))
            for equipment in background['possessions']
        ] + [
            # Add default equipment
            'Knife',
            'Lantern and a flask of oil',
            'Rucksack',
            '6 provisions',
            '%d silver pennies' % dice.xdy(2,6),
        ]

        # Turn random spells into actual spells when picking skills
        self.skills = [
            skill.replace('Random (Table 5)', random.choice(self.MAGIC_SPELLS))
            for skill in background['skills']
        ]

        # Fix some gender issues
        if 'Female' in self.appearance and self.background == 'Lonesome King':
            self.background = 'Lonesome Queen'
        elif self.background == 'Rhino-Man':
            self.appearance = self.appearance.replace('Female, ', '')
            self.appearance = self.appearance.replace('Male, ', '')
        elif self.background == 'Parchment Witch':
            self.appearance = self.appearance.replace('Male', 'Female')

    BACKGROUNDS = [
        {
            "skills": [
                "4 Strength",
                "3 Astrology",
                "2 Run",
                "2 Climb"
            ],
            "special": "",
            "name": "11 Ardent Giant of Corda",
            "possessions": [
                "An artefact of Lost Corda, being either an enormous blue star map which can tell where any portal leads with a successful Astrology test or a pocket barometer for telling the weather (5 in 6 accuracy) or a ruby lorgnette offering +2 Second Sight while worn."
            ],
            "description": "Every giant has a different story about Corda, well told and interrupted with tears and laughter, of how they lost it and mean to find it soon enough but oh, what of today? We should drink and cheer, we'll search again in the morning!"
        },
        {
            "skills": [
                "3 Spell -  Drown",
                "3 Swim",
                "2 Spell - Tongue Twister",
                "2 Spell - Undo",
                "1 Spell - Web",
                "1 Sneak",
                "1 Second Sight"
            ],
            "special": "You may drink stagnant water without harm.",
            "name": "12 Befouler of Ponds",
            "possessions": [
                "Sackcloth robes, caked in stinking mud and undergrowth. +1 to Sneak rolls in marshy terrain while wearing them, -1 everywhere else 'cos it stinks!",
                "A large wooden ladle (Damage as mace)."
            ],
            "description": "You're a wise man, a high priest, a pond-pisser, a typical but committed adherent of P!P!Ssshrp. The bloated toad god has no church other than the periphery of ponds where the foulness catches in the reeds, and no congregation other than the gnats and dragonflies. You minister to them all the same."
        },
        {
            "skills": [
                "2 Sneak",
                "2 Locks",
                "1 Awareness",
                "1 Climb",
                "1 Trapping",
                "1 Knife Fighting",
                "1 Crossbow Fighting"
            ],
            "special": "You may Test your Luck to find and get in with the local criminal underbelly if one exists.",
            "name": "13 Burglar",
            "possessions": [
                "Crossbow and 18 bolts.",
                "Roll of lock picks.",
                "Grappling hook."
            ],
            "description": "As a second-story man you often have cause to wander. Enemies come naturally from both sides of the law and it pays to keep ahead of trouble."
        },
        {
            "skills": [
                "2 Fusil Fighting",
                "2 Astrology",
                "2 Second Sight",
                "2 Spell - Random (Table 5)",
                "2 Spell - Random (Table 5)",
                "2 Golden Barge Pilot",
                "1 Spell - Random (Table 5)",
                "1 Sword Fighting"
            ],
            "special": "",
            "name": "14 Cacogen",
            "possessions": [
                "Fusil.",
                "2d6 plasmic cores.",
                "Sword.",
                "Velare."
            ],
            "description": "You are Those-Filthy-Born, spawned in the hump-backed sky lit only by great black anti-suns and false light. Your mother was sailing on the golden barges or caught in some more abstract fate when she passed you, far from the protective malaise of the million spheres. You were open to the power and the glory at a generative time and it shows in your teratoid form."
        },
        {
            "skills": [
                "6 Language - Kurgan",
                "3 Maul Fighting",
                "3 Secret Signs - Chaos Patron",
                "1 Spell - Random (Table 5)",
                "1 Second Sight"
            ],
            "special": "Name your patron. You may call upon your patron for aid once per day. To do so roll three 6s on 3d6. The GM will interpret their intervention.",
            "name": "15 Chaos Champion",
            "possessions": [
                "Ritual scars.",
                "A huge maul.",
                "Assortment of ragged armour (counts as Modest Armour).",
                "Dream journal, almost full."
            ],
            "description": "You no longer have the spiked brass armour but you still have the ear of your Chaos patron. They're happy for you to experiment with not plunging your world into disorder and, ultimately, darkness, but the door is always open."
        },
        {
            "skills": [
                "4 Locks",
                "3 Strength",
                "3 Trapping",
                "2 Spell - Open",
                "1 Spell - See Through",
                "1 Sledgehammer Fighting",
                "1 Spell - Lock"
            ],
            "special": "",
            "name": "16 Claviger",
            "possessions": [
                "Festooned with keys (counts as Modest Armour).",
                "A sledgehammer.",
                "Lock picking tools."
            ],
            "description": "The key masters wander the universe fathoming the workings of all entry ways they can find. Though they're quite fascinated with simple chests and doors they are most excited by metaphysical and metaphorical barriers. You might find small conclaves of clavigers camped around the feet of demon gates, debating appropriate methods of attack or building obscure machines of entry."
        },
        {
            "skills": [
                "5 Language - Abyssal",
                "3 Spell - Blood Shroud",
                "2 Second Sight",
                "2 Sword Fighting",
                "2 Bow Fighting",
                "1 Tracking",
                "1 Sneak"
            ],
            "special": "",
            "name": "21 Demon Stalker",
            "possessions": [
                "A silver sword.",
                "16 silver arrows and a bow.",
                "Pouch of salt.",
                "Vial of demon blood."
            ],
            "description": "You stake your reputation upon your ability to hunt and kill demonic creatures and those who break bread with them. Goat men in the wilds or the angel cults of the slums, all need to be driven back off the edge of the map and into the shores of chaos."
        },
        {
            "skills": [
                "3 Awareness",
                "2 Sculpting",
                "2 Painting",
                "2 Metalworking",
                "2 Construction",
                "2 Strength",
                "2 Fist Fighting",
                "2 Wrestling",
                "1 Hammer Fighting"
            ],
            "special": "Dwarfs may eat gems and rare metals as a food replacement. You in fact far prefer the taste of rare minerals to mundane food. Dwarfs are genderless. You are immune to all compulsions that play on a creature's desire for the opposite sex. This also means you don't have sexual organs. Instead of urinating you excrete through sweating, thus explaining your odour.",
            "name": "22 Dwarf",
            "possessions": [
                "Masonry hammer (Damage as mace).",
                "Roll of artist's supplies."
            ],
            "description": "You are a short, hairy, belligerent, alcohol dependent creature. The latter two may be linked but you'll fight anyone who suggests as much. Since there are no dwarf women (or men, technically) there are no dwarf children or dwarf families, so you can fully commit yourself to the important dwarfy endeavours of creating fine art in unusual places. You intend to find the most unusual places ever seen in all the million spheres."
        },
        {
            "skills": [
                "2 Awareness",
                "2 Evaluate",
                "1 Second Sight",
                "1 Etiquette",
                "1 Fist Fighting",
                "1 Run"
            ],
            "special": "Epopts may Test their Luck to get a yes or no answer to a question about mundane matters. The GM should make this Test in private, not informing the epopt if they are accurate.",
            "name": "23 Epopt",
            "possessions": [
                "Yellow epopt outfit, padded for protection against unhappy clients (counts as Modest Armour).",
                "Epopt staff, being a walking staff with seeing crystal on one end (Damage as staff).",
                "Collapsible tent, big enough for your stall."
            ],
            "description": "You are a roaming seer, selling your visions at courts and fetes. You are instantly recognisable by your yellow coif and habit as being open for business. Road weary and worldwise, your unpopular visions cause you to constantly move on."
        },
        {
            "skills": [
                "6 Language - Weird Exotic Language",
                "3 in the Fighting Skill of your weird weapon",
                "2 Language - local language",
                "2 Spell - Random (Table 5)",
                "1 Astrology",
                "1 Etiquette"
            ],
            "special": "",
            "name": "24 Exotic Warrior",
            "possessions": [
                "A weird and wonderful weapon.",
                "Strange clothes.",
                "Exciting accent.",
                "A tea set or 3 pocket gods or astrological equipment."
            ],
            "description": "No one has heard of your homeland. Your habits are peculiar, your clothes are outrageous, and in a land jaded to the outlandish and new you still somehow manage to stand out."
        },
        {
            "skills": [
                "3 Mathmology",
                "2 Astrology",
                "2 Spell - Find"
            ],
            "special": "",
            "name": "25 The Fellowship of Knidos",
            "possessions": [
                "Large astrolabe (Damage as mace).",
                "Abacus.",
                "Lots of scrolls and writing equipment."
            ],
            "description": "Mathmologists honour the clean and unambiguous truths of mathematics and coordinate them with their observation of the multiverse. All things can be measured and predicted with the application of the correct mathmological ratios, those methods applied to penetrate the ethereal surface to glimpse the fundamental numbers below."
        },
        {
            "skills": [
                "4 Strength",
                "2 Fist Fighting",
                "2 Run",
                "1 Hook Fighting",
                "1 Sneak",
                "1 Awareness"
            ],
            "special": "",
            "name": "26 Compeer of the Fellowship of Porters & Basin Fillers",
            "possessions": [
                "A wooden yoke.",
                "Brown overcoat and soft doffing cap of the guild.",
                "A bale hook--counts as a knife for Damage and gains you a +1 on rolls to lift heavy objects.",
                "Length of rope."
            ],
            "description": "Luggers are a servile group by nature, most often found in the service of others, weighed down by loads that would buckle a donkey. You take pride in that, maybe so much so that the everyday assignments of the guild could not sate your desire to serve, causing you to venture out in search of a real challenge for such a talented varlet."
        },
        {
            "skills": [
                "4 Tunnel Fighting",
                "4 Trapping",
                "2 Sneak",
                "2 Awareness",
                "2 Club Fighting",
                "2 Tracking",
                "1 Swim"
            ],
            "special": "",
            "name": "31 Gremlin Catcher",
            "possessions": [
                "Small but vicious dog.",
                "Flat cap.",
                "A club.",
                "A sack.",
                "1d6 empty gremlin jars.",
                "A jar with a pissed off gremlin inside."
            ],
            "description": "No matter what country, sphere, or abstract dimension you may find yourself in be assured that gremlins will be there digging their warrens and bothering nice people willing to pay you a shiny penny to bash their little heads in."
        },
        {
            "skills": [
                "1 Poison",
                "1 Sneak",
                "1 Locks",
                "1 Knife Fighting",
                "1 Climb",
                "1 Awareness",
                "1 Crossbow Fighting",
                "1 Swim",
                "1 Disguise"
            ],
            "special": "",
            "name": "32 Journeyman of the Guild of Sharp Corners",
            "possessions": [
                "Black clothes of the apprentice.",
                "Garrotte.",
                "Curved sword.",
                "3 vials of poison.",
                "Crossbow and 6 bolts."
            ],
            "description": "You are an assassin in training, graduated from fighting dummies and branding practise clients, freshly imbued with a license to ply your trade. You haven't fully developed the idiosyncratic methods required of a master but you are on the path."
        },
        {
            "skills": [
                "2 Greatsword Fighting",
                "2 Pistolet Fighting",
                "1 Run",
                "1 Fist Fighting",
                "1 Astrology"
            ],
            "special": "",
            "name": "33  Lansquenet",
            "possessions": [
                "Exquisite pistolet.",
                "Bandolier containing 18 plasmic cores.",
                "Greatsword.",
                "Brightly coloured clothing with lots of tassels and bells (impossible to sneak). Though frivolous looking, it is in fact built with the Autarch's divine alchemy and considered Modest Armour while weighing the same as normal clothing (takes no slots in your inventory)."
            ],
            "description": "You were a mercenary retained in the exclusive service of the Phoenix Throne, handsomely paid and sent to distant spheres on golden ships to spread the ineffable glory of your paymaster at the tip of your flaming lance."
        },
        {
            "skills": [
                "3 Etiquette",
                "3 Weapon Fighting in the weapon of your choice",
                "3 Ride",
                "1 Tracking"
            ],
            "special": "",
            "name": "34 Lonesome Monarch",
            "possessions": [
                "A nice weapon of your choice.",
                "A crown.",
                "A tired horse."
            ],
            "description": "You were the ruler of all you surveyed, a great conqueror, a lawbringer! Unfortunately your horse sped off into the pixie forest, or the court magician ensured you disappeared, or you led a sortie into the stars to put your stamp on them as well. Either way you are now a lost and lonely sovereign without a kingdom--no one has heard of you or your people. Most don't believe you and laugh, or worse, they do believe you and shrug at the vagaries of fate."
        },
        {
            "skills": [
                "3 Etiquette",
                "1 Strength",
                "1 Tracking",
                "1 Trapping",
                "1 Gastrology"
            ],
            "special": "Eaters are immune to mundane ingested poisons. They may also identify any object if eaten, gaining knowledge of its material, its origin (if plausibly familiar), and its magical properties on a successful Testtest of Gastrology, though the object must be thoroughly masticated, not merely swallowed and passed. This does not grant special immunity to any effects the object may possess.",
            "name": "35 Member of Miss Kinsey's Diner's Club",
            "possessions": [
                "Sharp metal dentures (Damage as sword) or forked metal dentures (Damage as knife, but on a Critical Hit you may cleanly strip all the flesh from one small appendage) or blunt metal dentures (Damage as knife but may be used to eat hard objects).",
                "Embroidered napkin."
            ],
            "description": "The Eaters know that there are only two worlds: the Without and the Within. They intend to insert as much of the prior into the latter as they can while experiencing the finest delights available. All culinary experience is open to them as nothing is forbidden at Miss Kinsey's. Try the other, other, other white meat."
        },
        {
            "skills": [
                "4 Climb",
                "2 Trapping",
                "1 Club Fighting",
                "1 Knife Fighting"
            ],
            "special": "",
            "name": "36 Monkeymonger",
            "possessions": [
                "Monkey club.",
                "Butcher's knife.",
                "1d6 small monkeys that do not heed commands but are too scared and hungry to travel far from you.",
                "A pocket full of monkey treats."
            ],
            "description": "Life on The Wall is hard. One is never more than a few yards from an endless fall yet those precarious villages still need to eat. This is where you come in with your Edible Monkeys (the distinction is purely for appeal since all monkeys are of course edible). You used to spend days on end dangling your feet off the edge of the world, watching over your chittering livestock while they scampered hither and thither, but there was no future in monkey meat. You wanted much more, and so stepped off. Or you fell off. Either way, you and some unlucky monkeys are here now and that's all that matters."
        },
        {
            "skills": [
                "2 Heal",
                "1 Spell - Posthumous Vitality",
                "1 Spell - Skeletal Counsel",
                "1 Spell - Torpor",
                "1 Sneak"
            ],
            "special": "",
            "name": "41 Necromancer",
            "possessions": [
                "Dusty robes.",
                "The skull of your master or a zombie servant or a ghost with whom you have developed a codependent relationship."
            ],
            "description": "The least popular of magical practitioners, necromancers are shunned by the major centres of learning, left to their own devices on the edges of society, passing on knowledge in the time honoured master-student dynamic. This loneliness encourages students to make their own friends."
        },
        {
            "skills": [
                "2 Spell - Protection From Rain",
                "2 Spell - Callous Strike",
                "2 Spell - Quench",
                "2 Spell - True Seeing",
                "2 Disguise",
                "2 Second Sight",
                "1 Healing",
                "1 Spell - Undo",
                "1 Spell - Random (Table 5)"
            ],
            "special": "You are undead, so you do not need to breathe, circulate blood, and so on. You take double Damage from silver weapons and regain Stamina half as effectively from all sources. You must Test your Luck if outside in the rain, are made wet, are close to open flames, or suffer generally grievous wounds. A failure will see your skin ruined. While your skin is damaged, you are very obviously a walking corpse.",
            "name": "42 Parchment Witch",
            "possessions": [
                "d6 rolls of parchment.",
                "Vials of pigments and powders.",
                "A collection of brushes.",
                "A wicked knife."
            ],
            "description": "You are known for your smooth skin, midnight gatherings and being fearful of rain and open flames. The Parchment Witches are long dead sorcerers who cannot give up the vanity of living and so cover themselves in perfect paper skin, a patiently painted and folded imitation of life meant to hide ancient bone and gristle."
        },
        {
            "skills": [
                "3 Fist Fighting",
                "3 Awareness",
                "2 Strength",
                "2 Wrestling",
                "2 Axe Fighting"
            ],
            "special": "Dwarfs may eat gems and rare metals as a food replacement. You in fact far prefer the taste of rare minerals to mundane food. Dwarfs are genderless. You are immune to all compulsions that play on a creature's desire for the opposite sex. This also means you don't have sexual organs. Instead of urinating you excrete through sweating, thus explaining your odour. Other dwarfs will completely ignore you as though you were a piece of furniture or somebody's abandoned hat. Very occasionally they may openly examine and comment thoughtfully to themselves on your unforgivable flaws, possibly while marking areas for improvement on your body with a grease pen. To non-dwarfy eyes you probably look like any other dwarf. +4 sneak vs dwarfs.",
            "name": "43 Poorly Made Dwarf",
            "possessions": [
                "Woodsman's axe.",
                "An empty firkin."
            ],
            "description": "Dwarfs are known for being the finest artisans of the million spheres. Give a dwarf a rock and they will make gold, give a dwarf a boulder and they will make a dwarf. You were supposed to be the finest expression of dwarfy craftsmanship, a masterpiece, a brand new dwarf like those made by the old masters, but you were imperfect and abandoned."
        },
        {
            "skills": [
                "3 Jousting",
                "2 Sword Fighting",
                "2 Spear Fighting",
                "1 Shield Fighting",
                "1 Awareness"
            ],
            "special": "",
            "name": "44 Questing Knight",
            "possessions": [
                "Heavy Armour.",
                "A horse.",
                "Lance (as spear).",
                "Sword.",
                "Shield.",
                "A never ending quest."
            ],
            "description": "You are on a quest for the grail, or the sword, or the throne, or for god, or a lost love, or some other significant object. Your sort are common enough, wandering the worlds, acting out your romantic melodrama, accusing good folk of being demons or faeries. Questing Knights are generally considered to be harmless."
        },
        {
            "skills": [
                "2 Spell - Ember",
                "2 Spell - Fire Bolt",
                "2 Spell - Flash",
                "2 Great Axe Fighting",
                "1 Second Sight",
                "1 Spell - Exorcism"
            ],
            "special": "",
            "name": "45 Red Priest",
            "possessions": [
                "Red robes.",
                "Traditional faceless metal helmet of your order (Modest Armour).",
                "Symbolic (but fully sized and fully functional) single headed great axe, to help batter down the door to sin (Damage as greatsword)."
            ],
            "description": "You are an evangelist of the Red Redemption, wandering confessor, cauterizer of the wound of sin, sin being the accumulation and recreational consumption of mass. How can your spirit fly free while shackled and flabby?"
        },
        {
            "skills": [
                "3 Glaive Fighting",
                "2 Run",
                "2 Strength",
                "1 Gambling"
            ],
            "special": "",
            "name": "46 Rhino-Man",
            "possessions": [
                "Horn (Damage as dagger).",
                "Thick Skin (Rhino Men always count as being Modestly Armoured).",
                "Glaive (Damage as polearm).",
                "Knuckle dice.",
                "Half full firkin of Rhino-beer (20 rations worth)."
            ],
            "description": "The original Rhino-Men were created by an insane sorcerer several centuries ago but rebelled and killed him. They are fairly rare creatures, serving as formidable and loyal guards to those who can afford their services."
        },
        {
            "skills": [
                "3 Fly",
                "3 Spell - Random (Table 5)",
                "3 Spell - Random (Table 5)",
                "3 Spell - Random (Table 5)",
                "2 Claw Fighting",
                "1 Hoof Fighting"
            ],
            "special": "",
            "name": "51 Sceptical Lammasu",
            "possessions": [
                "Incidental sacred jewellery worth 10d6 pence if traded.",
                "Peaked hat.",
                "Claws (Damage as swords).",
                "Hooves (Damage as clubs).",
                "Wings--able to fly as fast as a running man over clear ground."
            ],
            "description": "With the body of a bull, the head of a man, the forelegs of a cat and the wings of a swan, you are the sweetest of the children of the gods. You, however, were not content to rest on your cloud and instead descended from the heavens (or crawled up from the abyss) and set upon finding your own path among the stars."
        },
        {
            "skills": [
                "3 Astrology",
                "2 Second Sight",
                "2 Spell - Astral Reach",
                "1 Spell - Teleport",
                "1 Spell - Web",
                "1 Spell - Random (Table 5)",
                "1 Spell - Random (Table 5)",
                "1 Spell - Random (Table 5)"
            ],
            "special": "",
            "name": "52 Sorcerer of the Academy of Doors",
            "possessions": [
                "A small functional door worn on your forehead, through which you channel your magic.",
                "Flashy robes."
            ],
            "description": "As a student at Troika's very own wizarding academy, pride of the city, experts in pan-dimensional mobility, you were able to penetrate the (2d6)th door. You are no master, certainly, but few outside your peers can claim to know more about the vagaries of skyward travel than you."
        },
        {
            "skills": [
                "4 Secret Signs - Witching Words",
                "2 Run",
                "1 Climb",
                "1 Sleight of Hand",
                "1 Swim",
                "1 Sneak",
                "1 Second Sight",
                "1 Spell - Jolt",
                "1 Spell - Amity",
                "1 Spell - Mirror Selves",
                "1 Spell - Protection from Rain",
                "1 Spell - Helping Hands",
                "1 Spell - Purple Lens",
                "1 Spell - Random (Table 5)"
            ],
            "special": "",
            "name": "53 Sorcerer of the College of Friends",
            "possessions": [
                "Pointed wizard hat you received at graduation.",
                "Pocket full of wizard biscuits (2d6, each counts as a provision).",
                "Wand used to help focus new apprentices, now kept for sentimental reasons."
            ],
            "description": "You were trained in the sub-dimensional academy of the Cordial Wizard God. You spent your childhood learning about the fate of pixies, the colour of magic, ritual grammar and endless other theoretical topics. Now you're out in the world, discovering that your education hardly accounted for any of the things that you've seen."
        },
        {
            "skills": [
                "2 in a Fighting Skill of your choice",
                "2 Wrestling",
                "2 Swim",
                "2 Climb",
                "2 Run",
                "2 Fist Fighting"
            ],
            "special": "",
            "name": "54  Fellow of The Sublime Society of Beef Steaks",
            "possessions": [
                "A weapon of choice.",
                "A small gridiron.",
                "2kg of premium meat cuts.",
                "Waistcoat.",
                "Bottle of strong but fancy wine."
            ],
            "description": "Brawlers believe the application of might and a good beef steak is the universal truth. Words do not have power. Words can no more define the universe than they can build a house, lift a cup, or sear a steak. Might can! Really, they have thought a lot about this."
        },
        {
            "skills": [
                "3 Awareness",
                "2 Blacksmithing",
                "1 Sword Fighting",
                "1 Greatsword Fighting"
            ],
            "special": "The blessing of Telak awards you Armour equal to half (rounded down) the number of swords you carry. So if you were carrying 6 swords your armour would be 3, while if you carried 9 it would be 4. You must be overtly armed at all times or else Telak will take this blessing away until you forge, and donate to the unarmed, a brand new sword.",
            "name": "55 Temple Knight of Telak the Swordbringer",
            "possessions": [
                "The blessing of Telak.",
                "6 swords of your choice."
            ],
            "description": "You were once (and possibly still are) a fanatical monk set to maintain constant martial readiness in preparation for the end times, when all doorways crumble inwards. You are never unready and always have spares."
        },
        {
            "skills": [
                "3 Spell - Undo",
                "2 Spell - Assume Shape",
                "2 Spell - Thunder",
                "2 Spell - Random (Table 5)",
                "1 Spell - Brittle Twigs",
                "1 Spell - Random (Table 5)",
                "1 Second Sight",
                "1 Astrology"
            ],
            "special": "You may Test your Luck to just so happen to have exactly the (common) mystical nicknack the situation requires.",
            "name": "56 Thaumaturge",
            "possessions": [
                "Thaumaturgic fez.",
                "Staff, bedecked with charms and bells. May reroll one die on the Oops! Table if using this staff, however, may never sneak up on anyone because of the ringing and clattering it makes.",
                "Curled shoes.",
                "Voluminous robes"
            ],
            "description": "Wandering miracle workers, the depths of whose clothes are filled with pouches of unguents, holy icons and herbs. No matter the metaphysical need, you are always prepared."
        },
        {
            "skills": [
                "3 Golden Barge Pilot",
                "2 Astrology",
                "2 Pistolet Fighting",
                "2 Healing",
                "1 Run",
                "1 Strength",
                "1 Cooking"
            ],
            "special": "You don't recover Stamina by resting in the usual manner--instead you have to spend an evening with a hot iron melting your skin back together like putty. For each hour of rest with access to the right tools you regain 3 Stamina. You may recharge plasmic machines by hooking your fluids to them and spending Stamina at a rate of 1 Stamina and 6 minutes per charge. You always count as being at least Lightly Armoured.",
            "name": "61 Thinking Engine",
            "possessions": [
                "Soldering iron.",
                "Detachable autonomous hands or centaur body (+4 Run) or inbuilt particle detector (+4 Second Sight) or one random Spell at rank 3."
            ],
            "description": "Your eyes are dull ruby spheres, your skin is hard and smooth like ivory but brown and whorled like wood. You are clearly damaged, you have no memory of your creation or purpose, and some days your white internal juices ooze thickly from cracks in your skin."
        },
        {
            "skills": [
                "3 Longsword Fighting",
                "1 Awareness",
                "1 Climb",
                "1 Bow Fighting",
                "1 Run",
                "1 Swim"
            ],
            "special": "",
            "name": "62 Vengeful Child",
            "possessions": [
                "A too-big sword that provides +1 to Longsword Fighting and Damage while using it. Only you may benefit from this bonus; it's not magic, just sentimental.",
                "An old hunting bow and 12 arrows."
            ],
            "description": "Your village was burnt down by ruffians, or your mother was beheaded by snake cultists, or your father was hung by corrupt officials. Either way you took umbrage and entered the world with a chip on one shoulder and an oversized sword on the other."
        },
        {
            "skills": [
                "2 Evaluate",
                "2 Astrology",
                "1 Healing",
                "1 Spell - Random (Table 5)",
                "1 Sword Fighting",
                "1 Sleight of Hand"
            ],
            "special": "You may Test your Luck to recall facts that you might reasonably be expected to have encountered relating to the natural sciences and humanities.",
            "name": "63 Venturesome Academic",
            "possessions": [
                "Reading glasses in a sturdy case (you cannot read without them).",
                "Small sword.",
                "Bundle of candles and matches.",
                "Writing materials.",
                "Journal."
            ],
            "description": "You're a classically trained academic, a product of the universities of the Brass City, the Palace of Tigers or some other less prestigious centre of learning."
        },
        {
            "skills": [
                "2 Tracking",
                "2 Disguise",
                "2 Crossbow Fighting",
                "1 Sword Fighting",
                "1 Sneak",
                "1 Locks",
                "1 Etiquette"
            ],
            "special": "",
            "name": "64 Wizard Hunter",
            "possessions": [
                "Large sack.",
                "Witch-hair rope.",
                "Crossbow and 12 bolts.",
                "Sword.",
                "1d6 pocket gods.",
                "Ruby lorgnette."
            ],
            "description": "Some people say man is the most dangerous prey. They're wrong. Can men ignite the air and freeze your blood? Can men turn into flocks of seagulls when cornered in an alley? No, they can't. Wizards are the most dangerous prey."
        },
        {
            "skills": [
                "4 Weapon Fighting Skill of choice",
                "2 Etiquette",
                "1 Healing"
            ],
            "special": "",
            "name": "65 Yongardy Lawyer",
            "possessions": [
                "Rapier (Damage as sword) and puffy shirt or sjambok (Damage as club) and lots of scars or longsword and Heavy Armour or hammer (Damage as mace) and huge shield.",
                "Manual on Yongardy Law.",
                "Barrister's wig."
            ],
            "description": "Down in Yongardy they do things differently. They respect the law. Every day there is a queue outside the courts to get a seat to see the latest up and coming barrister defend their case with three feet of steel. The people follow the careers of their favourite solicitors, watch all their cases, collect their portraits and sneak into the court after hours to dab the patches of blood on white handkerchiefs. In Yongardy, they love the law."
        },
        {
            "skills": [
                "3 Climb",
                "3 Run",
                "2 Strength",
                "2 Fist Fighting",
                "2 Club Fighting",
                "2 Wrestling"
            ],
            "special": "You are immune to all mind altering effects. You are able to speak but usually choose not to. When making advancement checks in skills related to abstract thought, such as Spells or Astrology, you must roll twice and succeed on both or else fail.",
            "name": "66 Zoanthrop",
            "possessions": [
                "No starting possessions; you have thrown off the shackles of civilisation. You are also probably nude."
            ],
            "description": "At some point in your past you decided you didn't need it anymore. You found a zoanthropologist and paid them well to remove your troublesome forebrain and so elevate you to the pure and unburdened beast you are today."
        }
    ]

    MAGIC_SPELLS = [
        "Assassin's Dagger",
        "Animate",
        "Affix",
        "Assume Shape",
        "Befuddle",
        "Breach",
        "Cone of Air",
        "Banish Spirt",
        "Ember",
        "Cockroach",
        "Darksee",
        "Diminish",
        "Earthquake",
        "Fear",
        "Fire Bolt",
        "Flash",
        "Farseeing",
        "Find",
        "Grow",
        "Hurricane",
        "Helping Hands",
        "Illusion",
        "Invisibility",
        "Jolt",
        "Light",
        "Lock",
        "Languages",
        "Levitate",
        "Sentry",
        "Shatter",
        "Sleep",
        "Thunder",
        "Tongue Twister",
        "Undo",
        "Ward",
        "Wall of Power",
    ]
