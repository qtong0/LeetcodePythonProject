from sortedcontainers import SortedDict


class Leaderboard:

    def __init__(self):
        self.scores = {}
        # {score: times_scores_happens}
        self.sortedScores = SortedDict()


    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            val = self.sortedScores.get(-preScore)
            if val == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = val + 1
            newScore = preScore + score
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1


    def top(self, K: int) -> int:
        count, total = 0, 0

        for key, value in self.sortedScores.items():
            times = self.sortedScores.get(key)
            for _ in range(times):
                total += -key
                count += 1
                if count == K:
                    break
            if count == K:
                break

        return total


    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId]



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
