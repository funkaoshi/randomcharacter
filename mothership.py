import itertools
import random

import mixins
import dice

class ForgottenAndroid():
    def __init__(self):
        self.combat = f"30 {random.choice(['Scavenged Tools', 'Weapon', 'Scrap'])} 3d10 DMG"
        self.instinct = 25
        self.hits = 2
        self.hp = 10
        self.manufacturing_defect = random.choice(self.MANUFACTURING_DEFECT)
        self.adaption = random.choice(self.ADAPTATION)
        self.what_are_they_doing = random.choice(self.WHAT_ARE_THEY_DOING)
        self.wants_to_talk_about = random.choice(self.WANTS_TO_TALK_ABOUT)

    MANUFACTURING_DEFECT = [
       'Pseudoflesh rotted off completely. A walking metal skeleton.',
       'Missing random limb(s).',
       'Missing from the waist down.',
       'Face absent entirely.',
       'Balloon thin, massively swollen head from internal chemical reactions',
       'Face melted into a grotesque lump. Acid burns all over their pseudoflesh.',
       '“Bot Rot." Highly infectious fungal condition that grows bizarrely on delicate circuity.',
       'Two androids fused together side-by-side or back-to-back.',
       'Speech Synthesis center missing. Communicates by parroting, creatively chopping and changing.'
       'Limbs fused together and nearly useless. Crawls in the fetal position.',
    ]

    ADAPTATION = [
        'Claw-like fingers/toes, climbs on walls and ceiling. Forearms sharpened into scythe blades (2d10 DMG).',
        'Jury-rigged laser cutter replacing limb (1⁄2 DMG and android is stunned for 2 turns after firing).',
        'Enters “rest-mode” and appears dead. Often lies amongst “dead” android heaps.',
        'Wears a cloak of overpowered strobing lamps.',
        'Carries a tranq-gun fitted with data-syringes. Android targets make Sanity Save [+] or the virus crashes their consciousness, leaving them inert for 1 hour.'
        'Carries jugs of acidic, industrial run-off sludge (3d10 DMG, Armor Save or armor destroyed).',
        'Wearing a vaccsuit. Pretending to be a lost human, refusing to take off suit, insisting it has “a disease.”',
        'Constructed a hunting animal from jury-rigged swarm of limbs. C:50 (no DMG, grapples) I:20 H:2(10)',
        '2d10 passive android companions. Can broadcast a signal to send them into a killing frenzy. PC androids gain 2d10 stress OR give in to the signal for 3 rounds.',
        'Lives entirely within the vents and crawlspaces, never venturing into the corridors.',
    ]

    WHAT_ARE_THEY_DOING = [
        'Hiding and observing from a distance.',
        'Arguing amongst themselves. Loudly.',
        'Cheerfully playing a game of Hide & Seek.',
        'Harvesting parts from a broken android.',
        'Repairing a broken android with their own parts. This incapacitates or kills the donor.',
        'Stuck in a broken loop, trying to do the job of a CLOUDBANK employee.',
        'Connected to 1d10 androids via cable. Silently forming a Beowulf Cluster.',
        'Fleeing from a nearby Troubleshooter (pg. 14) killteam. 1d5 rooms away.',
        'Experimenting with a random Artifact (pg. 62) they just found.',
    ]

    WANTS_TO_TALK_ABOUT = [
        'Nothing. Runs away if approached.',
        'Getting out of here.',
        'The Minotaur (pg. 29). Is it true it can save humanity?',
        'Mundane details of CLOUDBANK production.',
        'One of them believes it is human despite physical evidence to the contrary. Begs to come with you.',
        'Normal human chit-chat. Follows like a lost puppy and asks child-like questions like "Why is the sky blue?"',
        'Terrified of Monarch (pg. 8). Afraid of being sent to the [35D] REJECT BIN. Willing to help.',
        'Mundane details of CLOUDBANK production. Their memories are all out of date and they don\'t realize the factory has closed down.'
        'What the world outside THE DEEP is like. Could they make it there? Would people treat them poorly?',
        'Their present condition is the result of torture by another (Diver? Android?). They hold you responsible.',
    ]
