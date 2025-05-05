from api.tags import Tags

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
  
  def getTags(self):
    rawTags = self.data["tags"] if "tags" in self.data else ""
    rawTags = rawTags.split(',')
    rawTags = [tag.strip().upper() for tag in rawTags]

    tags = [Tags[tag].value for tag in rawTags if tag in Tags.__members__]
    return tags
  
  def getFilterTags(self, failed="OR"):
    filterTags = self.data["filterTagsBy"] if "filterTagsBy" in self.data else failed
    return filterTags
