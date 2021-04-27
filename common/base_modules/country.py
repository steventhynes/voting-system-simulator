
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
        
    #For each voter in a district, add the average approval (1 or 0) 
    def get_district_representation(self):
        dist_list = []
        for district in self.districts:
            avg_rep_score = 0 #average for the district over the voters
            for voter in district.voters:
                rep_score = 0 #average for the voter over the representatives
                preferred_candidates = [x[0] for x in voter.candidate_retreiver.get_candidates(voter, district)]
                for rep in district.representatives:
                    if rep in preferred_candidates:
                        rep_score += 1 / len(district.representatives)
                avg_rep_score += rep_score / len(district.voters)
            dist_list.append(avg_rep_score)
        return dist_list #returns a list of the district scores