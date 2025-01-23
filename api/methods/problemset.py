class Problemset:
    def __init__(self, tags = []):
        self.tags = tags

    def __tagsToString(self):
        stringTags = ';'.join(map(str, self.tags))
        return stringTags

    def problems(self):
        request = f"problemset.problems?tags={self.__tagsToString()}"
        return request