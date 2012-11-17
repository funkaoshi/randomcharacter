import collections
import sys

import character

iterations = int(sys.argv[1])

for msg, gen in [('With Thieves', character.Character),
        ('Without Thieves', character.LBBCharacter)]:
    dist = collections.Counter(gen(testing=True).character_class['name']
                               for _ in range(iterations))
    print msg
    for c, count in dist.most_common():
        print c, count * 100 / iterations
    print '-'


