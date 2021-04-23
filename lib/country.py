
class Country:

    def __init__(self, nation_populator, nation_updater, voting_system, party_system=None, other_data={}):
        self.nation_populator = nation_populator
        self.nation_updater = nation_updater
        self.voting_system = voting_system
        self.party_system = party_system
        self.other_data = other_data

        self.districts = []
        self.legislature = []

        self.election_count = 0

        self.nation_populator.populate(self)
        for dist in self.districts:
            dist.district_populator.populate()

    def run_election(self):
        for dist in self.districts:
            self.voting_system.district_election(dist)
        self.voting_system.country_election(self)
        
        