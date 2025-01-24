from api.methods.apiCall import APICall
from api.objects.submission import Submission
from api.objects.problem import Problem
class User:
    def __init__(self, handle):
        self.handle = handle
    
    def info(self):
        return UserInfo(self.handle)
    
    def rating(self):
        return UserRating(self.handle)
    
    def status(self):
        return UserStatus(self.handle)
    
class UserInfo(APICall):
    def __init__(self, handle):
        super().__init__()
        self.handle = handle
        self.setRequest()

    def responseObject(self, response):
        return response['result'][0]

    def setRequest(self):
       self.request = self.requestBase + f"user.info?handles={self.handle}"

class UserRating(APICall):
    def __init__(self, handle):
        super().__init__()
        self.handle = handle
        self.setRequest()
    
    def responseObject(self, response):
        return response['result'][-1]['newRating']
    
    def setRequest(self):
        self.request = self.requestBase + f"user.rating?handle={self.handle}"

class UserStatus(APICall):
    def __init__(self, handle):
        super().__init__()
        self.handle = handle
        self.setRequest()
    
    def responseObject(self, response):
        submissions = []
        for submissionJSON in response['result']:
            problem = Problem(jsonData=submissionJSON['problem'])
            submission = Submission().setId(submissionJSON['id']).setVerdict(submissionJSON['verdict']).setProblem(problem)
            if 'contestId' in submissionJSON:
                submission.setContestId(submissionJSON['contestId'])
            submissions.append(submission)
        return submissions

    def setRequest(self):
        self.request = self.requestBase + f"user.status?handle={self.handle}"