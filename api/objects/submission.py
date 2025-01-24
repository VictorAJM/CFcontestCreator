class Submission:
    def __init__(
            self, id = None, contestId = None,
            problem = None, verdict = None):
        self.id = id
        self.contestId = contestId
        self.problem = problem
        self.verdict = verdict
    
    def setId(self, id):
        self.id = id
        return self
    
    def getId(self):
        return self.id
    
    def setContestId(self, contestId):
        self.contestId = contestId
        return self
    
    def getContestId(self):
        return self.contestId
    
    def setProblem(self, problem):
        self.problem = problem
        return self 
    
    def getProblem(self):
        return self.problem

    def setVerdict(self, verdict):
        self.verdict = verdict
        return self

    def getVerdict(self):
        return self.verdict
    
    def __str__(self):
        return f"id={self.id}, contestId={self.contestId},problem={self.problem}, verdict={self.verdict}"