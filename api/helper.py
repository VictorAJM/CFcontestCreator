import random
from api.methods.user import User
from api.methods.problemset import Problemset
from api.verdict import Verdict

def filterSubmissionBy(submissions, verdict = None, rating = None):
  _submissions = []
  for submission in submissions:
    if verdict is not None and submission.getVerdict() == verdict:
      _submissions.append(submission)
      continue
    if rating is not None and submission.getProblem().getRating() == rating:
      _submissions.append(submission)
      continue
  return _submissions

def filterProblemsBy(problems, rating = None):
  _problems = []
  for problem in problems:
    if rating is not None and problem.getRating() == rating:
      _problems.append(problem)
  return _problems

def getProblemsFromSolutions(submissions):
  problems = []
  problemNames = []
  for submission in submissions:
    if submission.getProblem().getName() not in problemNames:
        problems.append(submission.getProblem())
        problemNames.append(submission.getProblem().getName())
  return problems

def averageRating(problems):
  totalRating = 0
  for problem in problems:
    if problem.getRating() is not None:
      totalRating += problem.getRating()
  totalRating /= len(problems)
  return totalRating

def averageRatingSolvedProblems(handle):
  user = User(handle).status()
  submissions = user.requester()
  okSubmissions = filterSubmissionBy(submissions, verdict = Verdict.OK.value)
  solvedProblems = getProblemsFromSolutions(okSubmissions)
  return f"Tu rating promedio de problemas resueltos es: {averageRating(solvedProblems)} entre {len(solvedProblems)} problemas"

def getNotTriedProblems(handle):
  user = User(handle).status()
  submissions = user.requester()
  problemset = (Problemset().problemset()).requester()
  problemsTriedName = set()
  _problems = []
  for submission in submissions:
    problemsTriedName.add(submission.getProblem().getName())
  for problem in problemset:
    if problem.getName() not in problemsTriedName:
      _problems.append(problem)
  return _problems

def getProblems(handle, problems, rating):
  availableProblems = getNotTriedProblems(handle)
  validProblems = filterProblemsBy(availableProblems, rating = rating)
  if len(validProblems) < problems:
    print("No hay problemas suficientes :(")
    return
  
  randomProblems = random.sample(validProblems, problems)
  problems  = [[prob.getName(), prob.getUrl()] for prob in randomProblems]
  return problems