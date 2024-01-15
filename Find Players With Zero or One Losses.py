class Solution:
    def findWinners(self, matches):
        wins, losses = {}, {}

        for winner, loser in matches:
            wins[winner] = wins.get(winner, 0) + 1
            losses[loser] = losses.get(loser, 0) + 1

        not_lost_any = [player for player in set(wins.keys()) if player not in losses]
        lost_once = [player for player, count in losses.items() if count == 1]

        return [sorted(not_lost_any), sorted(lost_once)]
