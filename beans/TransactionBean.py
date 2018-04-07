class Transaction:
    def __init__(self, payload):
        self.order_number = payload[0]
        self.user_id = payload[1]
        self.game_id = payload[2]