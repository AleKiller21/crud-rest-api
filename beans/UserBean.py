class User:
    def __init__(self, payload):
        self.id = payload[0]
        self.first_name = payload[1]
        self.last_name = payload[2]
        self.email = payload[3]
        self.address = payload[4]
        self.gamertag = payload[5]
        self.profile_picture = payload[6]

    def to_dictionary(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'address': self.address,
            'gamertag': self.gamertag,
            'profile_picture': self.profile_picture
        }