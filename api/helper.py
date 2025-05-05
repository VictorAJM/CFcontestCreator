import random
from api.methods.user import User
from api.methods.problemset import Problemset
from api.verdict import Verdict
from api.objects.data import Data

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

def filterProblemsBy(problems, minimumRating = 0, maximumRating = 9999, minimumSolvedCount = 0, maximumSolvedCount = 999999, tags = [], filterTagsBy = "OR"):
  _problems = []
  for problem in problems:
    if problem.getRating() is None: continue
    if minimumRating > problem.getRating(): continue
    if maximumRating < problem.getRating(): continue
    if minimumSolvedCount > problem.getSolvedCount(): continue
    if maximumSolvedCount < problem.getSolvedCount(): continue
    
    problem_tags = problem.getTags()
    if len(tags) > 0:
      if filterTagsBy == "AND":
        all_tags_present = all(tag in problem_tags for tag in tags)
        if all_tags_present:
          _problems.append(problem)
      else:
        any_tag_present = any(tag in problem_tags for tag in tags)
        if any_tag_present:
          _problems.append(problem)
    else:
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

def getProblems(__data):
  
  data = Data(__data)
  handle = data.getHandle()
  problems = data.getProblems()
  minimumRating = data.getMinimumRating()
  maximumRating = data.getMaximumRating()
  minimumSolvedCount = data.getMinimumSolvedCount(failed = 0)
  maximumSolvedCount = data.getMaximumSolvedCount(failed = 999999)
  tags = data.getTags()
  filterTags = data.getFilterTags()
  
  availableProblems = getNotTriedProblems(handle)
  validProblems = filterProblemsBy(availableProblems, minimumRating = minimumRating, maximumRating=maximumRating, minimumSolvedCount = minimumSolvedCount, maximumSolvedCount = maximumSolvedCount, tags = tags, filterTagsBy=filterTags)
  if len(validProblems) < problems:
    print("No hay problemas suficientes :(")
    return []
  
  problems = random.sample(validProblems, problems)
  return problems