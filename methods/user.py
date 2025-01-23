class User:
    def __init__(self, handle):
        self.handle = handle
    
    def info(self):
        request = f"user.info?handles={self.handle}"
        return request

    def blogEntries(self):
        request = f"user.blogEntries?handles={self.handle}"
        return request

    def rating(self):
        request = f"user.rating?handle={self.handle}"
        return request

    def status(self):
        request = f"user.status?handle={self.handle}&count=2"
        return request