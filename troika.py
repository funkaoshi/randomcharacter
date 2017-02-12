import itertools
import random

import mixins
import dice


class Character(mixins.AppearenceMixin):

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(*args, **kwargs)

        # Attributes
        self.skill = dice.d(3) + 3
        self.stamina = dice.xdy(2,6) + 12
        self.luck = dice.d(6)+ 6

        # Pick a Background
        background = random.choice(self.BACKGROUNDS)

        self.background = background['name'][3:]
        self.description = background['description']
        self.special = background['special']

        # Pick one of the "ORs" for possessions when picking equipment
        self.equipment = [
            random.choice(equipment.split(' OR '))
            for equipment in background['possesions']
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
            "possesions": [
                "An artefact of Lost Corda, being either an enormous blue star map offering +1 astrology when studied for 12 minutes OR A contraption for telling the weather (5 in 6 accuracy) OR A ruby lorgnette offering +1 Second Sight while worn"
            ],
            "description": "Every giant has a different story about Corda, well told and interrupted with bouts of hysterical crying and laughter, of how they lost it and mean to find it soon enough but oh, what of today? We should drink and cheer, I'll search again in the morning!"
        },
        {
            "skills": [
                "3 Spell - Drown",
                "3 Swim",
                "2 Spell - Tongue Twister",
                "2 Spell - Undo",
                "1 Spell - Web",
                "1 Sneak",
                "1 Second Sight"
            ],
            "special": "May drink stagnant water without harm",
            "name": "12 Befouler of Ponds",
            "possesions": [
                "Sackcloth robes, caked in stinking mud and undergrowth. +1 to Sneak rolls in marshy terrain while wearing it, -1 everywhere else \u2018cos it stinks",
                "A large wooden ladle (damage as mace)"
            ],
            "description": "You're a wise man, a high priest, a pond-pisser, a typical but committed adherent of P!P!Ssshrp. The bloated toad god has no church other than the periphery of ponds where the foulness catches in the reeds and no congregation other than the gnats and dragonflies. You minister to them all the same."
        },
        {
            "skills": [
                "2 Sneak",
                "2 Locks",
                "1 Awareness",
                "1 Climb",
                "1 Trapping",
                "1 Knife fighting",
                "1 Crossbow fighting"
            ],
            "special": "You may test your luck to find and get in with the local criminal underbelly, if one exists.",
            "name": "13 Burglar",
            "possesions": [
                "Crossbow & 18 bolts",
                "Roll of lock picks",
                "Grappling hook"
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
            "possesions": [
                "Fusil",
                "2d6 plasmic cores",
                "Sword",
                "Velare"
            ],
            "description": "Those filthy born, spawned in the hump-backed sky lit only by great black anti-suns and false light. Your mother was sailing on the golden barges or caught in some more abstract fate when she passed you, far from the protective malaise of the million spheres. You were open to the power and the glory at a generative time and it shows in your teratoid form."
        },
        {
            "skills": [
                "6 Language - Kurgan",
                "3 Maul fighting",
                "3 Secret Signs - Chaos Patron",
                "1 Spell - Random (Table 5)",
                "1 Second sight"
            ],
            "special": "Name your patron. You may call upon your patron for aid once per day, to do so roll three 6s on 3d6, the GM will interpret his intervention.",
            "name": "15 Chaos Champion",
            "possesions": [
                "Ritual scars",
                "A huge maul",
                "Assortment of ragged armour (Modest armour)",
                "Dream journal, almost full"
            ],
            "description": "You no longer have the spiked brass armour but you still have the ear of your Chaos patron. He's happy for you to experiment with not plunging your sphere into disorder and, ultimately, darkness but the door is always open."
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
            "possesions": [
                "Festooned with keys (counts as modest armour)",
                "A sledgehammer",
                "Lock picking tools"
            ],
            "description": "The key masters wander the universe fathoming the workings of all entry ways they can find. Though they're quite fascinated with simple chests and doors they are most excited by metaphysical and metaphorical barriers. You might find small conclaves of clavigers camped around the feet of demon gates, debating appropriate methods of attack or building obscure machine of entry."
        },
        {
            "skills": [
                "5 Language - Abyssal",
                "3 Spell - Blood Shroud",
                "2 Second Sight",
                "2 Sword fighting",
                "2 Bow fighting",
                "1 Tracking",
                "1 Sneak"
            ],
            "special": "",
            "name": "21 Demon Stalker",
            "possesions": [
                "A silver sword",
                "Sixteen silver arrows and a bow",
                "Pouch of salt",
                "Vial of demon blood"
            ],
            "description": "You stake your reputation on your ability to hunt and kill demonic creatures and those who break bread with them. Goat men in the wilds, or the angel cults of the slums, all needs to be driven back off the edge of the map and into the shores of chaos."
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
                "1 Hammer fighting"
            ],
            "special": "May eat gems and rare metals as a food replacement. You in fact far prefer the taste of rare minerals to mundane food. Dwarves are genderless. You are immune to all compulsions that play on a creature's desire for the opposite sex. This also means you don't have sexual organs. Instead of urinating you excrete through sweating, thus explaining the odour.",
            "name": "22 Dwarf",
            "possesions": [
                "Masons hammer",
                "Roll of artists supplies"
            ],
            "description": "You are a short, hairy, belligerent, alcohol dependent creature. The latter two may be linked, but you'll fight anyone who suggests as much. Since there are no dwarf women (or men, technically) there are no dwarf children or dwarf families, so you can fully commit yourself to the important dwarfy endeavours of creating fine art in unusual places. You intend to find the most unusual places ever seen in all the million spheres."
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
            "special": "May test your luck to get a yes or no answer to a question about mundane matters. The GM should make this test in private, not informing the epopt if they are accurate.",
            "name": "23 Epopt",
            "possesions": [
                "Yellow epopt outfit, padded for protection against unhappy clients (counts as modest armour)",
                "Epopt staff, being a walking staff with",
                "seeing crystal on one end (counts as",
                "staff)",
                "Collapsible tent, big enough for your",
                "stall"
            ],
            "description": "A roaming seer, selling your visions at courts and fetes. You are instantly recognisable by your yellow coif and habit as being open for business. Road weary and world wise, your unpopular visions cause you to constantly move on."
        },
        {
            "skills": [
                "6 Language - Weird Exotic Language",
                "3 in the fighting skill of your weird"
            ],
            "special": "",
            "name": "24 Exotic Warrior",
            "possesions": [
                "A weird and wonderful weapon",
                "Strange clothes",
                "Exciting accent",
                "A tea set OR 3 pocket gods OR Astrological equipment"
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
            "possesions": [
                "Large Astrolabe (as mace)",
                "Abacus",
                "Lots of scrolls and writing equipment"
            ],
            "description": "Mathmologists honour the clean and unambiguous truths of mathematics, and coordinate it with their observation of the multiverse. All things can be measured and predicted with the application of the correct mathmological ratios, their methods applied to penetrate the ethereal surface to glimpse the fundamental numbers below."
        },
        {
            "skills": [
                "4 Strength",
                "2 Fist fighting",
                "2 Run",
                "1 Hook fighting",
                "1 Sneak",
                "1 Awareness"
            ],
            "special": "",
            "name": "26 Fellowship of Porters & Basin Fillers",
            "possesions": [
                "A wooden yoke",
                "Brown over coat and soft doffing cap of the guild",
                "A bale hook. Counts as a knife for damage and gains you a +1 on rolls to lift heavy objects if used to do so",
                "Length of rope"
            ],
            "description": "Porters & Basin Fillers Luggers are a servile group by nature, most often found in the service of others, weighed down by loads that would buckle a donkey. You take pride in that. Maybe so much that the everyday assignments of the guild could not sate your desire to serve, causing you to venture out in search of a real challenge for such a talented varlet."
        },
        {
            "skills": [
                "4 Tunnel fighting",
                "4 Trapping",
                "2 Sneak",
                "2 Awareness",
                "2 Club fighting",
                "2 Tracking",
                "1 Swim"
            ],
            "special": "",
            "name": "31 Gremlin Catcher",
            "possesions": [
                "Small but vicious dog",
                "Flat cap",
                "A club",
                "A sack",
                "D6 empty gremlin jars",
                "A jar with a pissed off gremlin inside"
            ],
            "description": "No matter what country, sphere or abstract dimension you may find yourself in, be sure that gremlins will be there digging their warrens and bothering nice people willing to pay you a shiny penny to bash their little heads in."
        },
        {
            "skills": [
                "1 Poison",
                "1 Sneak",
                "1 Locks",
                "1 Knife fighting",
                "1 Climb",
                "1 Awareness",
                "1 Crossbow fighting",
                "1 Swim",
                "1 Disguise"
            ],
            "special": "",
            "name": "32 Journeyman of the Guild of Sharp Corners",
            "possesions": [
                "Black clothes of the apprentice",
                "Garrotte",
                "Curved sword",
                "3 vials of poison",
                "Crossbow & 6 bolts"
            ],
            "description": "Sharp Corners You are an assassin in training, graduated from fighting dummies or branding practise clients, now you have a license to do it for real. You haven't fully developed the idiosyncratic methods required of a master but you are on the path."
        },
        {
            "skills": [
                "2 Greatsword fighting",
                "2 Pistolet fighting",
                "1 Run",
                "1 Fist Fighting",
                "1 Astrology"
            ],
            "special": "",
            "name": "33 Lansquenet",
            "possesions": [
                "Exquisite pistolet",
                "Bandolier containing 18 plasmic cores",
                "Greatsword",
                "Brightly coloured clothing with lots of tassels and bells (-4 to sneaking). Though frivolous looking it is in fact built with the autarch's divine alchemy and considered modest armour while weighing the same as normal clothing"
            ],
            "description": "You were a mercenary retained in the exclusive service of the phoenix throne, handsomely paid and sent to distant spheres on golden ships to spread the ineffable glory of your paymaster at the tip of your flaming lance."
        },
        {
            "skills": [
                "3 Etiquette",
                "3 Weapon fighting in the weapon of your choice",
                "3 Ride",
                "1 Tracking"
            ],
            "special": "",
            "name": "34 Lonesome King",
            "possesions": [
                "A nice weapon of your choice",
                "A crown",
                "A tired horse"
            ],
            "description": "You were a king. The ruler of all you surveyed, a great conqueror, a law-bringer! But your horse sped off into the pixie forest, or the court magician ensured you disappeared, or you led a sortie into the stars to put your stamp on them as well. Either way you are now a lost and lonely king without a kingdom, no one has heard of you or your people. Most don't believe you and laugh, or worse they do believe you and shrug at the vagaries of fate."
        },
        {
            "skills": [
                "3 Etiquette",
                "1 Strength",
                "1 Tracking",
                "1 Trapping",
                "1 Gastrology"
            ],
            "special": "Immune to mundane ingested poisons. Also can identify any object if eaten, gaining knowledge of its material, its origin (if plausibly familiar), and its magical properties on a successful test of gastrology. Must be thoroughly masticated, not merely swallowed and passed. This does not grant special immunity to any effects it may possess.",
            "name": "35 Miss Kinsey's Diner's Club",
            "possesions": [
                "Sharp metal dentures (damage as sword) OR Forked metal dentures (as knife, but on a critical you may cleanly strip all the flesh from one small appendage) OR Blunt metal dentures (damage as knife but may be used to eat hard objects)",
                "Embroidered napkin"
            ],
            "description": "The Eaters know that there are only two worlds: the without and the within. They intend to insert as much of the prior into the later as they can while experiencing the finest delights available. All culinary experience is open to them, nothing is forbidden at Miss Kinsey's. Try the other, other, other white meat."
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
            "possesions": [
                "Monkey Club",
                "Butcher Knife",
                "d6 small monkeys that do not listen to you but are too scared and hungry to travel far from you",
                "A pocket full of monkey treats"
            ],
            "description": "Life on The Wall is hard. One is never more than a few yards from an endless fall but those precarious villages still need to eat. This is where you come in with your edible monkeys (the distinction is purely for appeal, since all monkeys are of course edible). You used to spend days on end dangling your feet off the edge of the world watching over your chittering livestock while they scampered hither and thither. But there was no future in monkey meat, or future on The Wall. You wanted much more and so stepped off. Or you fell. Either way you and some unlucky monkeys are 10 here now and that's all that matters."
        },
        {
            "skills": [
                "2 Heal",
                "1 Spell - Posthumous vitality",
                "1 Spell - Skeletal Counsel",
                "1 Spell - Torpor",
                "1 Sneak"
            ],
            "special": "",
            "name": "41 Necromancer",
            "possesions": [
                "Dusty robes",
                "The skull of your master OR A zombie servant OR A ghost with whom you have developed a co-dependent relationship with"
            ],
            "description": "The least popular magical practitioners. Shunned by the major centres of learning, they're left to their own devices on the edges of society, passing on knowledge in the time honoured master student dynamic. The loneliness encourages students to make their own friends."
        },
        {
            "skills": [
                "2 Spell - Protection From Rain",
                "2 Callous Strike",
                "2 Spell - Quench",
                "2 Spell - True Seeing",
                "2 Disguise",
                "2 Second Sight",
                "1 Healing",
                "1 Undo",
                "1 Spell - Random (Table 5)"
            ],
            "special": "You are undead so do not need to breathe, circulate blood, and so on. You takes double damage from silver weapons and regain stamina half as effectively from all sources. You must test luck if outside in the rain, made wet, close to open flames, or suffer general grievous wounds. A failure will see your skin ruined. While your skin is damaged you are very obviously a walking corpse. 11",
            "name": "42 Parchment Witch",
            "possesions": [
                "d6 rolls of parchment",
                "Vials of pigments and powders",
                "Collection of brushes",
                "A wicked knife"
            ],
            "description": "Known for your smooth skin, midnight gatherings and being fearful of rain and open flames. The parchment witches are long dead sorcerers who cannot give up the vanity of living and so cover themselves in perfect paper skin. A patiently painted and folded imitation of life to hide ancient bone and gristle."
        },
        {
            "skills": [
                "3 Fist Fighting",
                "3 Awareness",
                "2 Strength",
                "2 Wrestling",
                "2 Axe Fighting"
            ],
            "special": "as Dwarf, but in addition... Other dwarves will completely ignore you as though you were a piece of furniture or somebody's abandoned hat. Very rarely they might openly examine and comment thoughtfully to themselves on your unforgivable flaws, possibly while marking areas for improvement on your body with a grease pen. To non-dwarfy eyes you probably look like any other dwarf. +4 sneak vs dwarves.",
            "name": "43 Poorly Made Dwarf",
            "possesions": [
                "Woodsmans axe",
                "An empty firkin"
            ],
            "description": "Dwarves are known for being the finest artisans of the million spheres. Give a dwarf a rock and he will make gold, give a dwarf a boulder and he will make a dwarf. You were supposed to be the finest expression of dwarfy craftsmanship, a masterpiece, a brand new dwarf like those made by the old masters. But you were imperfect and abandoned."
        },
        {
            "skills": [
                "3 Jousting",
                "2 Sword Fighting",
                "2 Spear fighting",
                "1 Shield fighting",
                "1 Awareness"
            ],
            "special": "",
            "name": "44 Questing Knight",
            "possesions": [
                "Heavy armour",
                "A horse",
                "Lance (as spear)",
                "Sword",
                "Shield",
                "A never ending quest"
            ],
            "description": "You are on a quest for the grail, or the sword, or the throne, or for god, or a lost love, or some other significant object. Your sort are common enough, wandering the worlds acting out your romantic melodrama, accusing good folk of being demons or faeries. Generally considered to be harmless."
        },
        {
            "skills": [
                "2 Spell - Ember",
                "2 Spell - Fire Bolt"
            ],
            "special": "",
            "name": "45 Red Priest",
            "possesions": [
                "Red robes",
                "Traditional faceless metal helmet of your order (modest armour)",
                "Symbolic (but fully sized and fully functional) single headed great axe, to help batter down the door to Sin"
            ],
            "description": "Evangelist of the red redemption, wandering confessor, cauterizer of the wound of sin. Sin being the accumulation and recreational consumption of mass. How can your spirit fly free while shackled and flabby?"
        },
        {
            "skills": [
                "3 Glaive fighting",
                "2 Run",
                "2 Strength",
                "1 Gambling"
            ],
            "special": "",
            "name": "46 Rhino-Man",
            "possesions": [
                "Horn (counts as dagger)",
                "Thick Skin (rhino men always count as being modestly armoured)",
                "Glaive",
                "Knuckle dice",
                "Half full firkin of Rhino-beer (20 rations worth)"
            ],
            "description": "The original Rhino-Men were created by an insane sorcerer several centuries ago, but rebelled and killed him. They are fairly rare creatures, serving as formidable and loyal guards to those who can afford their services."
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
            "possesions": [
                "Incidental sacred jewellery worth 10d6 monies if traded",
                "Peaked hat",
                "Claws (as Swords)",
                "Hooves (as Clubs)",
                "Wings, able to fly as fast as a running man over clear ground"
            ],
            "description": "Body of a bull, head of a man, forelegs of a cat and the wings of a swan, sweetest children of the gods. You, however, were not content to rest on your cloud and instead descended from the heavens (or crawled up from the abyss) and set upon finding your own path among the stars."
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
            "possesions": [
                "A small functional door, worn on your forehead. You channel your magic through it",
                "Flashy robes"
            ],
            "description": "Academy of Doors Troika's very own wizarding academy, pride of the city, experts in pan-dimensional mobility. You were an apprentice of the school and were able to penetrate the (2d6)th door. No master, certainly, but few outside your peers can claim to know more about the vagaries of skyward travel than you."
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
            "possesions": [
                "Pointed wizard hat you received at graduation",
                "Pocket full of wizard biscuits (2d6, each count as a ration)",
                "Wand used to help focus new apprentices, now kept for sentimental reasons"
            ],
            "description": "College of Friends You were trained in the sub-dimensional academy of the Cordial Wizard God. You spent your childhood learning about the fate of pixies, the colour of magic, ritual grammar and endless other theoretical topics. Now you're out in the world, discovering that your education hardly accounted for any of it."
        },
        {
            "skills": [
                "2 in a fighting skill of your choice",
                "2 Wrestling",
                "2 Swim",
                "2 Climb",
                "2 Run",
                "2 Fist Fighting"
            ],
            "special": "",
            "name": "54 The Sublime Society of Beef Steaks",
            "possesions": [
                "A weapon of choice",
                "A small gridiron",
                "2kg of premium meat cuts",
                "Waistcoat",
                "Bottle of strong but fancy wine"
            ],
            "description": "of Beef Steaks Brawlers believe the application of might and a good beef steak is the universal truth. Words do not have power. Words can no more define the universe than they can build a house, lift a cup, or sear a steak. Might can. Really, they have thought a lot about this."
        },
        {
            "skills": [
                "3 Awareness",
                "2 Blacksmithing",
                "1 Sword Fighting",
                "1 Greatsword fighting"
            ],
            "special": "The blessing of Telak awards you armour equal to half (rounded down) the number of swords you carry. So if you were carrying 6 swords your armour would be 3, while if you carried 9 it would be 4. You must be overtly armed at all times or else Telak will take this blessing away until you forge, and donate to the unarmed, a brand new sword.",
            "name": "55 Temple Knight of Telak the Swordbringer",
            "possesions": [
                "The blessing of Telak",
                "6 swords of your choice"
            ],
            "description": "Telak the Swordbringer You were once (and possibly still are) a fanatical monk set to maintain constant martial readiness in preparation for the end times when all doorways crumble inwards. You are never unready and always have spares."
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
            "special": "May test their luck to just so happen to have exactly the (common) mystical nicknack the situation requires",
            "name": "56 Thaumaturge",
            "possesions": [
                "Thamaturgical fez",
                "Staff, bedecked with charms and bells. May reroll one die on the Oops! Table if using this staff, however may never sneak up on anyone because of the ringing and clattering it makes",
                "Curled Shoes",
                "Voluminous robes"
            ],
            "description": "Wandering miracle workers, the depths of whose clothes are filled with pouches of unguents, holy icons and herbs. No matter the metaphysical need, they are always prepared."
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
            "special": "You don't recover Stamina by resting in the usual manner, instead you have to spend an evening with a hot iron melting your skin back together like putty. For each hour of rest with access to the right tools you regain 3 Stamina. May recharge plasmic machines by hooking your fluids to them and spending Stamina. 1 Stamina and 6 minutes per charge. You always count as being lightly armoured.",
            "name": "61 Thinking Engine",
            "possesions": [
                "Soldering iron",
                "Detachable autonomous hands OR Centaur body (+4 Run) OR Inbuilt particle detector (+4 Second Sight) OR One random spell at rank 3",
                "15"
            ],
            "description": "Your eyes are dull ruby spheres, your skin is hard and smooth like ivory but brown and whorled like wood. You are clearly damaged, you have no memory of your creation or purpose, and some days your white internal juices ooze thickly from cracks in your skin."
        },
        {
            "skills": [
                "3 Sword Fighting",
                "1 Awareness",
                "1 Climb",
                "1 Bow Fighting",
                "1 Run",
                "1 Swim"
            ],
            "special": "",
            "name": "62 Vengeful Child",
            "possesions": [
                "A too-big sword, +1 to Sword Fighting and Damage Rolls while using it. Only you may benefit from this bonus, it's not magic just sentimental",
                "An old hunting bow & 12 arrows"
            ],
            "description": "Your village was burnt down by ruffians, or your mother was beheaded by snake cultists, or your father was hung by corrupt officials. Either way, you took up the sword and entered the world with a chip on one shoulder and an oversized sword on the other."
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
            "special": "You may test your Luck to recall facts that you might reasonably be expected to have encountered relating to the natural sciences and humanities. 16",
            "name": "63 Venturesome Academic",
            "possesions": [
                "Reading glasses in a sturdy case (you cannot read without them)",
                "Small sword",
                "Bundle of candles & matches",
                "Writing materials",
                "Journal"
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
            "possesions": [
                "Large sack",
                "Witch-hair rope",
                "Crossbow & 12 bolts",
                "Sword",
                "d6 pocket gods",
                "Ruby Lorgnette"
            ],
            "description": "Some people say man is the most dangerous prey. They're wrong. Can men turn into flocks of seagulls when cornered in an alley? Can men ignite the air and freeze your blood? No, they can't. Wizards are the most dangerous prey."
        },
        {
            "skills": [
                "4 weapon fighting skill of choice",
                "2 Etiquette",
                "1 Healing"
            ],
            "special": "",
            "name": "65 Yongardy Lawyer",
            "possesions": [
                "Rapier and puffy shirt OR Sjambok (counts as club) and lots of scars OR Two handed sword and heavy armour OR Hammer and huge shield",
                "Manual on Yondardy Law",
                "Barrister's Wig"
            ],
            "description": "Down in Yongardy they do things differently. They respect the law. Every day there is a queue outside the courts to get a seat to see the latest up and coming barrister defend his case with three feet of steel. The people follow the careers of their favourite solicitors, watch all their cases, collect their portraits and sneak into the court after hours to dab the patches of blood on white handkerchiefs. In Yongardy they love the law."
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
            "special": "You are immune to all mind altering effects. You are able to speak but usually choose not to. When making advancement checks in skills related to abstract thought, such as spells or astrology, you must roll twice and succeed on both or else fail.",
            "name": "66 Zoanthrop",
            "possesions": [
                "Wooden club and no starting possessions, throw off the shackles of civilisation. You are probably nude."
            ],
            "description": "At some point in your past you decided you didn't need it any more. You found a zoanthropologist and paid him well to remove your troublesome forebrain and so elevate you to the pure and unburdened beast you are today."
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
