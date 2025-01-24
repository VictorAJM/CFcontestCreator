from api.methods.user import User
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