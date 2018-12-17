class CONNECTION:
    def __init__(self, station1, station2, duration):
        self.station1 = station1
        self.station2 = station2
        self.duration = duration
        self.critic = False
        self.used = False
    def setCritic(self, critic):
        self.critic = critic
    def setUsed(self, used):
        self.used = used