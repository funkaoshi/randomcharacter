import collections
import json

with open("troika_backgrounds.txt") as f:
    backgrounds_txt = collections.deque(f.readlines())


def nextline():
    return backgrounds_txt and backgrounds_txt.popleft().strip()


backgrounds = []
while backgrounds_txt:
    name = nextline()
    description = nextline()

    assert(nextline() == "")
    assert(nextline() == "Possessions")

    possessions = []
    while True:
        possession = nextline()
        if not possession:
            break
        possessions.append(possession)

    assert(nextline() == "Skills")

    skills = []
    while True:
        skill = nextline()
        if not skill:
            break
        skills.append(skill)

    specials = []
    if backgrounds_txt and backgrounds_txt[0].strip() == "Special":
        backgrounds_txt.popleft()
        while True:
            special = backgrounds_txt and nextline()
            if not special:
                break
            specials.append(special)

    backgrounds.append({
        "name": name,
        "description": description,
        "possessions": possessions,
        "skills": skills,
        "special": " ".join(specials)
    })

print((json.dumps(backgrounds, indent=4)))

