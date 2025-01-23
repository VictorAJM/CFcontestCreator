from methods.user import User
import helper

url = "https://codeforces.com/api/"

user = User("Chaska")
url = url + user.info()

print(url)

helper.requester(url)