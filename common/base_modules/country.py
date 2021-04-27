
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
            dist.district_updater.update(dist)
        self.country_updater.update(self)
        self.election_count += 1

    def get_district_representation(self): #For each voter in a district, add the squared distance to the closest representative
        dist_list = []
        for district in self.districts:
            total_error = 0
            for voter in district.voters:
                total_distance = 0 #total distance to candidates
                for rep in district.representatives:
                    distance = voter.views.distance(rep.views_current)
                    total_distance += distance
                total_error += (total_distance / len(district.representatives)) ** 2 #avg distance to candidates
            dist_list.append(total_error)
        return dist_list
        