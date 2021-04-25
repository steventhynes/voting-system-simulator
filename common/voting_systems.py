from base_modules.voting_system import VotingSystem

class FirstPastThePostVotingSystem(VotingSystem):

    def election(self, country):
        country.legislature.clear()
        for district in country.districts:
            count = {}
            for candidate in district.candidates:
                count[candidate] = 0
            for voter in district.voters:
                candidates = voter.candidate_retreiver.get_candidates(voter, district)
                count[candidates[0]] += voter.vote_power
            winner = max(count, key=lambda c: count[c])
            district.representatives = [winner]
            country.legislature.append(winner)
        

class RankedChoiceVotingSystem(VotingSystem):

    def election(self, country):
        country.legislature.clear()
        for district in country.districts:
            total_vote_power = sum([v.vote_power for v in country.voters])
            vote_lists = []
            for voter in district.voters:
                candidates = voter.candidate_retreiver.get_candidates(voter, district)
                vote_lists.append([candidates, 0, voter.vote_power])
            count = {}
            winner = None
            while True:
                for candidate in district.candidates:
                    count[candidate] = 0
                for vote_list in vote_lists:
                    if vote_list[1] < len(vote_list[0]):
                        count[vote_list[0][vote_list[1]]] += vote_list[2]
                winner = max(count, key=lambda c: count[c])
                loser = min(count, key=lambda c: count[c])
                if count[winner] > total_vote_power / 2:
                    break
                else:
                    del count[loser]
                    for vote_list in vote_lists:
                        while vote_list[1] < len(vote_list[0]) and vote_list[0][vote_list[1]] not in count:
                            vote_list[1] += 1
            district.representatives = [winner]
            country.legislature.append(winner)
                
                