class User:
    def __init__(self, handle):
        self.handle = handle
    
    def info(self):
        request = f"user.info?handles={self.handle}"
        return request