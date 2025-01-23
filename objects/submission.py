class Submission:
    def __init__(
            self, id = None, contestId = None,
            problem = None, verdict = None):
        self.id = id
        self.contestId = contestId
        #self.problem = problem
        self.verdict = verdict
    
    def setId(self, id):
        self.id = id
        return self
    
    def setContestId(self, contestId):
        self.contestId = contestId
        return self
    #**
    #def setProblem(self, problem):
    #    self.problem = problem
    #    return self 
    #

    def setVerdict(self, verdict):
        self.verdict = verdict
        return self
    
    def text(self):
        return f"id={self.id}, contestId={self.contestId}, verdict={self.verdict}"