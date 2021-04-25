
class PartySystem:

    def __init__(self, other_data={}):
        self.other_data = other_data

    def get_party(self, vector):
        raise NotImplementedError

    def generate_vector(self):
        raise NotImplementedError