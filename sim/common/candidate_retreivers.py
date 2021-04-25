from base_modules.candidate_retreiver import CandidateRetriever

class EuclideanDistanceCandidateRetreiver(CandidateRetriever):

    def get_candidates(self, voter, district):
        threshold = 1.0 #if a candidate falls outside this radius, the voter will not vote for him or her
        candidate_list = []
        for candidate in district.candidates:
            distance = voter.views.distance(candidate.views_current)
            if distance <= threshold:
                candidate_list.append((candidate, threshold - distance))
        return sorted(candidate_list, key=lambda x: x[1], reverse=True)