
class VotingSystem:

    def __init__(self, other_data={}):
        self.other_data = other_data

    def election(self, country):
        raise NotImplementedError