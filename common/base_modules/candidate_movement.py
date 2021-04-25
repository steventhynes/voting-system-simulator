
class CandidateMovement:

    def __init__(self, other_data={}):
        self.other_data = other_data

    def move(self, candidate, district):
        raise NotImplementedError