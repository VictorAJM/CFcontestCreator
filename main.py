from api.methods.user import User
from api.methods.problemset import Problemset
from api.objects.submission import Submission
from api.objects.problem import Problem
from api.verdict import Verdict
import api.helper as helper

url = "https://codeforces.com/api/"

user = User("Chaska")
contest = Contest()
problemset = Problemset(['implementation', '2-sat'])
problemset2 = Problemset()

problems = problemset.problemset().requester()
for problem in problems:
  print(problem)
"""
submissions = []
cnt = 0
for submissionJSON in response['result']:
    if submissionJSON['verdict'] != Verdict.OK.value:
        continue
    problem = Problem(jsonData=submissionJSON['problem'])
    submission = Submission().setId(submissionJSON['id']).setVerdict(submissionJSON['verdict']).setProblem(problem)
    if 'contestId' in submissionJSON:
        submission.setContestId(submissionJSON['contestId'])
    submissions.append(submission)
print(f"Has resuelto: {len(submissions)} problemas!")
print(submissions[-1])
"""