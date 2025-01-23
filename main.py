from methods.user import User
from methods.contest import Contest
from methods.problemset import Problemset
from objects.submission import Submission
import helper

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
for submissionJSON in response['result']:
    submission = Submission().setId(submissionJSON['id']).setContestId(submissionJSON['contestId']).setVerdict(submissionJSON['verdict'])
    print(submission.text())
    submissions.append(submission)

print(len(submissions))