from api.methods.apiCall import APICall
from api.objects.problem import Problem
class Problemset:
    def __init__(self, tags = []):
        self.tags = self.__tagsToString(tags)

    def __tagsToString(self, tags):
        stringTags = ';'.join(map(str, tags))
        return stringTags

    def problemset(self):
        return ProblemsetProblems(self.tags)

class ProblemsetProblems(APICall):
    def __init__(self, tags):
        super().__init__()
        self.tags = tags
        self.setRequest()

    def responseObject(self, response):
        problems = []
        solvedCount = []
        for JSON in response['result']['problemStatistics']:
          solvedCount.append(JSON['solvedCount'])
        for idx, JSON in enumerate(response['result']['problems']):
            problem = Problem(jsonData=JSON, solvedCount=solvedCount[idx])
            problems.append(problem)
        return problems

    def setRequest(self):
        self.request = self.requestBase + f"problemset.problems?tags={self.tags}"