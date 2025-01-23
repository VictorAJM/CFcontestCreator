from methods.user import User
from methods.contest import Contest

import helper

url = "https://codeforces.com/api/"

user = User("Chaska")
contest = Contest()

_url = url + user.info()
# helper.requester(_url)

_url = url + user.blogEntries()
# helper.requester(_url)

_url = url + user.rating()
# helper.requester(_url)

_url = url + contest.list()
helper.requester(_url)