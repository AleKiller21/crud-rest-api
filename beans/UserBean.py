class User:
    def __init__(self, payload):
        self.id = payload[0]
        self.first_name = payload[1]
        self.last_name = payload[2]
        self.email = payload[3]
        self.address = payload[4]
        self.gamertag = payload[5]
        self.profile_picture = payload[6]
