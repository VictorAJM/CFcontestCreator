class Problem:
    def __init__(
            self, contestId = None, index = None, name = None, rating = None,
            tags = [], jsonData = None
    ):
        self.contestId = contestId
        self.index = index
        self.name = name
        self.rating = rating
        self.tags = tags
        if jsonData is not None:
            if 'contestId' in jsonData:
                self.contestId = jsonData['contestId']
            if 'index' in jsonData:
                self.index = jsonData['index']
            if 'name' in jsonData:
                self.name = jsonData['name']
            if 'rating' in jsonData:
                self.rating = jsonData['rating']
            if 'tags' in jsonData:
                self.tags = jsonData['tags'] 
    
    def setContestId(self, contestId):
        self.contestId = contestId
        return self
    
    def getContestId(self):
        return self.contestId
    
    def setIndex(self, index):
        self.index = index
        return self
    
    def getIndex(self):
        return self.index

    def setName(self, name):
        self.name = name
        return self
    
    def getName(self):
        return self.name
    
    def setRating(self, rating):
        self.rating = rating
        return self
    
    def getRating(self):
        return self.rating

    def setTags(self, tags):
        self.tags = tags
        return self
    
    def getTags(self):
        return self.tags
    
    def addTag(self, tag):
        self.tag.append(tag)
        return self

    def getUrl(self):
        return f"https://codeforces.com/contest/{self.contestId}/problem/{self.index}"

    def __str__(self):
        return f"[contestId:{self.contestId}, index:{self.index}, name:{self.name}, rating:{self.rating}, tags:{self.tags}]"