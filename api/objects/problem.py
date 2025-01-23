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
    
    def setIndex(self, index):
        self.index = index
        return self

    def setName(self, name):
        self.name = name
        return self
    
    def setRating(self, rating):
        self.rating = rating
        return self

    def setTags(self, tags):
        self.tags = tags
        return self
    
    def addTag(self, tag):
        self.tag.append(tag)
        return self

    def __str__(self):
        return f"[contestId:{self.contestId}, index:{self.index}, name:{self.name}, rating:{self.rating}, tags:{self.tags}]"