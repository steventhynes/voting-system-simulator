from common.base_modules.voting_system import VotingSystem
from math import floor

class FirstPastThePostVotingSystem(VotingSystem):

    def election(self, country):
        country.legislature.clear()
        for district in country.districts:
            district.representatives.clear()
            count = {}
            for candidate in district.candidates:
                count[candidate] = 0
            for voter in district.voters:
                candidates = voter.candidate_retreiver.get_candidates(voter, district)
                if candidates:
                    count[candidates[0][0]] += voter.vote_power
            winner = max(count, key=lambda c: count[c])
            district.representatives = [winner]
            country.legislature.append(winner)
        

class RankedChoiceVotingSystem(VotingSystem):

    def election(self, country):
        country.legislature.clear()
        for district in country.districts:
            district.representatives.clear()
            vote_lists = []
            for voter in district.voters:
                candidates = voter.candidate_retreiver.get_candidates(voter, district)
                if candidates:
                    vote_lists.append([candidates, 0, voter.vote_power])
            count = {}
            for candidate in district.candidates:
                count[candidate] = 0
            winner = None
            while True:
                for candidate in count:
                    count[candidate] = 0
                for vote_list in vote_lists:
                    if vote_list[1] < len(vote_list[0]):
                        count[vote_list[0][vote_list[1]][0]] += vote_list[2]
                winner = max(count, key=lambda c: count[c])
                loser = min(count, key=lambda c: count[c])
                vote_sum = sum(count[c] for c in count)
                if count[winner] > vote_sum / 2:
                    break
                else:
                    del count[loser]
                    for vote_list in vote_lists:
                        while vote_list[1] < len(vote_list[0]) and vote_list[0][vote_list[1]][0] not in count:
                            vote_list[1] += 1
            district.representatives = [winner]
            country.legislature.append(winner)
                
class SingleTransferableVoteVotingSystem(VotingSystem):

    def election(self, country):
        country.legislature.clear()
        for district in country.districts:
            num_seats = 2
            district.representatives.clear()
            vote_lists = []
            for voter in district.voters:
                candidates = voter.candidate_retreiver.get_candidates(voter, district)
                if candidates:
                    vote_lists.append([candidates, 0, voter.vote_power])
            count = {}
            for candidate in district.candidates:
                count[candidate] = 0
            winners = []
            remaining_seats = num_seats
            while True:
                for candidate in count:
                    count[candidate] = 0
                for vote_list in vote_lists:
                    if vote_list[1] < len(vote_list[0]):
                        count[vote_list[0][vote_list[1]][0]] += vote_list[2]
                loser = min(count, key=lambda c: count[c])
                vote_sum = sum(count[c] for c in count)
                required_votes = floor(vote_sum / (remaining_seats + 1)) + 1
                for candidate in count:
                    surplus = count[candidate] - required_votes
                    if surplus >= 0:
                        winners.append(candidate)
                        surplus_ratio = surplus / count[candidate]
                        for vote_list in vote_lists:
                            if vote_list[1] < len(vote_list[0]) and vote_list[0][vote_list[1]][0] is candidate:
                                vote_list[2] *= surplus_ratio
                for candidate in winners:
                    if candidate in count:
                        del count[candidate]
                        remaining_seats -= 1
                if len(winners) == num_seats:
                    break
                else:
                    del count[loser]
                    for vote_list in vote_lists:
                        while vote_list[1] < len(vote_list[0]) and vote_list[0][vote_list[1]][0] not in count:
                            vote_list[1] += 1
            district.representatives.extend(winners)
            country.legislature.extend(winners)
                