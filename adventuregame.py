import random
from dice import d, xdy

class Character(object):
        
    def __init__(self):
        attributes = [6, 8, 10, 12]
        random.shuffle(attributes)
        self.str = attributes[0]
        self.sta = attributes[1]
        self.agi = attributes[2]
        self.int = attributes[3]
        self.calling = random.choice([DEFENDER, LEADER, SKIRMISHER])
        self.hp = self.str + self.sta
        if self.calling == DEFENDER:
            self.hp = self.hp + xdy(4,6) + 24
        elif self.calling in [LEADER, SKIRMISHER]:
            self.hp = self.hp + xdy(2,6) + 16
        self.vitality = random.choice([1, 2, 2, 3, 3, 4])
        self.theme = random.choice(THEME)
        self.subtheme = random.choice(self.theme['subtheme'])
        self.theme = self.theme['name']
        self.fighting_style = random.choice(FIGHTING_STYLE)
        self.background = random.choice(BACKGROUND)

DEFENDER, LEADER, SKIRMISHER = 'Defender', 'Leader', 'Skirmisher'

THEME = [
    {'name': 'Arcane', 'subtheme': ['Ofuda', 'Force', 'Summoning']},
    {'name': 'Divine', 'subtheme': ['Holy', 'Unholy', 'Water', 'Wind']},
    {'name': 'Elemental', 'subtheme': ['Earth', 'Fire', 'Water', 'Wind']},
    {'name': 'Physical', 'subtheme': ['Balanced', 'Brutal', 'Precise']},
    {'name': 'Primal', 'subtheme': ['Plant', 'Poison', 'Shifter']}
]

FIGHTING_STYLE = [
    'Dual Weapons (Melee)',
    'Dual Weapons (Ranged)',
    'Implements (Melee)',
    'Implements (Ranged)',
    'One Handed Weapons (Melee)',
    'One Handed Weapons (Ranged)',
    'One Handed Weapons w/Shield (Melee)',
    'One Handed Weapons w/Shield (Ranged)',
    'Two Handed Weapon (Melee)',
    'Two Handed Weapons (Ranged)',
    'Unarmed (Melee)',
]

BACKGROUND = [
    "<strong>Amnesiac</strong> &mdash; You've lost - or had stolen - your memory. How you lost it is a mystery to you. Your past is a blank slate. Chance or perhaps fate has drawn you into adventure and given you a clue to your past.",
    "<strong>Apprentice</strong> &mdash; You were once a pupil, an apprentice, studying under the tutelage of a well learned master. Was it a mundane art like scrivening or were you learning to be an apothecary? Could it have been a darker or more mystical art like sorcery or witchcraft? Is your former master still alive? If they, are they still an ally or did you betray them? If they're dead or missing... what happened?",
    "<strong>Brigand</strong> &mdash; For years, you've endured as a brigand, a bandit... stealing from others along empty stretches of roads or narrow trails used by smugglers. After provoking an overwhelming response from the locals, you've decided to take up a more 'ethical' profession of treasure hunting instead.",
    "<strong>Burglar</strong> &mdash; You thrived by breaking into the homes of those wealthier than you, taking their gold and silver, and fencing it down at the docks. However, you stole the wrong thing from the wrong person and now you're on the run. Or did you get caught by the guard and now need a quick score to pay off your fine?",
    "<strong>Compelled</strong> &mdash; An unknown force draws you towards the life of an adventurer. A calling to seek out others and venture into the unknown. Is it just voices in your head or something more sinister that has found its way into your mind? Or is it the curse of a dying witch?",
    "<strong>Con Artist</strong> &mdash; You're a fast talker and an even faster runner... which has served you well. Once again, you've taken too much from too many or even just a little from the wrong person and you've been forced to skip town, yet again. Perhaps you've grown tired of living off the gullibity of others or perhaps you're sure the dark places of the world hold more opportunities for you.",
    "<strong>Conscript</strong> &mdash; You were once drafted to fight as a conscript in a war not of your choosing. When you returned home, nothing was as you recalled... or perhaps you originally hailed from another land but were left behind when your troop was disbanded.",
    "<strong>Deposed Tyrant</strong> &mdash; You had great power in your grasp and lost hold of it in a terrible battle. Perhaps the people you ruled with an iron fist overthrew you or another person/creature of great power took it from you, but now... you're left with nothing but a common sword and piecemeal armor.",
    "<strong>Destitute</strong> &mdash; For whatever reason, you are broke. Perhaps your business failed or you had a sure bet backfire on you, but now... you've taken up adventuring under a false name in an effort to escape from those you owe money too.",
    "<strong>Diabolist</strong> &mdash; You released or were blamed for bring a demon into the Mortal Realms from the fiery Hells of Oblivion. Did you do this on purpose or by accident; did you do it at all and are just blamned for it? If you participated in the ritual... did you think you could control the demon?",
    "<strong>Digger</strong> &mdash; As a child, you were fascinated with diggung up buried treasure in the old stony hills behind your farmstead or perhaps you grew up with a parent who traveled the world as an archaeologist. Your past has instilled an obsession to unearth ancient treasures and has sabotaged your attempts to learn a local profession.",
    "<strong>Ex-cultist</strong> &mdash; As part of a strange sect, you became distrusted because of your associations with the cult. The cult however, has no place for you either. What was the cult like; does it still exist? If so, how do they feel about ex-cult members?",
    "<strong>Exhumer</strong> &mdash; By accident or by purpose, you've released something powerful from its prison. Was it a sealed crypt or an ancient tomb? A magical artifact you broke or triggered? Was it truly accidental or did greed drive your motives?",
    "<strong>Farmer</strong> &mdash; Your crops have turned to dust, your fields have gone fallow. You once tilled this land, but now, due to otherworldly corruption, vile sorcery, or perhaps something as mundane as a drought... you have been left homeless and your family has perished.",
    "<strong>Fearless</strong> &mdash; Whether for excitement or the adrenaline rush of near death, adventuring is an excuse for you push yourself to your limits and experience the thrill of living life to its fullest. The treasures you find are merely and engine to fund your endeavors.",
    "<strong>Follower</strong> &mdash; You're either a follower or friend of one of the other adventurers or you've just stumbled into things and decided to follow what the others were doing. Whether out of boredom or motivated by greed or curiosity, you continue to fall into adventure3.",
    "<strong>Gambler</strong> &mdash; Playing the odds has always been an addiction for you, even when its sent you to rock bottom. This is one of those times. You've lost everything and perhaps you still owe someone powerful, a rather large debt. Or perhaps you were accused of cheating and they're after you to exact revenge and reclaim your ill gotten winnings... even if y ou didn't cheat. Or did you?",
    "<strong>Healer</strong> &mdash; Using simple bandages, herbs, and known remedies, you once treated the sick, the infirm, and the wounded. However, you lost someone and you were blamed. Was it incompetence or intent? Who were you not able to save? Did you work for a lord or landed noble? Or were you just a village healer?",
    "<strong>Hunter</strong> &mdash; On the edge of civilization, you've survived for many years by catching wild game, hunting or trapping in the deep woods, and selling meat and furs to traders in small border towns. For whatever reason, you've been forced to move on. What drove you out of your hunting grounds?",
    "<strong>Instigator</strong> &mdash; Something in your house or town, maybe even kingdom bothered and upset you. So you tried to change that aspect, but failed and were exiled as a threat to friends and family or society. What did you fight against? Inequality, excessive taxes, or some other injustice?",
    "<strong>Mercenary</strong> &mdash; You fought in skirmishes, raided border towns, and perhaps even an all out war for gold. After some time, you tired of the life or were driven out of your mercenary outfit. How do your past employers feel about your services rendered? What does your former mercenary outfit think about you?",
    "<strong>Murderer</strong> &mdash; Hate, passion, anger, or perhaps even in a case of mistaken identity, you've been charged with murder and have run from the law.",
    "<strong>Oathbreaker</strong> &mdash; You were once part of an order or guild and broke a serious custom or rule. You're no longer welcome in what was once your home and representatives of the organization hinder your goals when your paths cross.",
    "<strong>Orphaned</strong> &mdash; For some time now, you've survived on wits alone. Your ambition is boundless and having come across rumors of treasures from the past, you've decided it's time to pull yourself out of the streets by getting those treasures for yourself.",
    "<strong>Outlaw</strong> &mdash; Was it a case of mistaken identity or did you truly commit the crime you have been accused of and then fled before authorities could bring you to justice? Regardless, you have fled civilized lands and seek treasure and wealth to bribe your way out of the offense or",
    "<strong>Protector</strong> &mdash; You were once an honor guard for a notable lord, a wizards guardian, or was it something else? You were there warden, their guardian, their protector... but they are no more. Was it your fault? Or was it unavoidable? How did you survive?",
    "<strong>Slave</strong> &mdash; Born into slavery or kidnapped at a young age, you eventually escaped or were freed. How were you freed? Are you hunted by your past masters?",
    "<strong>Smuggler</strong> &mdash; You're skilled at transporting disreputable goods across borders and keeping them out of the prying eyes of those that would confiscate such banned goods. Your previours routes are no longer open or profitable... or perhaps you lost or kept something that someone powerful wants back and now you're on the run from them. If so, what is it and why did you keep it or how did you lose it?",
    "<strong>Soldier</strong> &mdash; Unlike the mercenary, you were a soldier for a king, a duke, or other powerful noble. You served for some time, but your unit is now disbanded. Did it fall in battle or relieved of duty in peacetime to pursue other interests? Were you a good soldier or did you just serve your time and get out? Why aren't you a soldier anymore?",
    "<strong>Survivor</strong> &mdash; You're the last of your kind, kin, townsfolk, or perhaps the last member of a secret order. The only one to avoid death, disaster, or disease. What caused this calamity and how did you escape it?",
    "<strong>Visitor</strong> &mdash; You're not from around here. Perhaps it's from another land across the sea or even another time. Were you locked in stasis and only recently awoke? Or were your forced or stumble through a one-way portal? No matter the reason, you're stuck here now and have decided to make the best of it you can... though you stick out worse than a sore thumb.",
]