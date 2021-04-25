from base_modules.district_updater import DistrictUpdater
from base_modules.politics_vector import PoliticsVector
from base_modules.voter import Voter
from base_modules.candidate import Candidate
from candidate_retreivers import EuclideanDistanceCandidateRetreiver
from candidate_movements import BasicCandidateMovement
from scipy.stats import norm

class BasicDistrictUpdater(DistrictUpdater):

    def update(self, district):
        #Find the two voters furthest from a candidate
        def distance_to_closest_candidate(voter):
            min_dist = float("inf")
            for candidate in district.candidates:
                dist = voter.views.distance(candidate.views_current)
                if dist < min_dist:
                    min_dist = dist
            return min_dist
        
        sorted_voters = sorted(district.voters, key=distance_to_closest_candidate)
        voters_to_remove = sorted_voters[-2:-1]
        
        #Find the candidate furthest from the voter centroid who is not a representative
        centroid_x = 0
        centroid_y = 0
        for voter in district.voters:
            centroid_x += voter.views.get(0) / district.voters.size()
            centroid_y += voter.views.get(1) / district.voters.size()
        non_representative_candidates = [c for c in district.candidates if c not in district.representatives]
        max_dist = 0
        max_candidate = None
        for candidate in non_representative_candidates:
            distance = candidate.views_current.distance(PoliticsVector(2, [centroid_x, centroid_y]))
            if distance > max_dist:
                max_dist = distance
                max_candidate = candidate
        candidate_to_remove = max_candidate

        #Remove these people
        for voter in voters_to_remove:
            district.voters.remove(voters_to_remove)
        district.candidates.remove(candidate_to_remove)

        #Add new people
        for removed in voters_to_remove:
            voter_x = norm.rvs(loc=district.baseline_dimensions.get(0))
            voter_y = norm.rvs(loc=district.baseline_dimensions.get(1))
            voter_vector = PoliticsVector(2, [voter_x, voter_y])
            district.voters.append(Voter(voter_vector, EuclideanDistanceCandidateRetreiver()))
        candidate_x = norm.rvs(loc=district.baseline_dimensions.get(0))
        candidate_y = norm.rvs(loc=district.baseline_dimensions.get(1))
        candidate_vector = PoliticsVector(2, [candidate_x, candidate_y])
        district.candidate.append(Candidate(candidate_vector, BasicCandidateMovement()))
