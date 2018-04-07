class Game:
    def __init__(self, payload):
        self.id = payload[0]
        self.name = payload[1]
        self.developer = payload[2]
        self.publisher = payload[3]
        self.price = payload[4]
        self.description = payload[5]
