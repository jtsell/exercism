class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        self.sorted = scores[:]
        self.sorted.sort(reverse=True)
    
    def scores(self):
        return self.scores
    
    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return self.sorted[0]
    
    def personal_top_three(self):
        return self.sorted[:3]

