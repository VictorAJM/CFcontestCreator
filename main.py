from api.methods.user import User
from api.methods.contest import Contest
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

_url = url + user.info()
# helper.requester(_url)

_url = url + user.blogEntries()
# helper.requester(_url)

_url = url + user.rating()
# helper.requester(_url)

_url = url + contest.list()
#helper.requester(_url)

_url = url + problemset.problems()
#helper.requester(_url)

_url = url + problemset2.problems()
#helper.requester(_url)

_url = url + user.status()
response = helper.requester(_url)

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