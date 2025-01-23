class Contest:
    def __init__(self, gym = False):
        self.gym = gym

    def list(self):
        request = f"contest.list?gym={self.gym}"
        return request