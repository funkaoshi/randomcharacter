class CharacterProcessor(object):
    def __init__(self, character):
        self.character = character

    def process(self):
        """
        This method operates on the character, transforming it in someway.
        """
        raise NotImplementedError

