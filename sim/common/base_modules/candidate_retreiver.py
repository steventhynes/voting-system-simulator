
class CandidateRetriever:

    def __init__(self, other_data={}):
        self.other_data = other_data

    def get_candidates(self, voter, district):
        raise NotImplementedError