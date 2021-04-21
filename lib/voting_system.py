
class VotingSystem:

    def __init__(self, other_data={}):
        self.other_data = other_data

    def district_election(self, district):
        raise NotImplementedError

    def country_election(self, country):
        raise NotImplementedError