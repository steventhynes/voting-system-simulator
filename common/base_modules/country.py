
class Country:

    def __init__(self, country_populator, country_updater, voting_system, party_system=None, other_data={}):
        self.country_populator = country_populator
        self.country_updater = country_updater
        self.voting_system = voting_system
        self.party_system = party_system
        self.other_data = other_data

        self.districts = []
        self.legislature = []

        self.election_count = 0

        self.country_populator.populate(self)

    def run_election(self):
        self.voting_system.election(self)
        for dist in self.districts:
            dist.district_updater.update()
        self.country_updater.update()
        self.election_count += 1
        
        