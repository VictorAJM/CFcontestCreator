from methods.user import User
import helper

url = "https://codeforces.com/api/"

user = User("Chaska")
_url = url + user.info()

helper.requester(_url)

_url = url + user.blogEntries()
helper.requester(_url)

_url = url + user.rating()
helper.requester(_url)