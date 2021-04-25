from common.base_modules.candidate_movement import CandidateMovement
from common.base_modules.politics_vector import PoliticsVector

class BasicCandidateMovement(CandidateMovement):

    def move(self, candidate, district):
        tolerable_radius = 0.1
        centroid_x = 0
        centroid_y = 0
        for voter in district.voters:
            centroid_x += voter.views.get(0) / district.voters.size()
            centroid_y += voter.views.get(1) / district.voters.size()
        distance = candidate.views_base.distance(PoliticsVector(2, [centroid_x, centroid_y]))
        if distance <= tolerable_radius:
            candidate.views_current = PoliticsVector(2, [centroid_x, centroid_y])
        else:
            ratio = tolerable_radius / distance
            new_x = candidate.views_base(0) + (centroid_x - candidate.views_base.get(0)) * ratio
            new_y = candidate.views_base(1) + (centroid_y - candidate.views_base.get(1)) * ratio
            candidate.views_current = PoliticsVector(2, [new_x, new_y])