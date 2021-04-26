from common.base_modules.voting_system import VotingSystem

class FirstPastThePostVotingSystem(VotingSystem):

    def election(self, country):
        country.legislature.clear()
        for district in country.districts:
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
                
                