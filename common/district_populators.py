from scipy.stats import norm
from common.base_modules.district_populator import DistrictPopulator
from common.base_modules.politics_vector import PoliticsVector
from common.base_modules.voter import Voter
from common.base_modules.candidate import Candidate
from common.candidate_retreivers import EuclideanDistanceCandidateRetreiver
from common.candidate_movements import BasicCandidateMovement

class BasicDistrictPopulator(DistrictPopulator):

    def populate(self, district):
        num_voters = 20
        num_candidates = 5
        candidate_retreiver = EuclideanDistanceCandidateRetreiver()
        for v in range(num_voters):
            voter_x = norm.rvs(loc=district.baseline_dimensions.get(0))
            voter_y = norm.rvs(loc=district.baseline_dimensions.get(1))
            views = PoliticsVector(2, [voter_x, voter_y])
            district.voters.append(Voter(views, candidate_retreiver))
        candidate_movement = BasicCandidateMovement()
        for c in range(num_candidates):
            candidate_x = norm.rvs(loc=district.baseline_dimensions.get(0))
            candidate_y = norm.rvs(loc=district.baseline_dimensions.get(1))
            views = PoliticsVector(2, [candidate_x, candidate_y])
            district.candidates.append(Candidate(views, candidate_movement))

