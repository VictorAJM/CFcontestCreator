class Data:
  def __init__(self, data):
    self.data = data
    
  def getHandle(self):
    return self.data["handle"]
  
  def getProblems(self):
    return int(self.data["problems"])
  
  def getMinimumRating(self, failed = 800):
    if "minimumRating" in self.data:
      return int(self.data["minimumRating"])
    return failed
  
  def getMaximumRating(self, failed = 3600):
    if "maximumRating" in self.data:
      return int(self.data["maximumRating"])
    return failed
  
  def getMinimumSolvedCount(self, failed = 0):
    if "minimumSolvedCount" in self.data:
      return int(self.data["minimumSolvedCount"])
    return failed
  
  def getMaximumSolvedCount(self, failed = 99999):
    if "maximumSolvedCount" in self.data:
      return int(self.data["maximumSolvedCount"])
    return failed
  
  def getProblemsFolder(self, failed=''):
    if "problemsFolder" in self.data:
      return self.data["problemsFolder"]
    return failed