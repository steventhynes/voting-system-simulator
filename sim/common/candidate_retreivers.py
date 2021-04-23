from candidate_retreiver import CandidateRetriever
from math import sqrt

class EuclideanDistanceCandidateRetreiver(CandidateRetriever):

    def get_candidates(self, voter, district):
        threshold = 1.0 #if a candidate falls outside this radius, the voter will not vote for him or her
        candidate_list = []
        for candidate in district.candidates:
            distance = sqrt((voter.views.get(0) - candidate.views_current.get(0)) ** 2 + (voter.views.get(1) - candidate.views_current.get(1)) ** 2)
            if distance <= threshold:
                candidate_list.append((candidate, threshold - distance))
        return sorted(candidate_list, key=lambda x: x[1], reverse=True)