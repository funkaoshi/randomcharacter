import random

from fifth.languages import LANGUAGES
from fifth.processor import CharacterProcessor


class AbstractBackground(object):

    def name(self):
        return self.NAME if hasattr(self, 'NAME') else self.__class__.__name__

    def personality_trait(self):
        return random.choice(self.PERSONALITY_TRAIT)

    def ideal(self):
        return random.choice(self.IDEAL)

    def flaw(self):
        return random.choice(self.FLAW)

    def bond(self):
        return random.choice(self.BOND)

    def specialty(self):
        return random.choice(self.SPECIALTY) if hasattr(self, 'SPECIALTY') else ""

    def defining_event(self):
        return random.choice(self.DEFINING_EVENT) if hasattr(self, 'DEFINING_EVENT') else ""

    def proficiencies(self):
        return self.PROFICIENCIES

    def languages(self):
        return []

    def equipment(self):
        return self.EQUIPMENT


class Acolyte(AbstractBackground):
    PERSONALITY_TRAIT = [
        "I idolize a particular hero of my faith, and constantly refer to that person's deeds and example.",
        "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace.",
        "I see omens in every event and action. The gods try to speak to us, we just need to listen",
        "Nothing can shake my optimistic attitude.",
        "I quote sacred texts and proverbs in almost every situation.",
        "I misquote sacred texts and proverbs in almost every situation."
        "I am tolerant of other faiths and respect the worship of other gods.",
        "I am intolerant of other faiths and condemn the worship of other gods.",
        "I've spent so long in the temple that I have little practical experience dealing with people in the outside world.",
        "I've enjoyed fine food, drink, and high society among my temple's elite. Rough living grates on me."
    ]

    IDEAL = [
        "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld.",
        "Charity. I always try to help those in need, no matter what the personal cost.",
        "Power. I hope to one day rise to the top of my faith's religious hierarchy.",
        "Aspiration. I seek to prove myself worthy of my god's favour by matching my actions against his or her teachings.",
        "Change. We must help bring about the changes the gods are constantly working in the world.",
        "Faith. I trust that my deity will guide my actions. I have faith that if I work hard, things will go well.",
    ]

    BOND = [
        "I would die to recover an ancient relic of my faith that was lost long ago.",
        "I will someday get revenge on the corrupt temple hierarchy who branded me a heretic.",
        "I owe my life to the priest who took me in when my parents died.",
        "Everything I do is for the common people.",
        "I will do anything to protect the temple where I served.",
        "I seek to preserve a sacred text that my enemies consider heretical and seek to destroy.",
    ]

    FLAW = [
        "I judge others harshly, and myself even more severely.",
        "I put too much trust in those who wield power within my temple's hierarchy.",
        "My piety sometimes leads me to blindly trust those that profess faith in my god.",
        "I am suspicious of strangers and expect the worst of them.",
        "Once I pick a goal, I become obsessed with it to the detriment of everything else in my life.",
        "I am inflexible in my thinking.",
    ]

    PROFICIENCIES = ['Insight', 'Religion']

    def languages(self):
        return random.sample(LANGUAGES, 2)

    def equipment(self):
        return [
            'Holy symbol',
            random.choice(['Prayer book', 'Prayer wheel']),
            '5 sticks of incense',
            'Set of common clothes',
            '15gp'
        ]


class Criminal(AbstractBackground):

    SPECIALTY = [
        "Blackmailer",
        "Burglar",
        "Enforcer",
        "Fence",
        "Highway robber",
        "Hired killer",
        "Pickpocket",
        "Smuggler"
    ]

    PERSONALITY_TRAIT = [
        "I always have a plan for what to do when things go wrong.",
        "I am always calm, no matter what the situation. I never raise my voice or let my emotions control me.",
        "The first thing I do in a new place is note the locations of everything valuable&mdash;or where such things could be hidden.",
        "I would rather make a new friend than a new enemy.",
        "I am incredibly slow to trust. Those who seem the fairest often have the most to hide.",
        "I don't pay attention to the risks in a situation. Never tell me the odds.",
        "The best way to get me to do something is to tell me I can't do it.",
        "I blow up at the slightest insult."
    ]

    IDEAL = [
        "Honor. I don't steal from others in the trade.",
        "Freedom. Chains are meant to be broken, as are those who would forge them.",
        "Charity. I steal from the wealthy so that I can help people in need.",
        "Greed. I will do whatever it takes to become wealthy.",
        "People. I'm loyal to my friends, not to any ideals, and everyone else can take a trip down the Styx for all I care.",
        "Redemption. There's a spark of good in everyone."
    ]

    BOND = [
        "I'm trying to pay off an old debt I owe to a generous benefactor.",
        "My ill-gotten gains go to support my family.",
        "Something important was taken from me, and I aim to steal it back.",
        "I will become the greatest thief that ever lived.",
        "I'm guilty of a terrible crime. I hope I can redeem myself for it.",
        "Someone I loved died because of I mistake I made. That will never happen again."
    ]

    FLAW = [
        "When I see something valuable, I can't think about anything but how to steal it.",
        "When faced with a choice between money and my friends, I usually choose the money.",
        "If there's a plan, I'll forget it. If I don't forget it, I'll ignore it.",
        "I have a 'tell' that reveals when I'm lying.",
        "I turn tail and run when things look bad.",
        "An innocent person is in prison for a crime that I committed. I'm okay with that."
    ]

    PROFICIENCIES = ['Deception', 'Stealth']

    EQUIPMENT = ['crowbar' 'dark clothes with hood', '15gp']


class FolkHero(AbstractBackground):

    NAME = "Folk Hero"

    DEFINING_EVENT = [
        "I stood up to a tyrant's agents.",
        "I saved people during a natural disaster.",
        "I stood alone against a terrible monster.",
        "I stole from a corrupt merchant to help the poor.",
        "I led a militia to fight off an invading army.",
        "I broke into a tyrant's castle and stole weapons to arm the people.",
        "I trained the peasantry to use farm implements as weapons against a tyrant's soldiers.",
        "A lord rescinded an unpopular decree after I led a symbolic act of protest against it.",
        "A celestial, fey, or similar creature gave me a blessing or revealed my secret origin.",
        "Recruited into a lord's army, I rose to leadership and was commended for my heroism."
    ]

    PERSONALITY_TRAIT = [
        "I judge people by their actions, not their words.",
        "If someone is in trouble, I'm always ready to lend help.",
        "When I set my mind to something, I follow through no matter what gets in my way.",
        "I have a strong sense of fair play and always try to find the most equitable solution to arguments.",
        "I'm confident in my own abilities and do what I can to instill confidence in others.",
        "Thinking is for other people. I prefer action.",
        "I misuse long words in an attempt to sound smarter.",
        "I get bored easily. When am I going to get on with my destiny?"
    ]

    IDEAL = [
        "Respect. People deserve to be treated with dignity and respect.",
        "Fairness. No one should get preferential treatment before the law, and no one is above the law.",
        "Freedom. Tyrants must not be allowed to oppress the people.",
        "Might. If I become strong, I can take what I want&mdash;what I deserve.",
        "Sincerity. There's no good in pretending to be something I'm not.",
        "Destiny. Nothing and no one can steer me away from my higher calling."
    ]

    BOND = [
        "I have a family, but I have no idea where they are. One day, I hope to see them again.",
        "I worked the land, I love the land, and I will protect the land.",
        "A proud noble once gave me a horrible beating, and I will take my revenge on any bully I encounter.",
        "My tools are symbols of my past life, and I carry them so that I will never forget my roots.",
        "I protect those who cannot protect themselves.",
        "I wish my childhood sweetheart had come with me to pursue my destiny."
    ]

    FLAW = [
        "The tyrant who rules my land will stop at nothing to see me killed.",
        "I'm convinced of the significance of my destiny, and blind to my shortcomings and the risk of failure.",
        "The people who knew me when I was young know my shameful secret, so I can never go home again.",
        "I have a weakness for the vices of the city, especially hard drink.",
        "Secretly, I believe that things would be better if I were a tyrant lording over the land.",
        "I have trouble trusting in my allies."
    ]

    PROFICIENCIES = ["Animal Handling", "Survival"]

    EQUIPMENT = ["shovel", "iron pot", "common clothes", "10gp"]


class Sage(AbstractBackground):
    SPECIALTY = [
        "Alchemist",
        "Astronomer",
        "Discredited academic",
        "Librarian",
        "Professor",
        "Researcher",
        "Wizard's apprentice",
        "Scribe"
    ]

    PERSONALITY_TRAIT = [
        "I use polysyllabic words that convey the impression of great erudition.",
        "I've read every book in the world's greatest libraries&mdash; or I like to boast that I have.",
        "I'm used to helping out those who aren't as smart as I am, and I patiently explain anything and everything to others.",
        "There's nothing I like more than a good mystery. ",
        "I'm willing to listen to every side of an argument before I make my own judgment.",
        "I . . . speak . . . slowly . . . when talking . . . to idiots, . . . which . . . almost . . . everyone . . . is . . . compared . . . to me.",
        "I am horribly, horribly awkward in social situations.",
        "I'm convinced that people are always trying to steal my secrets."
    ]

    IDEAL = [
        "Knowledge. The path to power and self-improvement is through knowledge.",
        "Beauty. What is beautiful points us beyond itself toward what is true.",
        "Logic. Emotions must not cloud our logical thinking.",
        "No Limits. Nothing should fetter the infinite possibility inherent in all existence.",
        "Power. Knowledge is the path to power and domination.",
        "Self-Improvement. The goal of a life of study is the betterment of oneself."
    ]

    BOND = [
        "It is my duty to protect my students.",
        "I have an ancient text that holds terrible secrets that must not fall into the wrong hands.",
        "I work to preserve a library, university, scriptorium, or monastery.",
        "My life's work is a series of tomes related to a specific field of lore.",
        "I've been searching my whole life for the answer to a certain question.",
        "I sold my soul for knowledge. I hope to do great deeds and win it back."
    ]

    FLAW = [
        "I am easily distracted by the promise of information.",
        "Most people scream and run when they see a demon. I stop and take notes on its anatomy.",
        "Unlocking an ancient mystery is worth the price of a civilization.",
        "I overlook obvious solutions in favor of complicated ones.",
        "I speak without really thinking through my words, invariably insulting others.",
        "I can't keep a secret to save my life, or anyone else's."
    ]

    PROFICIENCIES = ['Arcana', 'History']

    EQUIPMENT = [
        "bottle of black ink",
        "quill",
        "small knife",
        "a set of common clothes",
        "letter from dead colleague posing a question you have not been able to answer"
    ]

    def languages(self):
        return random.sample(LANGUAGES, 2)

class Soldier(AbstractBackground):

    SPECIALTY = [
        "Officer",
        "Scout",
        "Infantry",
        "Cavalry",
        "Healer",
        "Quartermaster",
        "Standard bearer"
    ]

    PERSONALITY_TRAIT = [
        "I'm always polite and respectful.",
        "I'm haunted by memories of war. I can't get the images of violence out of my mind.",
        "I've lost too many friends, and I'm slow to make new ones.",
        "I'm full of inspiring and cautionary tales from my military experience relevant to almost every combat situation.",
        "I can stare down a hell hound without flinching.",
        "I enjoy being strong and like breaking things.",
        "I have a crude sense of humour.",
        "I face problems head-on. A simple, direct solution is the best path to success."
    ]

    IDEAL = [
        "Greater Good. Our lot is to lay down our lives in defence of others.",
        "Responsibility. I do what I must and obey just authority.",
        "Independence. When people follow orders blindly, they embrace a kind of tyranny.",
        "Might. In life as in war, the stronger force wins.",
        "Live and Let Live. IDEALs aren't worth killing over or going to war for.",
        "Nation. My city, nation, or people are all that matter."
    ]

    BOND = [
        "I would still lay down my life for the people I served with.",
        "Someone saved my life on the battlefield. To this day, I will never leave a friend behind.",
        "My honour is my life.",
        "I'll never forget the crushing defeat my company suffered or the enemies who dealt it.",
        "Those who fight beside me are those worth dying for.",
        "I fight for those who cannot fight for themselves."
    ]

    FLAW = [
        "The monstrous enemy we faced in battle still leaves me quivering with fear.",
        "I have little respect for anyone who is not a proven warrior.",
        "I made a terrible mistake in battle that cost many lives&mdash;and I would do anything to keep that mistake secret.",
        "My hatred of my enemies is blind and unreasoning.",
        "I obey the law, even if the law causes misery.",
        "I'd rather eat my armour than admit when I'm wrong."
    ]

    PROFICIENCIES = ['Athletics', 'Intimidation']

    def equipment(self):
        return [
            "insignia of rank",
            "%s from fallen enemy" % random.choice(['dagger', 'broken blade', 'banner']),
            random.choice(["set of bone dice", "deck of cards"]),
            "common clothes",
            "10gp"
        ]


class Background(CharacterProcessor):
    def process(self):
        # , Soldier
        Background = random.choice([Acolyte, Criminal, FolkHero, Sage])
        bg = Background()
        self.character.background = bg.specialty() or bg.name()
        self.character.defining_event = bg.defining_event()
        self.character.personality_trait = bg.personality_trait()
        self.character.ideal = bg.ideal()
        self.character.bond = bg.bond()
        self.character.flaw = bg.flaw()
        self.character.proficiencies.union(bg.proficiencies())
        self.character.equipment.extend(bg.equipment())
        self.character.languages.union(bg.languages())


