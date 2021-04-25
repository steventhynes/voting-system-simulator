
class Voter:

    def __init__(self, views, candidate_retreiver, vote_power=1, other_data={}):
        self.views = views
        self.candidate_retreiver = candidate_retreiver
        self.vote_power = vote_power
        self.other_data = other_data